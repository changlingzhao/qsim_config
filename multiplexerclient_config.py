class multiplexer_config(object):
    '''
    multiplexer client configuration file
    
    Attributes
    ----------
    info: dict
    {channel_name: (port, hint, display_location, stretched, display_pid, dac, dac_rails)}
    '''
    info = {
            '369': (8, '811.291540', (0,2), True, True, 3, [-.4,.4]),
            '935': (2, '320.571975', (0,3), True, True, 2, [-5.,5.]),
	    '399': (6, '751.526670', (0,4), True, True, 1, [-.5,.5]),
            }
    ip = '10.97.112.2'
    