print("Welcome to my Quiz game!")

playing = input("Are you ready to play?\nType 'yes' or 'no' below\n")


if playing.lower() != "yes":
    print("Please enter a valid input.")
    quit()
else:
    print("Okay! let's play :)")


score = 0

answer = input(" What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input(" What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input(" What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input(" What does SSD stand for? ")
if answer.lower() == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("How much is 1,000 terabytes? ")
if answer.lower() == "1 petabyte" "one petabyte":
   print("Correct!")
   score += 1
else:
   print("Incorrect")

print("You got " + str(score) + " question(s) correct!")
print("You got " + str((score/5) * 100) + "%.")
#                     ((score/5) The number (5) needs to match no. of questions.
