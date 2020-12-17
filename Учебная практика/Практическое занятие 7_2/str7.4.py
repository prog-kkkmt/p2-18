from string import Template
t = Template('Hey, $name!')
name = input()  #Zachar
print(t.substitute(name=name))
#Hey, Zachar!
