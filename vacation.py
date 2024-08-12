vacation_places = {}
active = True
while active:
    name = input("What's your name dear? ")
    place = input("Where would you like to visit? ")
    
    vacation_places[name] = place
    
    confirm = input("Do you want another person to respond? yes/no ")
    if confirm.lower() == 'no':
        active = False

print("Here's the vacation responses")
print("------------")
for key, value in vacation_places.items():
    print(f"{key} would like to visit {value}")