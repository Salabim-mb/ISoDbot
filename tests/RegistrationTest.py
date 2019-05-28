import os,sys,inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import Registration



def run():
	errorMessages = {}
	number_of_test = 5
	counter = 0
	
	
	if Registration.registered('anonek') == False
		counter += 1
	elif Registration.registered('anonek') == 1
		errorMessages['anonek'] = 'test: podany tylko login, stan faktyczny: niezarejestrowany'
	elif Registration.registered('anonek') == 2
		errorMessages['anonek'] = 'test: login+hasło bez weryfikacji, stan faktyczny: niezarejestrowany'
	else:
		errorMessages['anonek'] = 'test: zarejestrowany i zweryfikowany, stan faktyczny: niezarejestrowany'
		
		
	if Registration.registered('balasm') == False
		errorMessages['balasm'] = 'test: niezarejestrowany, stan faktyczny: zweryfikowany'
	elif Registration.registered('balasm') == 1
		errorMessages['balasm'] = 'test: podany tylko login, stan faktyczny: zweryfikowany'
	elif Registration.registered('balasm') == 2
		errorMessages['balasm'] = 'test: login+hasło bez weryfikacji, stan faktyczny: zweryfikowany'
	else:
		counter += 1
		
		
	if Registration.registered('boguszj') == False
		errorMessages['boguszj'] = 'test: niezarejestrowany, stan faktyczny: zweryfikowany'
	elif Registration.registered('boguszj') == 1
		errorMessages['boguszj'] = 'test: podany tylko login, stan faktyczny: niezarejestrowany'
	elif Registration.registered('boguszj') == 2
		errorMessages['boguszj'] = 'test: login+hasło bez weryfikacji, stan faktyczny: zweryfikowany'
	else:
		counter += 1
		
	
	if Registration.registered('polaczej') == False
		errorMessages['polaczej'] = 'test: niezarejestrowany, stan faktyczny: zweryfikowany'
	elif Registration.registered('polaczej') == 1
		errorMessages['polaczej'] = 'test: podany tylko login, stan faktyczny: niezarejestrowany'
	elif Registration.registered('polaczej') == 2
		errorMessages['polaczej'] = 'test: login+hasło bez weryfikacji, stan faktyczny: zweryfikowany'
	else:
		counter += 1
	
	
	if Registration.registered('ktokolwiek') == False
		counter += 1
	elif Registration.registered('ktokolwiek') == 1
		errorMessages['ktokolwiek'] = 'test: podany tylko login, stan faktyczny: niezarejestrowany'
	elif Registration.registered('ktokolwiek') == 2
		errorMessages['ktokolwiek'] = 'test: login+hasło bez weryfikacji, stan faktyczny: niezarejestrowany'
	else:
		errorMessages['ktokolwiek'] = 'test: zarejestrowany i zweryfikowany, stan faktyczny: niezarejestrowany'
		
		
	errorMessages['ilość testów'] = number_of_test
    errorMessages['ilość testów zaliczonych'] = counter

    return errorMessages
	
print(run())