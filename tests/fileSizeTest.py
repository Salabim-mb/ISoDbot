import os,sys,inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from Registration import *



def run():
	errorMessages = {}
	number_of_test = 5
	counter = 0
	
	if Registration.fileSize('anonek.tst') == 1:
		errorMessages['anonek'] = 'test: podano tylko login'
	elif Registration.fileSize('anonek.tst') == 2:
		errorMessages['anonek'] = 'test: podano login i hasło'
	else:
		errorMessages['anonek'] = 'test: za dużo linijek w pliku'
	else:
		errorMessages['anonek'] = 'test: plik nie istnieje'
		counter += 1
		
	if Registration.fileSize('balasm.tst') == 1:
		errorMessages['balasm'] = 'test: podano tylko login'
	elif Registration.fileSize('balasm.tst') == 2:
		errorMessages['balasm'] = 'test: podano login i hasło'
		counter += 1
	else:
		errorMessages['balasm'] = 'test: za dużo linijek w pliku'
	else:
		errorMessages['balasm'] = 'test: plik nie istnieje'
		
	if Registration.fileSize('boguszj.tst') == 1:
		errorMessages['boguszj'] = 'test: podano tylko login'
	elif Registration.fileSize('boguszj.tst') == 2:
		errorMessages['boguszj'] = 'test: podano login i hasło'
		counter += 1
	else:
		errorMessages['boguszj'] = 'test: za dużo linijek w pliku'
	else:
		errorMessages['boguszj'] = 'test: plik nie istnieje'
		
	if Registration.fileSize('polaczej.tst') == 1:
		errorMessages['polaczej'] = 'test: podano tylko login'
	elif Registration.fileSize('polaczej.tst') == 2:
		errorMessages['polaczej'] = 'test: podano login i hasło'
		counter += 1
	else:
		errorMessages['polaczej'] = 'test: za dużo linijek w pliku'
	else:
		errorMessages['polaczej'] = 'test: plik nie istnieje'
		
	if Registration.fileSize('ktokolwiek.tst') == 1:
		errorMessages['ktokolwiek'] = 'test: podano tylko login'
	elif Registration.fileSize('ktokolwiek.tst') == 2:
		errorMessages['ktokolwiek'] = 'test: podano login i hasło'
	else:
		errorMessages['ktokolwiek'] = 'test: za dużo linijek w pliku'
	else:
		errorMessages['ktokolwiek'] = 'test: plik nie istnieje'
		counter += 1
		
	errorMessages['ilość testów'] = number_of_test
	errorMessages['ilość testów zaliczonych'] = counter

	return errorMessages
	