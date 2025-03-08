# Over-engineered mad-libs game.
def getAge ():
    while True:
        try:
            ageInput = int(input("Enter a age: "))
            if ageInput <= 0:
                print("Please enter a proper positive number.")
                continue
            else:
                return ageInput
        except ValueError:
            print("Please enter a whole number.")

def getGenre ():
    validMaleWords = ["male", "m", "man", "boy"]
    validFemaleWords = ["female", "f", "woman", "girl"]
    while True:
        genreInput = str(input("Enter a genre (M/F): ")).lower()
        if genreInput.isdigit():
                print("Your genre can not be a number. ")
                continue
        elif genreInput in validMaleWords:
            return "M"
        elif genreInput in validFemaleWords:
            return "F"
        else:
            print("Could not find this genre. Please try again.")
            continue

def getWord(prompt="Enter a world", want="world"):
    while True:
        wordInput = str(input(prompt))
        if wordInput.isdigit():
            print(f"The world should be a {want}.")
            continue
        else:
            return wordInput

age = getAge()
genre = getGenre()

adjective1 = getWord("Enter a adjetive: ", "adjetive")
noun1 = getWord("Enter a noun: ", "noun")
verb1 = getWord("Enter a verb: ", "verb")
verb2 = getWord("Enter another verb: ", "verb")
noun2 = getWord("Enter a noun: ", "noun")
adjective2 = getWord("Enter a adjetive: ", "adjetive")


if (age >= 18):
    status = f"{age} years old"
elif genre == "M":
    status = "small boy"
elif genre == "F":
    status = "small girl"

print(f"When I was a {status}, I went to a very {adjective1} park.")
print(f"As I entered, I was struck in the head by a flying piece of a {noun1}.")
print(f"In shock, I started {verb1}ing agressively and then threw the {noun1} far away.")
print(f"The park manager insisted in {verb2}ing me and gave me a {noun2} for compensation.")
print(f"It was a {adjective2} experience. I would do it again.")