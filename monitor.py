def monitor_successfiles(foldername, filenames=None, time_wait='1h', time_max='48h'):
    '''Monitor the presence of success files in a folder
    
    Parameters:
      time_max (int or str): if int, max number of seconds to wait. If string, it
      has to be something like '48h', which is then converted into seconds.
    '''
    def convert_timetring(time):
        if isinstance(time, basestring):
            unit = time[-1]
            if unit == 'h':
                factor = 3600
            elif unit == 'm':
                factor = 60
            elif unit == 's':
                factor = 1
            else:
                raise ValueError('Time unit not understood')
            time = int(time[:-1]) * factor
        return int(time)


    def clean_foldername(foldername):
        import os
        return foldername.rstrip(os.sep)+os.sep


    def clean_filename(foldername):
        import os
        return foldername.lstrip(os.sep)


    def check_single_file(filename):
        '''Check existance of single file'''
        import os.path
        return os.path.isfile(filename)

    # Get input time parameters
    time_wait = convert_timetring(time_wait)
    time_max = convert_timetring(time_max)

    # Get the foldername paramter
    foldername = clean_foldername(foldername)

    # Get the filenames parameters, relative to the foldername
    if filenames is None:
        import os
        filenames = os.listdir(foldername)
    # NOTE: Transform into absolute paths
    filenames_abs = [foldername+clean_filename(fn) for fn in filenames]

    # Monitor files
    import time
    t = 0
    while t < time_max:
        if all(map(check_single_file, filenames_abs)):
            break
        time.sleep(time_wait)
        t += time_wait
    else:
        return 'Maximal time reached'

    return 'OK'
