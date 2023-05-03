"""
This module contains the function get_new_rail

    Parameters:
        None

    Returns:
        rail (string): Type of rail system in the city
"""

def get_new_rail():
    """
    Function to get the metro system of a city from the user
    and validate it
    """
    
    while True:
        rail = input('Enter the type of metro system  of the city.\
                     \nIf unknown, enter "Unknown": ')

        if not rail.isalpha():
            print('Invalid input: Rail type must be alpha characters.')
        else:
            break
        

    return rail
