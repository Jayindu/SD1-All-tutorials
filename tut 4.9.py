num=0
while True:
    print("Menu \n select on option entering nmber")
    print("1.Option 1")
    print("2.Option 2")
    print("3.Option 3")
    print("Quit")
    try:
        num=int(input("Enter selected number = "))
        if num==1:
            print("1 selected")
        elif num==2:
            print("2 selected")
        elif num==3:
            print("3 selected")
        else:
            print("Option not recognised")
    except ValueError:
        print("invalid input, enter integer")
    break
    

