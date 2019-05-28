import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Ciphrator import *

def run():

	errorMessages = {}

	number_of_test = 3
	counter = 0

	c = Ciphrator()

	if(c.decrypt('YWJjMTIz') == 'abc123'):
		counter+=1
	else:
		errorMessages['ciąg znków: YWJjMTIz'] = 'oczekiwany wynik: abc123, wynik testu: ' + c.decrypt('YWJjMTIz')
	if(c.decrypt('WFlaODkw') == 'XYZ890'):
		counter+=1
	else:
		errorMessages['ciąg znków: WFlaODkw'] = 'oczekiwany wynik: XYZ890, wynik testu: ' + c.decrypt('WFlaODkw')
	if(c.decrypt('Xy1bXXt9Py4sXC9gfiE=') == '_-[]{}?.,\/`~!'):
		counter+=1
	else:
		errorMessages['ciąg znków: Xy1bXXt9Py4sXC9gfiE='] = 'oczekiwany wynik: _-[]{}?.,\/`~!, wynik testu: ' + c.decrypt('Xy1bXXt9Py4sXC9gfiE=')

	errorMessages['ilość testów'] = number_of_test
	errorMessages['ilość testów zaliczonych'] = counter

	return errorMessages