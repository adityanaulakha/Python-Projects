while(1):
    print("\t\t\t\t\t\t||VOTING PORTAL||")
    print()
    print("\t\t\t\t     V O T I N G  L I N E S  A R E  O P E N")
    print()
    m=0
    r=0
    b=0
    k=0
    a=0
    user=input("Enter your username: ")
    password=input("Enter your password: ")
    match user:
        case 'aditya':
            if password=='aditya1':
                print()
                print("WELCOME Aditya")
            else:
                print("Wrong Password!!")
        case 'ankit':
            if password=='ankit1':
                print()
                print("WELCOME Ankit")
            else:
                print("Wrong Password!!")
                break
        case _:
            print("Invalid Username!!")
            break
    print()
    choice1=input("Press 'C' to Continue: ")
    while(1):
        print()
        if (choice1=='c' or choice1=='C'):
            print("MENU:")
            print("1.Representatives.\n2.Symbols for Representatives.\n3.Cast your Vote.\n4.See Votes.\n5.Result.\n6.Exit.")
            choice_2=int(input("Enter your choice: "))
            print()
            if choice_2==1:
                print()
                print("1.Narendra Modi.\n2.Rahul Gandhi.\n3.Mamta Banerjee.\n4.Arvind Kejriwal.\n5.Akhilesh Yadav.")
            elif choice_2==2:
                print()
                print("1.Narendra Modi--> M \n2.Rahul Gandhi--> R \n3.Mamta Banerjee--> B \n4.Arvind Kejriwal--> K \n5.Akhilesh Yadav.--> A")
            elif choice_2==3:
                gen=input("Enter your Gender(M/F): ")
                if gen=="M" or gen=='m':
                    name=input("Enter Your Name:\nMr.")
                elif gen=="F" or gen=='f':
                    stat=input("Single or Married(S/M): ")
                    if stat=="M" or stat=='m':
                        name=input("Enter Your Name:\nMrs.")
                    elif stat=="S" or stat=='s':
                        name=input("Enter Your Name:\nMs.")
                    else:
                        print("Invalid Input!!")
                else:
                        print("Invalid Input!!")
                print()
                age=int(input("Enter your age: "))
                if age>=18 and age<=150:
                    print("ELIGIBLE TO VOTE")
                elif age<18 and age>0:
                    print("NOT ELIGIBLE TO VOTE")
                else:
                    print("INVALID INPUT")
                print()
                choice_3=input("Enter Symbol for your Respective Candidate: ")
                if choice_3=='M' or choice_3=='m':
                    m=m+1
                elif choice_3=='R' or choice_3=='r':
                    r=r+1
                elif choice_3=='B' or choice_3=='b':
                    b=b+1
                elif choice_3=='K' or choice_3=='k':
                    k=k+1
                elif choice_3=='A' or choice_3=='a':
                    a=a+1
            elif choice_2==4:
                print()
                print("Total Votes are:")
                print("1.Narendra Modi-->",m)
                print("2.Rahul Gandhi-->",r)
                print("3.Mamta Banerjee-->",b)
                print("4.Arvind Kejriwal-->",k)
                print("5.Akhilesh Yadav-->",a)
            elif choice_2==5:
                print()
                if (m>r and m>b and m>k and m>a):
                    print("Winner--> Narendra Modi !!!")
                elif (r>m and r>b and r>k and r>a):
                    print("Winner--> Rahul Gandhi !!!")
                elif (b>r and b>m and b>k and b>a):
                    print("Winner--> Mamta Banerjee !!!")
                elif (k>r and k>b and k>m and k>a):
                    print("Winner--> Arvind Kejriwal !!!")
                elif (a>r and a>b and a>k and a>m):
                    print("Winner--> Akhilesh Yadav !!!")
                else:
                    print("Result are not Declared Yet!!")
                print("\nThankyou!!")
            elif choice_2==6:
                break
