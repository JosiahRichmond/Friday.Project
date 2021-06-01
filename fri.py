match=100
inp="none"
matches="|"*match
turn=1
print("""Welcome to Nim bot! The game works as follows:
There are 100 matches. On your turn, you must take 1-10 matches.
After your turn, I will take my turn. The player who takes the
last match loses.""")
print("*\n*")
while inp!="start":
    inp=input("Enter \"start\" to continue: ")
while match>0:
    matches="|"*match
    print("*\n*")
    print(matches)
    print("There are", match, "matches left.")
    print("*\n*")
    if turn==1:
        print("Your turn")
        subtract=int(input("Choose 1-10 matches to remove: "))
        while subtract<1 or subtract>10:
            print("Invalid input")
            subtract=int(input("Choose 1-10 matches to remove: "))
        match-=subtract
        if match<1:
            print("*\n*")
            print("There are no matches left.")
            print("Too bad! You loose!")
        else:
            turn=2
    else:
        print("My turn")
        roboturn=11-subtract
        match-=roboturn
        print("I took", roboturn, "matches.")
        if match<1:
            print("Rats, I lost!")
        else:
            turn=1
print("*\n*\nThanks for playing! Come back sometime soon!")
