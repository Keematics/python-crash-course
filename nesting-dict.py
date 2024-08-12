cities = {
    'Dubai': {
        'population': 1_000_000,
        'continent': 'Asia',
        'fact': 'Serenity and Tourism'
    },
    'Tokyo': {
        'population': 12_000_000,
        'continent': 'Asia',
        'fact': 'Technology'
    },
    'South Africa': {
        'population': 5_000_000,
        'continent': 'Africa',
        'fact': 'Park'
    },
}

for city_name, city_info in cities.items():
    print(city_name.title(), f"in {city_info['continent']} has {city_info['population']} population")
    print(f"She is known for her {city_info['fact']}")
    print('------------')
    