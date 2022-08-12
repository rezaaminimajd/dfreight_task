from shared import Stage
from setting import Links, BASE_LINKS
from services.utils import request
from lxml import html
from services.textprocess import clean_city_name
from apps.city import add_city

from services.database import engine
from apps.city.models import Base

Base.metadata.create_all(bind=engine)


class InitialStage(Stage):

    def __init__(self, *args, **kwargs):
        self.link = BASE_LINKS[Links.INITIAL_PAGE_LINK.value]
        super().__init__(*args, **kwargs)

    def run(self) -> bool:
        response = request(
            method='GET',
            url=self.link
        )
        return self.__collect_cities(response.content)

    def __collect_cities(self, content):
        tree = html.fromstring(content)
        cities_name = clean_city_name(tree.xpath('/html/body//table//tr/td[1]/a/text()'))
        cities_link = tree.xpath('/html/body//table//tr/td[1]/a/@href')
        for i in range(len(cities_link)):
            add_city(
                self.step,
                cities_name[i],
                cities_link[i]
            )
        return True
