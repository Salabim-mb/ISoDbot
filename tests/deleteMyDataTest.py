import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Utils import *

def run():

	errorMessages = {}

	number_of_test = 6
	counter = 0

	if(Utils.delete_my_data('user6.tst') == -1):
		counter+=1
	else:
		errorMessages['plik: user1.tst'] = 'oczekiwany wynik: brak próby usunięcia nieistniejącego pliku, wynik testu: podjęto próbę usunięcia niestniejącego pliku'

	try:
		f = open('user1.tst', 'r')
		errorMessages['plik: user1.tst'] = 'oczekiwany wynik: usunięto plik, wynik testu: plik wciąż istnieje'
	except FileNotFoundError:
		counter+=1
	try:
		f = open('user2.tst', 'r')
		errorMessages['plik: user2.tst'] = 'oczekiwany wynik: usunięto plik, wynik testu: plik wciąż istnieje'
	except FileNotFoundError:
		counter+=1
	try:
		f = open('user3.tst', 'r')
		errorMessages['plik: user3.tst'] = 'oczekiwany wynik: usunięto plik, wynik testu: plik wciąż istnieje'
	except FileNotFoundError:
		counter+=1
	try:
		f = open('user4.tst', 'r')
		errorMessages['plik: user4.tst'] = 'oczekiwany wynik: usunięto plik, wynik testu: plik wciąż istnieje'
	except FileNotFoundError:
		counter+=1
	try:
		f = open('user5.tst', 'r')
		errorMessages['plik: user5.tst'] = 'oczekiwany wynik: usunięto plik, wynik testu: plik wciąż istnieje'
	except FileNotFoundError:
		counter+=1

	errorMessages['ilość testów'] = number_of_test
	errorMessages['ilość testów zaliczonych'] = counter

	return errorMessages

