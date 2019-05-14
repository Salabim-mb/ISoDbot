import requests
from bs4 import BeautifulSoup


def verifyData(login, password):
	login_url = 'https://isod.ee.pw.edu.pl/isod-stud/signin/?wicket:interface=:0:signInForm::IFormSubmitListener::'
	login_values = {
		'wiaUsername': login,
		'wiaPassword': password
	}
	s = requests.Session()
	s.post(login_url, data=login_values)
	c = s.cookies
	try:
		new_api = s.get(
			'https://isod.ee.pw.edu.pl/isod-stud/person?wicket:interface=:15:person:contApikey:generateApikey::ILinkListener::',
			cookies=c)
		soup = BeautifulSoup((s.get(
			'https://isod.ee.pw.edu.pl/isod-stud/person?wicket:interface=:15:person:contApikey:showApikey::ILinkListener::',
			cookies=c)).text, 'html.parser')
		spans = soup.find_all(attrs={"class": "value"});
		api = spans[len(spans) - 1].text
		return True
	except:
		return False

def getAPI(login, password):
	login_url = 'https://isod.ee.pw.edu.pl/isod-stud/signin/?wicket:interface=:0:signInForm::IFormSubmitListener::'  # adres do logowania na isoda
	login_values = {
		'wiaUsername': login,
		'wiaPassword': password
	}
	s = requests.Session()  # robimy sobie sesje zeby moc zapisywac ciacha
	l = s.post(login_url, data=login_values)  # logujemy sie na isoda
	c = s.cookies
	new_api = s.get(
		'https://isod.ee.pw.edu.pl/isod-stud/person?wicket:interface=:15:person:contApikey:generateApikey::ILinkListener::',
		cookies=c)
	soup = BeautifulSoup((s.get(
		'https://isod.ee.pw.edu.pl/isod-stud/person?wicket:interface=:15:person:contApikey:showApikey::ILinkListener::',
		cookies=c)).text, 'html.parser')
	# tutaj mamy juz ladna stronke  'dane osoby', gdzie mozna znalezc swoje api
	spans = soup.find_all(
		attrs={"class": "value"});  # szukamy po klasie 'values', bo taka klase ma span, ktory zawiera api
	api = spans[len(
		spans) - 1].text  # ciezko mi bylo wyodrebnic samo api, na szczescie jest ostatnim spanem na stronie, wiec z tego korzystamy
	return api


def getPlan(login, password):
	url = 'https://isod.ee.pw.edu.pl/isod-portal/wapi?q=myplan&username=' + login + '&apikey=' + getAPI(
		login, password)  # adres stronki z ktorej mozna wziac indywidualny plan za pomoca api
	p = requests.post(url)
	plan = p.text
	return plan


def getNews(login, password):
	url = 'https://isod.ee.pw.edu.pl/isod-portal/wapi?q=mynewsheaders&username=' + login + '&apikey=' + getAPI(
		login, password)
	n = requests.post(url)
	news = n.text
	return news