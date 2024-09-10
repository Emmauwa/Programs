action  = input("Do you like action movies (yes/no)").lower() == "yes"
romance = input("Do you like romance movies (yes/no)").lower() == "yes"
comedy = input("Do you like comedy movies (yes/no)").lower() == "yes"


if action and romance and comedy:
    genre = "Action-Romance-Comedy"
elif action and romance and not comedy:
    genre = "Action-Romance"
elif action and comedy and not romance:
    genre = "Action-Comedy"
elif comedy and romance and not action:
    genre = "Comedy-Romance"
elif action and not romance and not comedy:
    genre = "Action"
elif romance and not action and not comedy:
    genre = "Romance"
elif comedy and not action and not romance:
    genre = "Comedy"
else:
    genre = "Unknown"

if (genre == "Action-Romance-Comedy"):
    print("Beyond The Boundary")
elif (genre == "Action-Romance"):
    print("Btoom")
elif (genre == "Action-Comedy"):
    print("Gintama")
elif (genre == "Comedy-Romance"):
    print("Kaguya-Sama love is war")
elif (genre == "Action"):
    print("Attack on Titan")
elif (genre == "Romance"):
    print("The Fragrant Flower Blooms with Dignity")
elif (genre == "Comedy"):
    print("Grand Blue")
else: 
    print("Sorry, we couldn't determine your movie preferences.")
