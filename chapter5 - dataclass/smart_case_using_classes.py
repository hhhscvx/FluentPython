from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class City:
    continent: set
    name: str
    country: str


cities = [
    City('Asia', 'Tokyo', 'JP'),
    City('Asia', 'Delhi', 'IN'),
    City('North America', 'Mexico', 'MX'),
    City('North America', 'New York', 'US'),
    City('South America', 'Sao Paulo', 'BR'),
]


def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia', country=country):
                results.append(country)  # country присвоили в переменную - гениально
    return results
