#!/usr/bin/python3
def search_replace(my_list, search, replace):
        list_cpy = my_list.copy()
        for ct in range(len(list_cpy)):
                if search == list_cpy[ct]:
                        list_cpy[ct] = replace
        return list_cpy
