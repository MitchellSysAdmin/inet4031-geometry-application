## Simple Python Code for computing the volume of a Sphere
# 
# This code can be used in two different ways:
# Imported and used by another Python program
# Ran by itself

import math

# Function to calculate the volume of a sphere.
# Formula: Volume = 4/3 * π * r^3
def volume(rad):
    volume = (4/3) * math.pi * rad * rad * rad
    return volume

def surfaceArea():
    pass

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))

    print("\nThe Volume of a CylSphere = ", volume(radius))

if __name__ == '__main__':
    prompt()
