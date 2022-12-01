cities = {
    'zagreb':{
        'country': 'croatia',
        'nationality': 'croatians',
        'religion': 'christians',
        'population': 1_000_000,
    },
    'singapore':{
        'country': 'singapore',
        'nationality': 'multi-ethnic',
        'religion': 'buddhist',
        'population': 5_686_000,
    },
    'zurich':{
        'country': 'switzerland',
        'nationality': 'swiss',
        'religion': 'christian',
        'population': 8_637_000,
    },
}

for city in cities: # ili: for city in cities.keys():
    print(f"{city.title()}")

print ("------")

for city, infos in cities.items():
    print (f"City: {city.title()};")
    for info, value in infos.items():
        print (f"\t{info.title()}: {value}")