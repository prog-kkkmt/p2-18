people = {"Prokop", "Polina", "Tom", "Johh", "Kirill"} 
while True:                        
    if len(people) == 0:       
        break                       
    print("do you really want to delete one of your best friends?") 
    answer = input() 
    
    print("what is the name:")
    name = input()
    people.remove(name)
    print("Your friends are ", people)
