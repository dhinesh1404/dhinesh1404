bar = [value for value in range(10,20)]
#[10,11,12,13,14,15,16,17,18,19]

#slicing
#Reference variable[start : stop : step]
#start : 0 -> stop : 4 - 1 
foo = bar[0 : 4 :  1]

print("foo: ", foo)
print("bar: ", bar)

bar = [2, 3, 4, 5, 6]

foo = bar[-1: -6: -1] #

print(foo)

bar = [2, 3, 4, 5, 6]
bar[1] = 20
#After : [2, 20, 4, 5, 6]

bar[0 : 3] = [100, 200, 300]

print(bar)





bar = [100, 200, 300, 400, 500, 600, 700]

#CRUD:delete
#Delete element: Delete one element, delete all elements in the list
#Delete one element: three methods
#Delete the element at the corresponding index using the del command 
#Use the remon=ve function to delete the element using the value
#using the pop function,delete the element of the corresponding index an return the delete value

#bar = [] 
