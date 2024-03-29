from Plant import Plant  # Assuming you have a Plant class defined in the Plant module

def get_plant():
    """
    Creates a plant object by requesting data from a user.
    
    Returns:
        plant - a completed plant object (Plant).
    """

    # Prompt the user for input data
    name = input("Enter plant name: ")
    species = input("Enter species: ")
    
    # Ensure that height is a valid float
    while True:
        try:
            height = float(input("Enter plant height (in meters): "))
            break  # Exit the loop if a valid float is entered
        except ValueError:
            print("Invalid input. Height must be a numeric value.")

    soil_type = input("Enter soil type: ")

    # Create a Plant object using the collected data
    plant = Plant(name, species, height, soil_type)

    return plant

# Usage example:
if __name__ == "__main__":
    plant = get_plant()
    print(f"Plant created: {plant}")
