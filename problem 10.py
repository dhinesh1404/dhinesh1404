#Incrementcount function definition:
#Increase the value of the global variable count by 1
def incrementcount():
    global count;
    count = count + 1
    
#Decrementcount function defition:
# - Decrease the value of global variable count by 1
def decrementcount():
    global count;
    count = count - 1
    
#Initialize global variable count to 1
count = 1

incrementcount()
print(count)

decrementcount()
print(count)

incrementcount()
print(count)
incrementcount()
print(count)