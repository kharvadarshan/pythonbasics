
dict = {}

while True:
    choice = int( input("Enter Choice (1,2,3):"))
    if(choice==1):
        name = input("Enter Student Name:")
        marks = int(input("Enter Marks:"))
        dict[name] = marks
    elif(choice==2):
        name = input("Enter Student Name:")
        marks = int(input("Enter updated Marks:"))
        dict[name] = marks
    elif(choice==3):
        for(name, marks) in dict.items():
            print(f"{name} : {marks}")
    else:
        break