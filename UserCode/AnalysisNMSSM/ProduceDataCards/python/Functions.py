import time
import sys
import os



def RejectHistogram(DIRNAME, HISTNAME):
    reject = False
    D = str(DIRNAME)
    H = str(HISTNAME)
    if 'eleTau' in D and 'mutau' in H :
           reject = True
    if 'muTau' in D and 'etau' in H :
           reject = True
    if '_btag_' in D and '_nobtag_' in H :
           reject = True
    if '_nobtag_' in D and '_btag_' in H :
           reject = True
    if '_btag' in D and '_nobtag_' in H :
           reject = True
    if '_nobtag' in D and '_btag_' in H :
           reject = True
    if 'inclusive' in D and 'btag' in H:
           reject = True
    if '_nobtag_low' in D and '_nobtag_high' in H:
           reject = True
    if '_nobtag_low' in D and '_nobtag_medium' in H:
           reject = True
    if '_nobtag_medium' in D and '_nobtag_low' in H:
            reject = True
    if '_nobtag_medium' in D and '_nobtag_high' in H:
            reject = True
    if '_nobtag_high' in D and '_nobtag_low' in H:
            reject = True
    if '_nobtag_high' in D and '_nobtag_medium' in H:
            reject = True
    if '_btag_low' in D and '_btag_high' in H:
           reject = True
    if '_btag_low' in D and '_btag_medium' in H:
           reject = True
    if '_btag_medium' in D and '_btag_low' in H:
            reject = True
    if '_btag_medium' in D and '_btag_high' in H:
            reject = True
    if '_btag_high' in D and '_btag_low' in H:
            reject = True
    if '_btag_high' in D and '_btag_medium' in H:
            reject = True
    if '_btag' in D and '_nobtag_8' in H:
              reject = True
    if '_nobtag' in D and '_btag_8' in H:
              reject = True
    if 'btag' in D and 'btag_' not in D:
        if 'low' in H and 'lowMass' not in H: reject = True
        if 'medium' in H: reject = True
        if 'high' in H: reject = True
    if 'btag_' in D:
        if 'btag' in H and 'low' not in H and 'medium' not in H and 'high' not in H:
            reject = True

    return reject
