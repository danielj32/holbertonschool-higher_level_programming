#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
        n_list = []
        ct = 0
        for j in range(list_length):
                try:
                        ct = my_list_1[j] / my_list_2[j]
                except IndexError:
                        print("out of range")
                except TypeError:
                        print("wrong type")
                except ZeroDivisionError:
                        print("division by 0")
                finally:
                        n_list.append(ct)
        return n_list
