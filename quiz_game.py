print("Welcome to my computer quiz!")

playing = input("Do you wanna play? ")


if playing.lower()!="yes":
    quit()

print("Okay let`s play!")
score = 0
ans = input("What does CPU stand for? ")
cans = "central processing unit"
if ans.lower() == cans:
    print("Correct!")
    score+=1
else:
    print("Incorrect! the answer is "+ cans)
    
ans = input("What does GPU stand for? ")
cans = "graphics processing unit"
if ans.lower() == cans:
    print("Correct!")
    score+=1
else:
    print("Incorrect! the answer is "+ cans)
    
ans = input("What does RAM stand for? ")
cans = "random access memory"
if ans.lower() == cans:
    print("Correct!")
    score+=1
else:
    print("Incorrect! the answer is "+ cans)
    
ans = input("What does DNS stand for? ")
cans = "domain name system"
if ans.lower() == cans:
    print("Correct!")
    score+=1
else:
    print("Incorrect! the answer is "+ cans)
print("Congratulations you got " + str(score)+ " Questions correct = " + str((score/4)*100)+"%")


 