def clean_city_name(cities):
    new_cities = []
    for city in cities:
        new_cities.append(city.replace('\u200c', ''))
    return new_cities
