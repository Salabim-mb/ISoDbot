import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import Isod


def run():
    errorMessages = {}

    number_of_test = 5
    counter = 0

    if Isod.verifyData('polaczej', '6pVev7sf') != 0:
        counter += 1
    else:
        errorMessages['użytkownik: polaczej'] = 'stan faktyczny: konto istnieje, wynik testu: konto nie istnieje'

    if Isod.verifyData('ćwirćwir', 'blabla') == 0:
        counter += 1
    else:
        errorMessages['użytkownik: ćwirćwir'] = 'stan faktyczny: konto nie istnieje, wynik testu: konto istnieje'

    if Isod.verifyData('boguszj', '4qivPZKX') != 0:
        counter += 1
    else:
        errorMessages['użytkownik: boguszj'] = 'stan faktyczny: konto istnieje, wynik testu: konto nie istnieje'

    if Isod.verifyData('swiderj', 'afhLNWdi') != 0:
        counter += 1
    else:
        errorMessages['użytkownik: swiderj'] = 'stan faktyczny: konto istnieje, wynik testu: konto nie istnieje'

    if Isod.verifyData('balasm', 'K33lH@ul') != 0:
        counter += 1
    else:
        errorMessages['użytkownik: balasm'] = 'stan faktyczny: konto istnieje, wynik testu: konto nie istnieje'


    errorMessages['ilość testów'] = number_of_test
    errorMessages['ilość testów zaliczonych'] = counter

    return errorMessages

print(run())