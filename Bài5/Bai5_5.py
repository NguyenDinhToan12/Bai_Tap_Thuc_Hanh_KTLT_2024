n = int(input ("Enter the number of elements: "))
my_list = [int (input (f"Enter element (i+I): ")) for i in range (n)]
max_element = max(my_list)
min_element = min(my_list)
print ("Largest Element:", max_element)
print ("Smallest Element:", min_element)
