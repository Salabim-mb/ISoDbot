import requests
	from bs4 import BeautifulSoup
	
	class Isod:
		def verifyData(login, password):
			login_url = 'https://isod.ee.pw.edu.pl/isod-stud/signin/?wicket:interface=:0:signInForm::IFormSubmitListener::'
			login_values = {
			    'wiaUsername': login,
			    'wiaPassword': password
		    }
			s = requests.Session()
			s.post (login_url, data = login_values)
			c = s.cookies
			try:
				new_api = s.get ('https://isod.ee.pw.edu.pl/isod-stud/person?wicket:interface=:15:person:contApikey:generateApikey::ILinkListener::', cookies = c)
				soup = BeautifulSoup((s.get ('https://isod.ee.pw.edu.pl/isod-stud/person?wicket:interface=:15:person:contApikey:showApikey::ILinkListener::', cookies = c)).text, 'html.parser')
				spans = soup.find_all(attrs={"class" : "value"});
				api = spans[len(spans) - 1].text
				return True
			except:
				return False