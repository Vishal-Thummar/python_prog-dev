seat_type = input("Enter your Seat type (Slepper/AC/General/luxury) : " ).lower()
match seat_type:
    case "slepper":
        print("Sleeper No AC. beds availabel" )
    case "ac":
        print("AC beds availabel")
    case "general":
        print("Genral Chepest Option , no reservation required")
    case "luxury":
        print("Luxury beds availabel")
    case _:
        print("Invalid Seat Type")