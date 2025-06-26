print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does BIOS stand for? ")
if answer.lower() == "basic input output system":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PDF stand for? ")
if answer.lower() == "portable document format":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does OS stand for? ")
if answer.lower() == "operating system":
    print('Correct!')
    score += 1
else:
    print('Incorrect!') 

answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")