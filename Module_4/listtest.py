tuple_old = ('Python II', 'Hao Zhang', 'Data Analytics', 'Cheryl Aasheim', 'IT issues', 'Jeff Kaleta')
print("The old tuple is: " + str(tuple_old))


list_tuple = list(tuple_old)
print("\nlist_tuple: " + str(list_tuple))
list_tuple[2] = 'Network Security'
list_tuple[3] = 'Lei Chen'

tuple_updated = tuple(list_tuple)
#tuple_updated = tuple_old[:2] + ('Network Security', 'Lei Chen') + tuple_old[4:]
print("\nThe updated tuple is: " + str(tuple_updated))

tuple_of_ints = (2, 3, 4, 5, 6)
print("tuple_of_ints[1]: " + str(type(tuple_of_ints[1])))
list_ints = list(tuple_of_ints)
list_ints[0] = 1
tuple_new = tuple(list_ints)
print("\ntuple_of_ints: " + str(list_ints))
