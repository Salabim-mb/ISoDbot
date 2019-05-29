import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from Utils import *


def run():
    errorMessages = {}

    number_of_test = 5
    counter = 0

    if (Utils.wantToGetPlan('poniedziałek') != -1):
        counter += 1
    else:
        errorMessages['poniedziałek'] = 'stan faktyczny: poniedziałek, wynik testu: nieznana komenda'
    if (Utils.wantToGetPlan('wtorek') != -1):
        counter += 1
    else:
        errorMessages['wtorek'] = 'stan faktyczny: wtorek, wynik testu: nieznana komenda'
    if (Utils.wantToGetPlan('środa') != -1):
        counter += 1
    else:
        errorMessages['środa'] = 'stan faktyczny: środa, wynik testu: nieznana komenda'
    if (Utils.wantToGetPlan('czwartek') != -1):
        counter += 1
    else:
        errorMessages['czwartek'] = 'stan faktyczny: czwartek, wynik testu: nieznana komenda'
    if (Utils.wantToGetPlan('piątek') != -1):
        counter += 1
    else:
        errorMessages['piątek'] = 'stan faktyczny: piąteczek, piątunio, wynik testu: nieznana komenda'

    errorMessages['ilość testów'] = number_of_test
    errorMessages['ilość testów zaliczonych'] = counter

    return errorMessages
