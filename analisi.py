import numpy as np
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import pandas as pd
import os
from matplotlib.pyplot import *
import matplotlib.pyplot as plt


np.set_printoptions(suppress=True)

def f(x, a, b, c):
    return a * x ** 2 + b * x + c

def vertice(array):
    return np.divide(-popt[1], 2.*popt[0]), np.divide(-np.power(array[1],2.), 4.*array[0]) + array[2]

def find_nearest(array, value):
    idx = np.argmin(_ for _ in array if i > value)
    return idx, array[idx]

def Maxima(time, data):
    for index, i in enumerate(data):
        maximum = np.argmax(i)
        xdata = [0, 1, 2]
        if maximum == 1:
            popt, _ = curve_fit(f, xdata, i[maximum-1:maximum+2])
        else:
            pass
        tmax, Emax = vertice(popt)
        t_needed, E_needed = find_nearest( i, Emax / 2.0)

def lettura_file(files):
    data = pd.read_csv(files, sep=' ')
    data = np.transpose(data.values)
    data = data.tolist()
    timestamp = data[14]; del data[14]; time = np.asarray(timestamp)
    del data[0:9]
    data = np.transpose(np.asarray(data, dtype=np.float64))
    data = pd.DataFrame(data)
    data = data[data.columns[::-1]]
    data = data.values
    return timestamp, data

if __name__=='__main__':
    #working = os.path.realpath('/run/media/wronsmin/Storage/Dataset/160908/Peak_Finder')
    #list_path = []
    #for i in os.listdir(working):
    #    list_path.append(working + '/' + i)

    tmp = 'peak_finder_dump_fifo_1ch_lkrl0-fe-1a01_Thu__08_Sep_2016_15-28-46.csv'
    timestamp, data = lettura_file(tmp)
    maximum = np.argmax(data[0])
    if maximum == 1:
        xdata = [0, 1, 2]; xdata = np.asarray(xdata)
        popt, _ = curve_fit(f, xdata, data[0][0:3])
    else:
        pass
    tmax, Emax = vertice(popt)
    t_needed, E_needed = find_nearest(data[0], Emax / 2.0)
    plot(data[0])
    print(tmax, Emax, t_needed, E_needed)
    xdata = np.linspace(0,6,50)
    plot(xdata, f(xdata, *popt))
    show()
