rivers = {
    'Egypt': 'Nile',
    'Croatia': 'Sava',
    'Italy': 'Pad',
    'China': 'Yangtze',
    'Austria':'Danube',
}
for country, river in sorted(rivers.items()):
    print (f"{river.title()} flows through {country.title()}.")