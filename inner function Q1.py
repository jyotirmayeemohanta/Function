def eligible_for_vote():
    age=int(input("enterb your age"))
    if age<18:
        print("not eligble")
    elif age>=18:
        print("you are eligble")
eligible_for_vote()
