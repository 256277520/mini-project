
print("Welcome to my quiz")

playing = input("Do you want to play? ")

print("print every letter beginning in uppercase")


if playing != "yes":
    quit()
else:
    print("YaY! let's get started with 'Game of Thrones' ")

score = 0


answer = input("Who killed ned stark? ")

if answer == "Jeoffery":
    print("Correct for 1 point")
    score += 1
else:
    print(":( incorrect, try again")


answer = input("Who was Jon Snow's first? ")

if answer == "Ygritte":
    print("Correct for 1 point")
    score += 1
else:
    print(":( incorrect, try again")


answer = input("Who became the king at the end? ")

if answer == "Bran":
    print("Correct for 1 point")
    score += 1
else:
    print(":( incorrect, try again")



answer = input("Who was tyron's brother? ")

if answer == "Jaime":
    print("Correct for 1 point")
    score += 1
else:
    print(":( incorrect, try again")

print(" Your score is " + str(score))



