#!/usr/bin/python3

from sys import argv
from os.path import exists
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filenama = "add_item.json"
py_list = []

# Check if the file exists, load its content if it does
if exists(filename):
    py_list = load_from_json_file(filename)
else:
    # Add command line arguments to the list
    py_list.extend(argv[1:])

# Save the updated list to the file
save_to_json_file(py_list, filename)
