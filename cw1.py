
names = ['John', 'Ivan', 'Marie', 'Slava']

def likes(names):
    #your code here
    if len(names) == 0:
        print("no one likes this")
    elif len(names) == 1:
        print(names[0] + " likes this")
    elif len(names) == 2:
        print(names[0]+ " " + names[1] + " like this")
    elif len(names) == 3:
        print(names[0]+ ", " + names[1] + " and " + names[1] + " like this")
    else: 
        print(names[0]+ ", " + names[1] + " and " + str((len(names)-2)) + " like this")

likes(names)