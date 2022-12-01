#imamo igricu, i u igrici postoje objekti (svemirski brod i meteori)
#svaki od njih ima svoju poziciju u 2D prostoru (smjer kretanja i brzinu)
#napisi simulaciju kako se igrica razvija iz sekunde u sekundu
#for petlja za vremenski period N kako se događaju promjene

print ("-- OPCIJA 1 --")

entities = {
    'shuttle': {
        'x': 3,
        'y': 2,
        'dx':0,
        'dy':1,
    },
    'meteor_1': {
        'x': 3,
        'y': 4,
        'dx': 0,
        'dy': -1,
    },
    'meteor_2': {
        'x': 6,
        'y': 0,
        'dx': 1,
        'dy': -4,
    }
}

#primjer ispisa:
# t=0:
#   shuttle: (2,3)
#   meteor_1: (3,4)
#   metor_2: (5,8)
# t=1
#   shuttle: (4,2)
#   meteor_1: (7,6)
#   metor_2: (6,4)

t_0=0
t_max=5

for t in range(t_0,t_max+1):
    print (f"\n t = {t}:")
    for entity_name, coords in entities.items():
        print (f"\t{entity_name}: ({coords['x']}, {coords['y']})")
        coords['x']=coords['x']+coords['dx']
        coords['y'] = coords['y'] + coords['dy']

#ako imaju meteor i shuttle istu kordinatu, ispisi game over (jos ne znamo prekinuti igru zbog while)
        #
        # if entities['shuttle']['x'] == entities['meteor_1']['x'] or \
        #         entities['shuttle']['x'] == entities['meteor_2']['x']:
        #     print ("BOOM!")

    # ovo radi za proizvoljnu kolicinu meteora
    # for entity_name in entities.keys():
    #     if entity_name != 'shuttle':
    #         pozicija_meteora = entities[entity_name]['x']
    #         pozicija_shuttle = entities['shuttle']['x']
    #         if pozicija_meteora == pozicija_shuttle:
    #             print ("BOOM!")
    #
    # promjeni komad koda da odmah u for-petlji vadis vrijednosti, a ne da pristupas preko kljuca

    # ili entities2 = entities.copy()
    # .copy() - iteration error solution (adding new entity to dictionary)

    for entity_name, coords in entities.copy().items(): #ili entities2.items()
        if entity_name != 'shuttle':
            pozicija_meteora_x = coords['x'] #ovo se mijenja po entitiima
            pozicija_shuttle_x = entities['shuttle']['x'] # specificno za tu fiksnu
            pozicija_meteora_y = coords['y'] #ovo se mijenja po entitiima
            pozicija_shuttle_y = entities['shuttle']['y'] # specificno za tu fiksnu
            if pozicija_meteora_x == pozicija_shuttle_x and pozicija_meteora_y == pozicija_shuttle_y:
                print ("BOOM!")

# kad se sudare pojavi se novi meteor

                meteor_number= len(entities.keys())
                #meteor_name = 'meteor' + '_' + meteor_number
                meteor_name = f"meteor_{meteor_number}"
                entities[meteor_name] = {
                    'x': pozicija_meteora_x,
                    'y': pozicija_meteora_y,
                    'dx': 3,
                    'dy': 7,
                    }

print ("\n")
print (entities.items())