class Countries:

    def __init__(self, countries, cities):
        self.cities = {}
        for country, city in zip(countries, cities):
            self.cities[city] = country

    def get_country_by_city(self, city):
        return self.cities.get(city)


if __name__ == '__main__':
    c = Countries(['Albania', 'Albania', 'Georgia', 'USA', 'USA'], ['Tirana', 'Berat', 'Tbilisi', 'Colorado', 'Chicago'])
    find = ['Tblisi', 'Chicago']
    for city in find:
        print(c.get_country_by_city(city))
