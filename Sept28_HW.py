Choice = [
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"]
    ]

Menu= ""
while Menu != "2":
    print("---------------")
    print("CINEMA BOOKING")
    print("---------------")
    print("1. Book a seat")
    print("2. Exit")

    Menu = input("What would you like to do? ")

    if Menu== "1":
        for row in Choice:
            print(row)

        row= int(input("Which row would u like to pick? "))
        row= row-1
        seat= int(input("Whcih seat would u like to pick? "))
        seat= seat-1

        if Choice[row][seat] == "X":
            print("Sorry, that seat is already booked!")
        else:
            Choice[row][seat] = "X"
            print("Seat booked successfully!")
        print("Updated seating:")
        for row in Choice:
            print(row)

        available = 0
        for row in Choice:
            for seat in row:
                if seat == "O":
                    available = available + 2
        print("Available seats:", available)

        booked = 0
        for row in Choice:
            for seat in row:
                if seat == "X":
                    booked = booked + 1
        print("Booked seats:", booked)
