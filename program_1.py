# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):    
    miles = 0.0
    ######################
     """
    Converts kilometers to miles.
    
    Parameters:
        kilometers (float): distance in kilometers
        
    Returns:
        float: distance in miles
    """
    miles = kilometers * 0.6214
    return miles


def main():
    print("=== Kilometer to Mile Converter ===")
    
    try:
        kilometers = float(input("Enter distance in kilometers: "))
        
        if kilometers < 0:
            print("Distance cannot be negative.")
        else:
            miles = kilometers_to_miles(kilometers)
            print(f"{kilometers:.2f} kilometers is equal to {miles:.2f} miles.")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


# Program execution starts here
if __name__ == "__main__":
    main()


    # Return the variable to the calling function
    return miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    # Get User Input
    print('in main')
    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    
    # Display the miles
