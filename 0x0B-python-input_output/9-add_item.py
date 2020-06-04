#!/usr/bin/python3
""" adds all arguments to a Python list  """
import json
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        lista_json = load_from_json_file('add_item.json')
    except FileNotFoundError:
        lista_json = []

    for j in range(1, len(sys.argv)):
        lista_json.append(sys.argv[j])
    save_to_json_file(lista_json, "add_item.json")
