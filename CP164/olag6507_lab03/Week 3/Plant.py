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

import string
class Plant:
    
    #constant
    SPECIES = ("Shrub", "Wildflower", "Vine", "Tree", "Fern", "Groundcover")

    @staticmethod
    def species(self, SPECIES):
        """
        -------------------------------------------------------
        Creates a string list of plant type in the format:
            0 Shrub
            1 Wildflower
            2 Vine
            ...
        Use: s = Plant.species()
        Use: print(Plant.species())
        -------------------------------------------------------
        Returns:
            string - A numbered list of valid plant types (str)
        -------------------------------------------------------
        """

        # your code here
        string = ""
        for index, i in enumerate(Plant.SPECIES):
            string += "{index}, {i}" "\n"

        return string
    
        # ALTERNATIVE METHOD WHICH WORK FINE ALSO
        # species_list = "\n".join(f"{i} {type}" for i, type in enumerate(Plant.SPECIES))
        # return species_list
 
        
    
    def __init__(self,name,specie,height,moisture_level):
        """
        -------------------------------------------------------
        Initialize a plant object.
        Use: f = Plant( name, specie,height,moisture_level )
        -------------------------------------------------------
        Parameters:
            name - plant name (str)
            specie - plant species (int)
            height - plant height (int)
            moisture_level - moisture requirement (str)
        Returns:
            A new Plant object (Plant)
        -------------------------------------------------------
        """
        # assert specie in range(len(Plant.SPECIES)), "Invalid species ID"
        assert specie in (Plant.SPECIES), "Invalid species ID"
        assert height is height >= 0, "height must be >= 0"
        
        self.name=name
        self.species = specie
        self.height= height
        self.moisture_level= moisture_level

        return

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of plant data.
        Use: print(f)
        Use: s = str(f)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of plant (str)
        -------------------------------------------------------
        """

        # your code here

        return f"""
        Name: {self.name}
        Specie: {self.species}
        Height: {self.height}
        Moisture: {self.moisture_level}
        """

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares this plant against another plant for equality.
        Use: f == target
        -------------------------------------------------------
        Parameters:
            target - [right side] plant to compare to (plant)
        Returns:
            result - True if name and specie match, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.name.lower(), self.specie) == (
            target.name.lower(), target.specie)
        return result

    def __lt__(self, target):
        """
        -------------------------------------------------------
        Determines if this plant comes before another.
        Use: f < target
        -------------------------------------------------------
        Parameters:
            target - plant to compare to (plant)
        Returns:
            result - True if plant precedes target, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.name.lower(), self.specie) < \
            (target.name.lower(), target.specie)
        return result

    def __le__(self, target):
        """
        -------------------------------------------------------
        Determines if this plant precedes or is or equal to another.
        Use: f <= target
        -------------------------------------------------------
        Parameters:
            target - [right side] Plant to compare to (Plant)
        Returns:
            result - True if this plant precedes or is equal to target,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        result = self < target or self == target
        return result

    def write(self, file_variable):
        """
        -------------------------------------------------------
        Writes a single line of plant data to an open file.
        Use: f.write(file_variable)
        -------------------------------------------------------
        Parameters:
            file_variable - an open file of plant data (file)
        Returns:
            The contents of plant are written as a string in the format
              name|specie|height to file_variable.
        -------------------------------------------------------
        """
        print("{}|{}|{}|{}"
              .format(self.name, self.specie, self.height, self.moisture_level),
              file=file_variable)
        return
    