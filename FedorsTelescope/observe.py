import os
import sys
from time import sleep


#Input observation parameters
f_center = str(1420.4057517)
f_center = str(float(f_center)*10**6)
bandwidth = str(2.4)
bandwidth = str(float(bandwidth)*10**6)
channels = str(1024)
t_int = str(1)
nbins = str(int(float(t_int) * float(bandwidth)/float(channels)))
duration = str(obst)

#Calibration option
cal=True

#Delete pre-existing observation.dat & plot.png files
try:
    os.remove('observation.dat')
    os.remove('plot.png')
except OSError:
    pass

#Execute top_block.py with parameters
sys.argv = ['top_block.py', '--c-freq='+f_center, '--samp-rate='+bandwidth, '--nchan='+channels, '--nbin='+nbins, '--obs-time='+duration]
execfile('top_block.py')

#Execute plotter
if cal:
    sys.argv = ['plot_hi.py', 'freq='+f_center, 'samp_rate='+bandwidth, 'nchan='+channels, 'nbin='+nbins]
    execfile('plot_hi.py')
else:
    sys.argv = ['plot.py', 'freq='+f_center, 'samp_rate='+bandwidth, 'nchan='+channels, 'nbin='+nbins]
    execfile('plot.py')