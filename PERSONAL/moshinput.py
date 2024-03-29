name = input("Enter name: ").lower()
message = name.split(" ")
# if name in message:
if name == "abdulbasit":
    run = input("""
Hmmm, it's you again, Bad guy
Have you had lunch? """).lower()
    print()
    if run == "yes":
        print("Perfect, now go read or do something productive")
        print()
        print("You can watch a movie too my boy")
    else:
        print("Sad but trust that you'd eat soon!")
else:
    print("This is awkward, I don't know you, so I don't know what to do")
