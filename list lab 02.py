import random

trail_num = 5

made_list = []

for trail_count in range(0, trail_num):
    
    while True:
        random_num = random.randint(1, 5)
        
        found_duplication = False
    
        for made_index in range(0, trail_count):
            if made_list[made_index] == random_num:
                found_duplication = True
                break
            
        if not found_duplication:
            made_list.append(random_num)
            break 
    
print(made_list)

while True:
    input_index = int(input("Index :"))
    
    if 0 <= input_index <= len(made_list):
        print("Element value:",made_list[input_index])
        break
    print("Out of index")