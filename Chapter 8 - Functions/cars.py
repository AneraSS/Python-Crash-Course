def make_car (company, name, **features):
    features['Company'] = company
    features['Name'] = name
    return features


car = make_car('renault', 'megane', color='black', fog_lights=True)
print(car)