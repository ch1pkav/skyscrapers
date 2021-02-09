from skyscrapers import check_skyscrapers

print("This is a program to easily check a skyscraper game board located in a text file.")
path = input("Enter file location...")

game_completed = check_skyscrapers(path)

if game_completed:
    print("This is a properly completed game")
else:
    print("This is not a properly completed game")

