from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from stage.shared import Stage
from services.utils import request
from setting import Links, BASE_LINKS
from apps.city import get_all_city


class NlpNer(Stage):

    def __init__(self, *args, **kwargs):
        self.link = BASE_LINKS[Links.NLP_PRE_TRAINED_MODEL.value]
        tokenizer = AutoTokenizer.from_pretrained(self.link)
        model = AutoModelForTokenClassification.from_pretrained(self.link)
        self.nlp = pipeline("ner", model=model, tokenizer=tokenizer)
        super().__init__(*args, **kwargs)

    def run(self) -> bool:
        cities = get_all_city()
        for index, city in enumerate(cities):
            response = request(
                method='GET',
                url=BASE_LINKS[Links.BASE_WIKI.value] + city.page_url
            )
            tokens = self.nlp(response.content)
        return True

# todo Failed
