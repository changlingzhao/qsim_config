class config(object):

    """
    scriptscanner config object for the molecules experiment.
    """
    # Folder names within the experiments folder that holder experiments
    exps = 'Qsim.scripts.experiments.'

    # list in the format (import_path, class_name)
    scripts = [(exps + 'tickle.tickle_experiment', 'ticklescan'),
	       (exps + 'wavemeter_linescan.wavemeter_linescan', 'wavemeter_linescan'),
               (exps + 'test_DDS_channels.DDS_test_channels', 'DDS_test_channels'),
	       (exps + 'laser_stability_monitor.laser_stability_monitor', 'lasermonitor'),
	       (exps + 'FFT.PMT_FFT', 'fft_spectrum'),
	       (exps + 'TD_Flourescence.TD_flourescence', 'TD_flourescence'),
	       (exps + 'interleaved_linescan.interleaved_linescan', 'InterleavedLinescan'),
	       (exps + 'ML_Piezo_scan.ML_Piezo_scan', 'MLpiezoscan'),
	       (exps + 'line_narrowing.Line_Narrowing', 'Line_Narrowing')
               ]
    scripts.append((exps + 'dds_linescan.dds_linescan', 'DDSLinescan'))

    allowed_concurrent = {}
    allowed_concurrent['lasermonitor'] = ['lasermonitor']

    launch_history = 1000
