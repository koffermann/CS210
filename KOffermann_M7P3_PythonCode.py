# CS210 - Project Three
# Name: Kerrian Offermann
# Date: 10/13/2021

import re
import string
import os

# These codes will help Python to find the correct location of the input file
working_directory = os.getcwd() 
file_path = working_directory + 'inputfile.txt'

def QuantityAll(): # The function used to populate items list with quantity
    count = 0    # The count begins and is initialized at 0

    itemList = open('inputfile.txt', 'r') # Opens the text file with the items sold today listed
    
    itemDict = dict() # Create a dictionary that will later store the item names and the values (quantity) associated with them
  
    for line in itemList: # This For Loop will go through each line 
        line = line.strip()  # Each line pulled will have any excess spaces or newlines stripped
        line = line.lower() # To make reading items easier, every line will be set to lowercase to avoid any case-related problems
        items = line.split(" ") # Each line will be split into its own word -- assigned with the variable "items"
  
        for item in items: # This For Loop will go through each word in the line  
            if item in itemDict: # If the item is already in the dictionary then add 1 to the item's quantity
                itemDict[item] = itemDict[item] + 1
            else: # Otherwise, add item to the dictionary and add a quantity of one for this one item
                itemDict[item] = 1
  
    for key in list(itemDict.keys()): # This For Loop will go through each item in the dictionary and print with its count/quantity
        print(key, ":", itemDict[key])

    itemList.close() # The text file must be closed now that it is done being used


# ------------------------------------------------------------------------------------------------------------------------


def QuantityOne(): # The function used to print the item and quantity requested by user
    itemList = open('inputfile.txt', 'r') # Opens the text file with the items sold today listed
    
    itemDict = dict() # Create a dictionary that will later store the item names and the values (quantity) associated with them
    


  
    for line in itemList: # This For Loop will go through each line 
        line = line.strip()  # Each line pulled will have any excess spaces or newlines stripped
        line = line.lower() # To make reading items easier, every line will be set to lowercase to avoid any case-related problems
        items = line.split(" ") # Each line will be split into its own word -- assigned with the variable "items"

        for item in items: # This For Loop will go through each word in the line  
            if item in itemDict: # If the item is already in the dictionary then add 1 to the item's quantity
                itemDict[item] = itemDict[item] + 1
            else: # Otherwise, add item to the dictionary and add a quantity of one for this one item
                itemDict[item] = 1

    for item in itemDict:
        print("Please enter the item you would like to search:")

        itemInput = input()
        itemInput = itemInput.lower() # Lowers the case of all input so search will be accurate

        if itemInput in itemDict: # If the user's input is in the dictionary of items and quantities...
            print("Your results:", itemDict[itemInput], itemInput, "(s) sold.") #... Print "Your results: # itemInput sold"
            break
        else: # If user enters a nonexistent item then this prompt will print
            print("Your item could not be found. Please check for entry error or try a new item.")
            continue

    itemList.close() # The text file must be closed now that it is done being used
  
    return 0;

# --------------------------------------------------------------------------------------------------------------------------------


def QuantityGraph(): # Th
    itemList = open('inputfile.txt', 'r') # Opens the text file with the items sold today listed
    
    itemDict = dict() # Create a dictionary that will later store the item names and the values (quantity) associated with them
  
    for line in itemList: # This For Loop will go through each line 
        line = line.strip()  # Each line pulled will have any excess spaces or newlines stripped
        line = line.lower() # To make reading items easier, every line will be set to lowercase to avoid any case-related problems
        items = line.split(" ") # Each line will be split into its own word -- assigned with the variable "items"

        for item in items: # This For Loop will go through each word in the line  
            if item in itemDict: # If the item is already in the dictionary then add 1 to the item's quantity
                itemDict[item] = itemDict[item] + 1
            else: # Otherwise, add item to the dictionary and add a quantity of one for this one item
                itemDict[item] = 1

    itemGraph = open("frequency.dat", "w") # The loop will create a frequency.dat file) 
    
    for key in list(itemDict.keys()): # This For Loop will repeat for every item in the dictionary
        print(key, itemDict[key]*'*', file=itemGraph) # In the file, it will write item's name with an asterisk for each item sold

    print("Graph saved as frequency.dat file.")

    for key in list(itemDict.keys()): # This For Loop will go through each item in the dictionary and print with its count/quantity
        print(key, itemDict[key]*'*') # Count will be converted into asterisks
                   
    itemGraph.close()
         
    return 0;