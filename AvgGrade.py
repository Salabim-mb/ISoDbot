from lxml import html
import requests

class AvgGrade:
    def __init__(self, login, password):
        self.login = login
        self.password = password




    def getAvgGrade(self):
        s = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

        # payload
        payload = {
            "wiaUsername": self.login,
            "wiaPassword": self.password
        }
        # perform login
        result = s.post('https://isod.ee.pw.edu.pl/isod-stud/signin?wicket:interface=:0:signInForm::IFormSubmitListener::', params=payload, headers=headers)

        result = s.get('https://isod.ee.pw.edu.pl/isod-stud/semesterlist?wicket:interface=:16:crumbs:levels:1:level::ILinkListener::', headers=headers)
        tree = html.fromstring(result.content)
        elements = tree.xpath('//span[@class="value"]')
        avgGrade = elements[9]
        return avgGrade