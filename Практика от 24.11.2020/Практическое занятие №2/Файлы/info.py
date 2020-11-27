name = input("What`s is your Name?\n>")
lname = input("What`s is your last Name?\n>")
old = input("How old are you?\n>")
std = int(input("You a student? (1 - YES, 2 - NOT)\n>"))
if std == 1:
    study = input("Where do you study?\n>")
    print("You:",name,lname,"\n","Age: ", old,"\n","Study: ",std,study)
else:
    job = input("Where do you work?\n")
    print("You:",name,lname,"\n","Age:", old,"\n","Work:", job)
input("ENTER to exit")
