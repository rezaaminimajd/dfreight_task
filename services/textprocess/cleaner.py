from khoshnevis import normalizer

Normalizer = normalizer()


def clean_cities_name(cities):
    new_cities = []
    for city in cities:
        new_cities.append(clean_city_name(city))
    return new_cities


def clean_city_name(city):
    city = city.replace('\u200c', '')
    return Normalizer.normalize(
        text=city,
        zwnj="\u200c",
        tokenized=False,
        clean_url=False,
        extra_clean=True,
        remove_emoji=False
    )


def has_numbers(string):
    return any(char.isdigit() for char in string)
