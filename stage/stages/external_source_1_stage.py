from stage.shared import Stage
from setting import Links, BASE_LINKS
from services.utils import request
from services.textprocess import clean_city_name
from lxml import html
from apps.city import add_old_city


class ExternalSource1(Stage):

    def __init__(self, *args, **kwargs):
        self.link = BASE_LINKS[Links.ES1_PAGE_LINK.value]
        super().__init__(*args, **kwargs)

    def run(self) -> bool:
        response = request(
            method='GET',
            url=self.link
        )
        return self.__collect_old_cities(response.content)

    @staticmethod
    def __collect_old_cities(content):
        tree = html.fromstring(content)
        cities_name = tree.xpath('/html/body//div[@class="entry-content"]/p/text()')[2:]
        for city_name in cities_name:
            city_names = str(city_name).strip().split(':')
            city_name = city_names[0].strip()
            old_city_name = city_names[1].strip()
            if city_name and old_city_name:
                add_old_city(clean_city_name(old_city_name), clean_city_name(city_name))
        return True
