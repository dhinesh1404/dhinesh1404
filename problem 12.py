#Current temperature(celsius) is input from the user.
current_temperature = float(input("Enter your current temperature: ")) 

#If the temperature is above 30 degrees "swimming".
if current_temperature >= 30:
    print("current temperature: ", current_temperature)
    print("recommend : swimming")
    
elif 20 <= current_temperature < 30:
    print("current_temperature: ", current_temperature)
    print("recommend : hiking")
    
elif  10 <= current_temperature < 20:
    print("current_temperature", current_temperature)
    print("recommend : riding bicycle")
    
else:
    print("curent_temperature", current_temperature)
    print("recommend : skiing")