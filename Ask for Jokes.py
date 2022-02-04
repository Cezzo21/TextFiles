import os
import random

if os.path.exists("Funny.txt"): #exists
    print("File found. I will continue from where you left off")
    f = open("Funny.txt", "r")

    number = -1
    for number in f:
        pass
    if number == -1:
        f.close()
        os.remove("Funny.txt")
        print("There was an issue with your file, so I had to reset it. Don't worry, it was most likely blank :)")
        f = open("Funny.txt", "x")
    else: #everything is working, and the file exists
        print("You last finished on:", number)
        while True: #so you can go again
            f.close()
            command = input("What would you like to do next (read/edit/add/quit)? ")
            while True: #incase of random input
                if command == "read":
                    f = open("Funny.txt", "r")
                    for line in f:
                        print(line)
                    break
                elif command == "add":
                    f = open("Funny.txt", "a")
                    f.write("\n")
                    joke = input("Okay, give me your best joke: ")
                    f.write(joke)

                    #random reactions:
                    react = random.randint(1, 3)
                    if react == 1:
                        print("AHAHAHAHA I LOVE IT")
                    elif react == 2:
                        print("uhhh okay, anyway...")
                    elif react == 3:
                        print("lmaooo good one XD")
                    break
                elif command == "edit":
                    f = open("Funny.txt", "r")
                    jokelist = []
                    for line in f:
                        jokelist.append(line)
                    f.close()

                    edit = int(input("What joke number would you like to change? "))
                    if edit > len(jokelist):
                        print("You're tryna outsmart me? BYE")
                        quit()
                    else:
                        newjoke = input("What would you like to change it to? ")

                    f = open("Funny.txt", "w")
                    n = 1
                    for line in jokelist:
                        if not n == edit:#we are re-writing the file basically
                            f.write(line)
                        else:
                            f.write(newjoke)
                            f.write("\n")
                        n += 1

                    print("Yeah I think that one is much better.")
                    break
                elif command == "quit":
                    print("Okay, thanks for keeping me company :)")
                    print("See ya!")
                    quit()
                else:
                    command = input("I'm sorry, I did not understand. Can you try again? I only take 'read', 'add', 'edit', and 'quit' for an answer: ")
else:
    print("File not found. I will create one")
    f = open("Funny.txt", "w")
    joke = input("Now let's add a joke: ")
    f.write(joke)
    print("Great job :)")

    #copy paste of lines 18-73
    while True:  # so you can go again
        f.close()
        command = input("What would you like to do next (read/edit/add/quit)? ")
        while True:  # incase of random input
            if command == "read":
                f = open("Funny.txt", "r")
                for line in f:
                    print(line)
                break
            elif command == "add":
                f = open("Funny.txt", "a")
                f.write("\n")
                joke = input("Okay, give me your best joke: ")
                f.write(joke)

                # random reactions:
                react = random.randint(1, 3)
                if react == 1:
                    print("AHAHAHAHA I LOVE IT")
                elif react == 2:
                    print("uhhh okay, anyway...")
                elif react == 3:
                    print("lmaooo good one XD")
                break
            elif command == "edit":
                f = open("Funny.txt", "r")
                jokelist = []
                for line in f:
                    jokelist.append(line)
                f.close()

                edit = int(input("What joke number would you like to change? "))
                if edit > len(jokelist):
                    print("You're tryna outsmart me? BYE")
                    quit()
                else:
                    newjoke = input("What would you like to change it to? ")

                f = open("Funny.txt", "w")
                n = 1
                for line in jokelist:
                    if not n == edit:  # we are re-writing the file basically
                        f.write(line)
                    else:
                        f.write(newjoke)
                        f.write("\n")
                    n += 1

                print("Yeah I think that one is much better.")
                break
            elif command == "quit":
                print("Okay, thanks for keeping me company :)")
                print("See ya!")
                quit()
            else:
                command = input("I'm sorry, I did not understand. Can you try again? I only take 'read', 'add', 'edit', and 'quit' for an answer: ")




quit()