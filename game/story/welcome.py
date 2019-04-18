import game.map as map_model


def show():
    a = [['.', ','], ['.', ',']]
    b = map_model.map(a, "city")
    b.render()
    print('Welcome traveller')
