# Creating the initial list of the students
studentlist = ["SANJAY", "GOWDA", "SAN", "JAY", "HITMAN"]
# defining the function which take all the Inputs


def studentmanagement():

    print("\n$$$$$ Welcome to SANJAY Student Management System $$$$$\n")
    print("[Choice 1: Showing the List of Student]")
    print("[Choice 2: Add New Student]")
    print("]Choice 3: Searching Student]")
    print("[Choice 4: Deleting a Student]\n")
    try:
        x = int(input("Enter a choice: "))
    except ValueError:
        exit("\nHi! This is not a Number")
    else:
        print("\n")
# if the choice=1 :
    if(x == 1):
        print("Student List\n")
        for students in studentlist:
            print("** {} **".format(students))
# if the choice =2:
    elif(x == 2):
        studentnew = input("Enter New Student: ")
        if(studentnew in studentlist):
            print("\nThis Student {} Already In The Table".format(studentnew))
        else:
            studentlist.append(studentnew)
            print("\n** New Student {} Added Success **\n".format(studentnew))
            for students in studentlist:
                print("** {} **".format(students))
# if the choice =3:
    elif(x == 3):
        studentsearching = input("Choose Student Name To Search: ")
        if(studentsearching in studentlist):
            print("\n** Record Found for {} **".format(studentsearching))
        else:
            print("\n** No Record Found for {} **".format(studentsearching))
# if the choice =4:
    elif(x == 4):
        studentdelete = input("Choose a Student Name To Delete: ")
        if(studentdelete in studentlist):
            studentlist.remove(studentdelete)
            for students in studentlist:
                print("** {} **".format(students))
        else:
            print("\n** No Record Found for {} **".format(studentdelete))

    elif(x < 1 or x > 4):
        print("Please Enter Valid Choice")

studentmanagement()
# to run the program in a loop:


def continueAgain():
    runningagain = input("Want to continue the process yes/no?: ")
    if(runningagain.lower() == 'yes'):

        studentmanagement()
        continueAgain()
    else:
        quit()
continueAgain()
