def advance_reservation (age, event_code, reservation_date):
    if (event_code in ['E1','E2','E3'] and 1 <= reservation_date <= 30):
        print("Invalid input. terminating program.")
        
    if event_code == 'E1':
        if age < 18:
            print("You reservation cannot be made due to age restrictions.")
        else:
            print("Your reservation is complete.")
            
    elif event_code == 'E2':
        if reservation_date is 2 != 0:
            print("No reservations are available on the dates you selected.")
        else:
            print("Your reservation is complete.")
            
    elif event_code == 'E3':
        if age < 16 or reservation_date is 7 !=0:
            print("Your reservation cannot be made due to age restrictions.")
        else:
            print("Your reservation is complete.")
            
age = int(input("Please enter your age: "))
event_code = input("Enter the event code:")
reservation_date = int(input("Enter the reservation date (1 to 30): "))
advance_reservation (age, event_code, reservation_date)