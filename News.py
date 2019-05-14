import Isod as Isod, re


class News:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.news_string = Isod.getNews(login, password)
        self.news = []
        self.parse_news()

    class NewsItem:
        def __init__(self, id):
            self.id = id

    def parse_news(self):
        news_string = ''  # robimy stringa ktorego zapelniamy planem
        for index, i in enumerate(self.news_string):  # tutaj robimy tylko troche ladniej
            news_string += i
            # if index - 1 < len(text):
            if (i == '{' or i == '[' or i == ',') and (self.news_string[index + 1] < 'A' or self.news_string[index + 1] > 'z'):
                news_string += "\n"
        plan_array = news_string.split('\n')
        n = 3
        m = 0
        activities = []
        while not re.match(r'.*username.*', plan_array[n]):
            activity = self.NewsItem(m)
            while not re.match(r'(.*)\}', plan_array[n]):
                lin = re.search(r'"(.*)":(.*),', plan_array[n])
                if lin:
                    typ = lin.group(1)
                    val = lin.group(2)
                    val = val[1:-1]
                    setattr(activity, typ, val)
                    n += 1
                else:
                    n += 1
            n += 1
            if (plan_array[n] == '{'):
                n += 1
            activities.append(activity)
            m += 1
        for obj in activities:
            self.news.append(obj)

    def getlastnews(self):  # daje naglowki 5 ostatnich newsow
        self.parse_news()
        list = []
        for i in range(0, 5):
            list.append(self.news[i].subject)
        return list
