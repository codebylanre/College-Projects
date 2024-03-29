from Plant import Plant
from ArrayStack import ArrayStack



def update_plant_height(plantstack):

    new_height = ArrayStack()
    while not plantstack.isEmpty():
        content = plantstack.pop()

        content += 2
        new_height.push(content)
    return new_height


def test():
    plantstack = ArrayStack()
    plantheight = [10, 20, 30, 40]

    for plant in plantheight:
        plantstack.push(plant)


    result = update_plant_height(plantstack)
    while not result.isEmpty():
        content = result.pop()
        print(content)




