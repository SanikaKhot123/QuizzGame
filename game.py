print("Let's know how much you know India.")
playing = input("Are you ready to play this quiz ? ").lower()
score = 0

if playing != "yes" :
    quit()
else:
    print("Okay! Let's play ")

answer = input("What is the capital of India? ")
if answer.lower() == "delhi":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is the National Anthem of India? ")
if answer.lower() == "jana gana mana":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What is the National Song of India? ")
if answer.lower() == "vande mataram":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What is the National Flower of India? ")
if answer.lower() == "lotus":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is the National Animal of India? ")
if answer.lower() == "tiger":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is the National Bird of India? ")
if answer.lower() == "peacock":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What is the National Tree of India? ")
if answer.lower() == "banyan":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What is the National Game of India? ")
if answer.lower() == "hockey":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What is the National Fruit of India? ")
if answer.lower() == "mango":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is the National River of India? ")
if answer.lower() == "ganga":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("Your score is "+ str(score) + " question right!")
print("You score " + str((score/10)*100) + "%")