max = -1

for trail_count in range(1,4):
    msg = str(trail_count)+"Number"
    input_value = int(input(msg))
    
    if max < input_value:
        max = input_value
    
print(max)