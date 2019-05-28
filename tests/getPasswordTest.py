import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Utils import *

def run():

	errorMessages = {}

	number_of_test = 5
	counter = 0

	if(Utils.getPassword('user1.tst') != -1):
		counter+=1
	else:
		errorMessages['plik: user1.tst'] = 'stan faktyczny: plik zawiera hasło, wynik testu: plik nie zawiera hasła'
	if(Utils.getPassword('user2.tst') != -1):
		counter+=1
	else:
		errorMessages['plik: user2.tst'] = 'stan faktyczny: plik zawiera hasło, wynik testu: plik nie zawiera hasła'
	if(Utils.getPassword('user3.tst') == -1):
		counter+=1
	else:
		errorMessages['plik: user3.tst'] = 'stan faktyczny: plik nie zawiera hasło, wynik testu: plik zawiera hasła'
	if(Utils.getPassword('user4.tst') == -1):
		counter+=1
	else:
		errorMessages['plik: user4.tst'] = 'stan faktyczny: plik nie zawiera hasła, wynik testu: plik zawiera hasła'
	if(Utils.getPassword('user5.tst') != -1):
		counter+=1
	else:
		errorMessages['plik: user5.tst'] = 'stan faktyczny: plik zawiera hasło, wynik testu: plik nie zawiera hasła'

	errorMessages['ilość testów'] = number_of_test
	errorMessages['ilość testów zaliczonych'] = counter

	return errorMessages