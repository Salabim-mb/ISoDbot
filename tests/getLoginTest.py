import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Utils import *

def run():

	errorMessages = {}

	number_of_test = 5
	counter = 0

	if(Utils.getLogin('user1.tst') != -1):
		counter+=1
	else:
		errorMessages['plik: user1.tst'] = 'stan faktyczny: plik zawiera login, wynik testu: plik nie zawiera loginu'
	if(Utils.getLogin('user2.tst') != -1):
		counter+=1
	else:
		errorMessages['plik: user2.tst'] = 'stan faktyczny: plik zawiera login, wynik testu: plik nie zawiera loginu'
	if(Utils.getLogin('user3.tst') != -1):
		counter+=1
	else:
		errorMessages['plik: user3.tst'] = 'stan faktyczny: plik zawiera login, wynik testu: plik nie zawiera loginu'
	if(Utils.getLogin('user4.tst') == -1):
		counter+=1
	else:
		errorMessages['plik: user4.tst'] = 'stan faktyczny: plik nie zawiera loginu, wynik testu: plik zawiera loginu'
	if(Utils.getLogin('user5.tst') != -1):
		counter+=1
	else:
		errorMessages['plik: user5.tst'] = 'stan faktyczny: plik zawiera login, wynik testu: plik nie zawiera loginu'

	errorMessages['ilosc testow'] = number_of_test
	errorMessages['ilosc testow zaliczonych'] = counter

	return errorMessages