

def homesize():
    """
    calculates a home's square footage 
    by adding together the square footage of every user-inputted room
    """
    floorplan_list = []
    data_input = True 
    print("\nWelcome to Home-Size, where we will size your home! ")
    while data_input == True: 
        room_name = input("\nWhat room is you talking about? ")
        room_length = input(f"What is the length in ft of {room_name}? ")
        room_width = input(f"What is the width in ft of {room_name}? ")
        room_area = int(room_width) *int(room_length)

        room = {"Room Name" : room_name,
                "Room Length" : room_length,
                "Room Width" : room_width, 
                "Room Area" : room_area 
                }
        floorplan_list.append(room)
       
        keepgoing = input("Any more rooms? y/n ")

       
        if keepgoing.lower() == "n":
            data_input = False 
            break 

    total_area = []
    print("\nThank you for your input. Summarizing: ")
    for x in floorplan_list:
        total_area.append(int(x["Room Area"]))
        print(f"\nRoom: {x['Room Name']} \n\tRoom length: {x['Room Length']} ft\n\tRoom width: {x['Room Width']} ft")


    print("\nThe total square footage of your home is " + str(sum(total_area)) + " SqFt.")
    if sum(total_area) < 500: 
        print("Seems cozy! ")
    elif sum(total_area) >= 500 and sum(total_area) <= 3000:
        print("That's a pretty decent size! ")
    elif sum(total_area) > 3000:
        print("Woah there, call MTV Cribs! ")

def circle():
    """
    calculates the circumference of a circle from user input.
    C=2πr
    """
    import math 
    print("\nCalculating the circumference of a circle: ")
    radius = input("\nWhat is the radius (in inches) of your circle? ")
    radius = int(radius)
    circumference = round((2 * math.pi * radius),2)
    print(f"\nThe circumference of your circle is {circumference} inches. ")
    
