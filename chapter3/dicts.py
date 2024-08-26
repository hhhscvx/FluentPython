from pprint import pprint


dial_codes = [(880, 'Bangladesh'),
              (55, 'Brazil'),
              (86, 'China'),
              (91, 'India'),
              (62, 'Indonesia'),
              (81, 'Japan'),
              (234, 'Nigeria'),
              (92, 'Pakistan'),
              (7, 'Russia'),
              (1, 'United States'),
              ]

country_dial = {country: code for code, country in dial_codes}

pprint(country_dial)

imba = {code: country.upper() for country, code in sorted(country_dial.items()) if code >= 70}
print()
pprint(imba)
