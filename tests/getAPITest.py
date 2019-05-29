import os,sys,inspect
import requests
from bs4 import BeautifulSoup
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from Isod import *

#jeśli do poprawnego requesta damy błędny klucz API to wywali stronę z jedną linijką

def run():

	errorMessages = {}

	number_of_test = 5
	counter = 0


	request_url_1 = 'https://isod.ee.pw.edu.pl/isod-portal/wapi?q=mynewsheaders&username=swiderj&apikey=' + getAPI(
		'swiderj', 'afhLNWdi')
	r = requests.post(request_url_1)
	message = r.text
	soup = BeautifulSoup(message, "html.parser")
	check = soup.find(
		text="{\"message\":\"Exception: Podczas wykonywania zapytania wystąpił nieoczekiwany błąd. Skontaktuj się ze wsparciem technicznym i podaj komunikat błędu: Niewłaściwy klucz API.")

	if(check == None):
		counter+=1
	else:
		errorMessages[
			'API dla użytkownika swiderj'] = 'stan faktyczny: Klucz dla tego użytkownika powinien być dostępny, wynik testu: klucz API zwrócony przez metodę jest błędny'

	request_url_2 = 'https://isod.ee.pw.edu.pl/isod-portal/wapi?q=mynewsheaders&username=swiderj&apikey=' + getAPI(
		'polaczej', '6pVev7sf')
	r = requests.post(request_url_2)
	message = r.text
	soup = BeautifulSoup(message, "html.parser")
	check = soup.find(
		text="{\"message\":\"Exception: Podczas wykonywania zapytania wystąpił nieoczekiwany błąd. Skontaktuj się ze wsparciem technicznym i podaj komunikat błędu: Niewłaściwy klucz API.")

	if (check == None):
		counter += 1
	else:
		errorMessages[
			'API dla użytkownika Polaczej'] = 'stan faktyczny: Klucz dla tego użytkownika powinien być dostępny, wynik testu: klucz API zwrócony przez metodę jest błędny'


	request_url_3 = 'https://isod.ee.pw.edu.pl/isod-portal/wapi?q=mynewsheaders&username=swiderj&apikey=' + getAPI(
		'random', 'randrand')
	r = requests.post(request_url_3)
	message = r.text
	soup = BeautifulSoup(message, "html.parser")
	check = soup.find(
		text="{\"message\":\"Exception: Podczas wykonywania zapytania wystąpił nieoczekiwany błąd. Skontaktuj się ze wsparciem technicznym i podaj komunikat błędu: Niewłaściwy klucz API.")

	if (check != None):
		counter += 1
	else:
		errorMessages[
			'API dla użytkownika random'] = 'stan faktyczny: Klucz dla tego użytkownika nie istnieje, wynik testu: klucz API zwrócony przez metodę jest z jakiegoś powodu dobry'

	request_url_4 = 'https://isod.ee.pw.edu.pl/isod-portal/wapi?q=mynewsheaders&username=swiderj&apikey=' + getAPI(
		'boguszj', 'złehasło')
	r = requests.post(request_url_4)
	message = r.text
	soup = BeautifulSoup(message, "html.parser")
	check = soup.find(
		text="{\"message\":\"Exception: Podczas wykonywania zapytania wystąpił nieoczekiwany błąd. Skontaktuj się ze wsparciem technicznym i podaj komunikat błędu: Niewłaściwy klucz API.")

	if (check != None):
		counter += 1
	else:
		errorMessages[
			'API dla użytkownika boguszj z błędnym hasłem'] = 'stan faktyczny: Klucz dla tego użytkownika nie powinien być dostępny, wynik testu: klucz API zwrócony przez metodę jest z jakiegoś powodu dobry'

	request_url_5 = 'https://isod.ee.pw.edu.pl/isod-portal/wapi?q=mynewsheaders&username=swiderj&apikey=' + getAPI(
		'randomx2', 'afhLNWdi')
	r = requests.post(request_url_5)
	message = r.text
	soup = BeautifulSoup(message, "html.parser")
	check = soup.find(
		text="{\"message\":\"Exception: Podczas wykonywania zapytania wystąpił nieoczekiwany błąd. Skontaktuj się ze wsparciem technicznym i podaj komunikat błędu: Niewłaściwy klucz API.")

	if (check != None):
		counter += 1
	else:
		errorMessages[
			'API dla użytkownika randomx2 z dobrym hasłem'] = 'stan faktyczny: Klucz dla tego użytkownika nie powinien być dostępny, wynik testu: klucz API zwrócony przez metodę jest z jakiegoś powodu dobry'



	errorMessages['ilość testów'] = number_of_test
	errorMessages['ilość testów zaliczonych'] = counter

	return errorMessages