import random
doors = ["car", "goat", "goat"]
results = []
trials = 100000

for i in range(trials):
    choice = random.randint(0,2)

    doors = random.sample(doors,len(doors))

    if choice ==0:
        if doors[1]=="goat":
            newchoice = doors[2]
        elif doors[2]=="goat":
            newchoice = doors[1]
        

    elif choice==1:
        if doors[0]=="goat":
            newchoice = doors[2]
        elif doors[2]=="goat":
            newchoice = doors[0]

    else:
        if doors[0]=="goat":
            newchoice = doors[1]
        elif doors[1]=="goat":
            newchoice = doors[0]

    results.append(newchoice)

x = 0

for i in results:
    if i =="car":
        x+=1

print("Switching is successful in", x, "out of", trials, "trials.")
print("Not switching is successful in", trials - x, "out of", trials, "trials.")
