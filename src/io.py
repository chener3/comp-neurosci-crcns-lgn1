# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for file IO"""
from __future__ import print_function, division, absolute_import
#I choose another dataset from the CRCNS, which is lgn-1. 

#These files contain the spiking responses of LGN neurons in the mouse to drifting gratings.
#Each file contains the spiking responses and stimulus specifications for a single neuron.

from scipy.io import loadmat

neuron1 = loadmat("data/mouselgn/mlgnori_01.mat")   #load data, loading one in MatLab will bring a structure called mlgn into MatLab's memory
print(neuron1.keys())                               #check the keys
print(neuron1)                                      #check the data

print("mlgn ->", neuron1["mlgn"])                  # You access elements of a dict by key using the familiar bracket syntax:
print("spktimes of mlgn ->",neuron1["mlgn"]["spktimes"])  # the spktimes of mlgn, MxNxT size array, where M is the stimulus number, N is the repeat number and T is time in milliseconds
print("stim of mlgn ->",neuron1["mlgn"]["stim"])          # the stim of mlgn, M size array, where M is the number of stimulus conditions
from os import path
import glob

def load_spikes(fname):
    """Load spikes from a file in flat ascii format"""
    with open(fname, "rt") as fp:
        return [np.fromstring(line, sep=" ") for line in fp]

# The '*' character will match any file name, so this `glob` call will return a list
# of all the files in `data/mouselgn/`
for dirname in glob.glob("data/mouselgn/*"):
    neuron = path.basename(dirname)
    print(" neuron:", neuron)
    for respfile in glob.glob(path.join(dirname, "*")):
        stim = path.splitext(path.basename(respfile))[0]
        print("  stim:", stim)
        for i, trial in enumerate(load_spikes(respfile)):
            print("   trial", i, ":", len(trial), "spikes")

spike_data = {}
for dirname in glob.glob("data/mouselgn/*"):
    neuron = path.basename(dirname)
    animal = neuron.split("_")[0]
    stims = []
    for respfile in glob.glob(path.join(dirname, "*")):
        stim = path.splitext(path.basename(respfile))[0]
        trials = load_spikes(respfile)
        stims.append({"stimulus": stim, "response": trials})
    ndata = {"animal": animal, "stimuli": stims}
    spike_data[neuron] = ndata