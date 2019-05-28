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

	if(c.encrypt('abc123') == 'YWJjMTIz'):
		counter+=1
	else:
		errorMessages['ciąg znków: abc123'] = 'oczekiwany wynik: YWJjMTIz, wynik testu: ' + c.encrypt('abc123')
	if(c.encrypt('XYZ890') == 'WFlaODkw'):
		counter+=1
	else:
		errorMessages['ciąg znków: XYZ890'] = 'oczekiwany wynik: WFlaODkw, wynik testu: ' + c.encrypt('XYZ890')
	if(c.encrypt('_-[]{}?.,\/`~!') == 'Xy1bXXt9Py4sXC9gfiE='):
		counter+=1
	else:
		errorMessages['ciąg znków: _-[]{}?.,\/`~!'] = 'oczekiwany wynik: Xy1bXXt9Py4sXC9gfiE=, wynik testu: ' + c.encrypt('_-[]{}?.,\/`~!')

	errorMessages['ilość testów'] = number_of_test
	errorMessages['ilość testów zaliczonych'] = counter

	return errorMessages