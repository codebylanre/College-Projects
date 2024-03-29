"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@mylaurier.ca
Section: CP164 Lab Fall 2023
__updated__ = "Sep 23, 2023"
------------------------------------------------------------------------
"""
from Plant import Plant


def get_plant():
    """
    -------------------------------------------------------
    Creates a plant object by requesting data from a user.
    Use: f = get_plant()
    -------------------------------------------------------
    Returns:
        plant - a completed plant object (Plant).
    -------------------------------------------------------
    """

    name = input("Enter plant name: ")
    specie = input("Enter Plant's specie: ")

    try:
        height = float("Enter plants height: ")
    except ValueError:
        print("Value must be a number")
    moisture_level = input("Enter moisture level")
    # Your code here

    plant = Plant(name, specie, height, moisture_level)

    return plant


def read_plant(line):
    """
    -------------------------------------------------------
    Creates and returns a plant object from a line of string data.
    Use: f = read_plant(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of plant data in the format
          name|species|height|moisture level (str)
    Returns:
        plant - contains the data from line (Plant)
    -------------------------------------------------------
    """

    # Your code here

    # Split the line into individual attributes using | as the delimiter
    attributes = line.split('|')

    if len(attributes) == 4:

        # Extract each plant attributes from the split
        name, species, heightt, moisture_level = attributes

        # convert the height just incase
        try:
            height = float(heightt)
        except ValueError:
            height = 0.0 # setting a default value if height isnt found

        # Creating a new plant object
        plant = Plant(name, species, height, moisture_level)

        return plant
    
    else:
        # Prompting attribute length error
        raise ValueError("Input line should have four attributes")


def read_plants(file_variable):
    """
    -------------------------------------------------------
    Reads a file of plant strings into a list of Plant objects.
    Use: plants = read_plants(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of plant data (file)
    Returns:
        plants - a list of plant objects (list of Plant)
    -------------------------------------------------------
    """

    # Your code here
    
    # Empty list to store Plant objects
    plants = []

    # Loop each line in files
    for line in file_variable:
        # calling previous function to test the code
        plant = read_plant(line.strip())
        plants.append(plant)

    file_variable.close()

    return plants


def write_plants(file_variable, plants):
    """
    -------------------------------------------------------
    Writes a list of plant objects to a file.
    file_variable contains the objects in plants as strings in the format
          name|species|height|moisture level
    plants is unchanged.
    Use: write_plants(file_variable, plants)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of plant data (file)
        plants - a list of Plant objects (list of Plant)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    # LOOP EACH PLANT OBJECT IN THE LIST
    for plant in plants:
        plant_data = f"{plant.name}|{plant.species}|{plant.height}|{plant.moisture_level}\n" 

        file_variable.write(plant_data)

    return


def get_trees(plants):
    """
    -------------------------------------------------------
    Creates a list of tree species.
    plants is unchanged.
    Use: t = get_trees(trees)
    -------------------------------------------------------
    Parameters:
        plants - a list of Plant objects (list of Plants)
    Returns:
        trees - Plant objects from plants that are trees (list of Plant)
    -------------------------------------------------------
    """

    # Your code here

    # return trees


def by_species(plants, species):
    """
    -------------------------------------------------------
    Creates a list of plants by species.
    plants is unchanged.
    Use: v = by_species(plants, species)
    -------------------------------------------------------
    Parameters:
        plants - a list of Plant objects (list of Plant)
        species - a plant origin (int)
    Returns:
        sp_species - Plant objects from plants that are of a particular species (list of Plant)
    -------------------------------------------------------
    """
    assert species in range(len(Plant.SPECIES))


    # Your code here

    # return sp_species


def average_height(plants):
    """
    -------------------------------------------------------
    Determines the average height in a list of plants.
    plants is unchanged.
    Use: avg = average_height(plants)
    -------------------------------------------------------
    Parameters:
        plants - a list of Plant objects (list of Plant)
    Returns:
        avg - average height in all Plant objects of plants (int)
    -------------------------------------------------------
    """

    # Your code here

    # return avg


def height_by_specie(plants, species):
    """
    -------------------------------------------------------
    Determines the average heightcalor in a list of plants.
    plants is unchanged.
    Use: a = height_by_origin(plants, origin)
    -------------------------------------------------------
    Parameters:
        plants - a list of Plant objects (list of Plant)
        origin - the origin of the Plant objects to find (int)
    Returns:
        avg - average height for all Plants of the requested origin (int)
    -------------------------------------------------------
    """
    assert species in range(len(Plant.SPECIES))

    # Your code here

    # return avg



def plant_search(plants, specie, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for plants that fit certain conditions.
    plants is unchanged.
    Use: results = plant_search(plants, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        plants - a list of Plant objects (list of Plant)
        origin - the origin of the plant (int)
        max_height - the maximum height for the plant; if 0, accept any height value (float)
        
    Returns:
        result - a list of plants that fit the conditions (list of Plant)
            plants parameter must be unchanged
    -------------------------------------------------------
    """
    assert specie in range(len(Plant.SPECIES))

    # Your code here

    # return result




if __name__ == "__main__":
    plant_list = [
    Plant("Alderleaf Buckthorn", "Shrub", 3, "Wet"),
    Plant("Bearberry", "Groundcover", 2, "Normal"),
    Plant("Giant Hyssop", "Wildflower", 2, "Dry")
    ]

    # Creating a file for writing
    with open("new_plants.txt", "w+") as fh:
        # calling the function on it
        write_plants(fh, plant_list)
        
