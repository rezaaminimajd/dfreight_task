from stage.shared import Stage
from setting import Links, BASE_LINKS
from services.utils import request
from lxml import html
from services.textprocess import clean_cities_name, has_numbers
from apps.city import upsert_city
from unidecode import unidecode


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

    @staticmethod
    def __collect_cities(content):
        tree = html.fromstring(content)
        cities_name = clean_cities_name(tree.xpath('/html/body//table//tr/td/a/text()'))
        cities_link = tree.xpath('/html/body//table//tr/td/a/@href')
        for i in range(len(cities_link)):
            if not has_numbers(unidecode(cities_name[i])):
                upsert_city(
                    cities_name[i],
                    cities_link[i]
                )
        return True
