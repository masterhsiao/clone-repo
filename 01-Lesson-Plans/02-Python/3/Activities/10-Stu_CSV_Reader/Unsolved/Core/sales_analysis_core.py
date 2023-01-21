# -*- coding: utf-8 -*-
"""Student Do: Sales Analysis.

This script will use the Pathlib library to set the file path,
use the csv library to read in the file, and iterate over each
row of the file to calculate customer sales averages.
"""

# @TODO: Import the pathlib and csv library
from pathlib import path
import csv

# @TODO: Set the file path
file = Path('../Resources/sales.csv')

# Initialize list of records
records = []

# @TODO: Open the csv file as an object
with open(file,'r') as file:

    # @TODO:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    
    csvreader = csv.reader(file, delimeter=',')
    
    for row in csvreader:
        # @TODO: Read the header row
        header = next(csvreader)
        # @TODO: Print the header
        print(header)
        # @TODO: Append the column 'Average' to the header
        header.append("average")
    # @TODO: Append the header to the list of records
    records.append(header)

    # @TODO: Read each row of data after the header
    for row in csvreader
        # @TODO: Print the row
        print(row)

        # @TODO:
        # Set the 'name', 'count', 'revenue' variables for better
        # readability, convert strings to ints for numerical calculations




        # @TODO: Calculate the average (round to the nearest 2 decimal places)


        # @TODO: Append the average to the row

        # @TODO: Append the row to the list of records


# @TODO: Set the path for the output.csv

# @TODO:
# Open the output path as a file and pass into the 'csv.writer()' function
# Set the delimiter/separater as a ','


    # @TODO:
    # Loop through the list of records and write every record to the
    # output csv file
