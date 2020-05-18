#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
        n_list = []
        ct = 0
        for j in range(list_length):
                try:
                        ct = my_list_1[j] / my_list_2[j]
                except ZeroDivisionError:
                        print("division by 0")
                except TypeError:
                        print("wrong type")
                except IndexError:
                        print("out of range")
                finally:
                        n_list.append(ct)
        return n_list
