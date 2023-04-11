print("Welcome to the Quiez Game!")

question1 = str(input("What do you need to survive ?\n"))

score = 0

if question1.lower() == "food":
    print("You nailed it!")
    score += 1
else:
    print("You messed up!")

question2 = str(input("Where is the capital of japan ?\n"))

if question2.lower() == "tokyo":
    score += 1
    print("You nailed it!")
else:
    print("You messed up!")

question3 = str(input("Who invented the light bulb ?\n"))

if question3.lower() == "edison":
    score += 1
    print("You nailed it!")
else:
    print("You messed up!")

question4 = str(input("What is the material inside the pencil?\n"))

if question4.lower() == "graphite":
    score += 1
    print("You nailed it!")
else:
    print("You messed up!")

question5 = str(input("When you are not depressed means that you are .....\n"))

if question5.lower() == "happy":
    score += 1
    print("You nailed it!")
else:
    print("You messed up!")

print("Your score is {0} of 5".format(score))