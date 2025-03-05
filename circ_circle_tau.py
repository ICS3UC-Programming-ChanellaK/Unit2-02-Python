#!/usr/bin/env python3
# created by :chanella
# created on:May 3rd,2025
# This program asks the user for the radius of
# a circle i mm.It then calculates and displays
# the circumference using tau
# import the TAU constant from the constants.py
import constants


def main():
    # get the radius from the user
    radius = float(input("Enter the radius of the circle(mm):"))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print("circumference={} mm".format(circumference))


if __name__ == "__main__":
    main()
