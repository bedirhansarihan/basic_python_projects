# All users and informations
admin_users = {"admin": ["sehir123"]}
student_users = {"Ahmet": ["123", 900, ["mathematics"]], "ayse": ["456", 400, []]}
# ex. student_users = {"name":["password",money,["taken course"]}]}

## Courses and their credits
list_courses = {"physics": 4, "mathematics": 3, "programming": 3}


# LOGIN
def login():
    print("****Welcome to Course Management System**** \nPlease provide login information")
    global username
    username = input("Id: ")
    password = input("Password: ")
    if username in student_users:
        if password == student_users[username][0]:
            print("Successfully logged in!")
            student_menu()
        # call student menu function
        else:
            print("Invalid id or password please try again")
            login()
    elif username in admin_users:
        if password == admin_users[username][0]:
            print("Successfully logged in!")
            admin_menu()

        # call admin menu function
        else:
            print("Invalid id or password please try again")
            login()
    else:
        print("Invalid id or password please try again")
        login()


## admin_menu()

def admin_menu():
    print("Welcome Admin! What do you want to do?")
    print("\n1-List courses")
    print("2-Create a course")
    print("3-Delete a course")
    print("4-Show students registered to a course")
    print("5-Users budget Menu")
    print("6-List Users")
    print("7-Create User")
    print("8-Delete User")
    print("9-Exit")
    while True:
        your_choice = input("\nYour choice: ")
        if your_choice == "1":
            list_course()
        elif your_choice == "2":
            create_a_course()
        elif your_choice == "3":
            delete_a_course()
        elif your_choice == "4":
            show_students_registered_to_a_course()
        elif your_choice == "5":
            user_budget_menu()
        elif your_choice == "6":
            list_users()
        elif your_choice == "7":
            create_a_user()
        elif your_choice == "8":
            delete_a_user()
        elif your_choice == "9":
            login()


# 1- List course
# it shows all course in the system

def list_course():
    print("*** Offered Courses ***")
    print("Course name          Credit")
    number = 1
    for i in list_courses:
        print(number, i, "            ", list_courses[i])
        number += 1

    admin_menu()


# 2- Create a Course
# it creates a new course and saves it to the list_course

def create_a_course():
    new_course = input("What is the name of the course that you want to add?: ")
    new_course_credit = input("How many credits this course has?: ")
    answer = input(new_course + " will be added with " + new_course_credit + "\n Are you sure [Y/N]: ")
    while answer != "Y" and answer != "N":  # nothing can be written except Y-N
        answer = input(new_course + " will be added with " + new_course_credit + "\n Are you sure [Y/N]: ")
    if answer == "Y":
        list_courses[new_course] = int(new_course_credit)  # add new course
        print(new_course + " has been added to courses with " + new_course_credit + " credits\n")
        admin_menu()
    elif answer == "N":  # if answer is N, nothing will be changed
        admin_menu()


# 3- Delete a course
# system deletes the course that admin choose.After course deleted, students taking the course are given money back

def delete_a_course():
    print("*** Offered Courses ***")
    print("Course name          Credit")
    number = 1
    for i in list_courses:
        print(number, "-", i, "            ", list_courses[i])  # it shows courses
        number += 1

    while True:
        deleted_course = input("Which course do you want to delete?: ")
        if (deleted_course) <= str(len(list_courses)) and deleted_course != "" and deleted_course != "0":

            number = 1
            for i in list_courses:
                if int(deleted_course) == number:
                    for j in student_users:
                        if i in student_users[j][2]:
                            student_users[j][1] += (list_courses[i]) * 100
                    list_courses.pop(i)
                    break
                number += 1
            print(i + " has been deleted and money has been transferred back to student accounts\n")
            admin_menu()


### 4- Show students registered to a course
# admin may check which course has been taken by whomever

def show_students_registered_to_a_course():
    show_course = input("Which course do you want to show?: ")
    while show_course not in list_courses:
        print(
            "This course doesn't exist, please provide a valid input")
        show_course = input("Which course do you want to show?: ")
    if show_course in list_courses:
        print("Course name: " + show_course)
        print("Students taking " + show_course)
        number = 1
        for i in student_users:
            if show_course in student_users[i][2]:
                print(number, "-", i)
                number += 1

    admin_menu()


### 5- User budget menu
# admin may add money to users's account
# admin may subtract money from users's account

def user_budget_menu():
    print("User          Money")
    number = 1
    for i in student_users:
        print(number, i, "      ", student_users[i][1])  # it shows all users budget
        number += 1

    print("What do you want to do?\n")
    print("1-Add money to user")
    print("2-Subtract money from user")
    print("3-Back to admin menu")

    your_choice1 = input("\nYour choice: ")
    while your_choice1 != "1" and your_choice1 != "2" and your_choice1 != "3":  # nothing can be written except 1-2-3
        your_choice1 = input("\nYour choice: ")

    if your_choice1 == "1":
        print("Which user do you want add money to their account")
        number = 1
        for i in student_users:
            print(number, "-", i)  # choose user to add money
            number += 1

        while True:
            your_choices2 = input("\nYour choice: ")
            if your_choices2 <= str(len(student_users)) and your_choices2 != "" and your_choices2 != "0":
                amount_money = input("How much money do you want to add?: ")

                number1 = 1
                for i in student_users:
                    if your_choices2 == str(number1):
                        your_choices2 = int(your_choices2)
                        print(amount_money + "$ " + "will be added to ", i)
                        while True:
                            answer1 = input("Are you sure?[Y/N]: ")
                            if answer1 == "Y":
                                student_users[i][1] += int(amount_money)  # Add money his/her account

                                admin_menu()
                            elif answer1 == "N":
                                admin_menu()

                    number1 += 1

    if your_choice1 == "2":
        print("Which user do you want subtract money to their account")
        number = 1
        for i in student_users:
            print(number, "-", i)  # choose user to subtract money
            number += 1

        while True:
            your_choices2 = input("\nYour choice: ")
            if your_choices2 <= str(len(student_users)) and your_choices2 != "0" and your_choices2 != "":
                amount_money = input("How much money do you want to subtract?: ")

                number2 = 1
                for i in student_users:
                    if int(your_choices2) == number2:
                        print(amount_money + "$ " + "will be subtract to ", i)
                        while True:
                            answer2 = input("Are you sure?[Y/N]: ")
                            if answer2 == "Y":
                                student_users[i][1] -= int(amount_money)  # subtract Money his/her account
                                admin_menu()
                            elif answer2 == "N":
                                admin_menu()

                    number2 += 1

    if your_choice1 == "3":
        admin_menu()


### 6-List users
# it shows the user

def list_users():
    print("Current Users:\n")
    number = 1
    for i in student_users:  # shows current student users
        print(number, "-", i)
        number += 1
    while True:
        press_1 = input(
            "\npress 1 to return to admin menu")  # nothing has been written in mini project file, I added to return menu
        if press_1 == "1":
            admin_menu()


#### 7- Create a new user
def create_a_user():
    username1 = input("What is the name of user that you want to create?: ")
    password1 = input("What is the password for account?: ")
    default_money = input("How much money do you want user to have?:  ")
    # while True:
    #    default_money = input ("How much money do you want user to have?:  ")
    #    if default_money in str (list (range (1, 99999))) and default_money != "":  # I couldn't solve differently
    #        break
    # if default_money == str, code will ask the question again.
    student_users[username1] = [password1, int(default_money),
                                []]  # ex. student_users = {"name":["password",money,"taken course"}]}
    print("\nThe new user has been added successfully!")
    admin_menu()


### 8- Delete a user
def delete_a_user():
    print("Current Users:\n")
    number = 1
    for i in student_users:  # shows current student users
        print(number, "-", i)
        number += 1

    while True:
        number1 = 1
        deleted_user = input("Which user do you want to delete: ")
        if int(deleted_user) < number:
            for i in student_users:
                if int(deleted_user) == number1:
                    student_users.pop(i)  # delete the user
                    print(i + " is deleted!")
                    admin_menu()
                number1 += 1


### 9- Exit for admin menu  ### 5- Exit for student menu
def exitt():
    login()


########################################################
### Student Menu
def student_menu():
    print("Welcome", username, "What do you want to do?")
    print("\n1-Add courses to my courses")
    print("2-Delete a course from my courses")
    print("3-Show my courses")
    print("4-Budget Menu")
    print("5-Exit")
    while True:
        your_choice = input("\nYour choice: ")
        if your_choice == "1":
            add_courses_to_my_courses()
        elif your_choice == "2":
            delete_a_course_from_my_courses()
        elif your_choice == "3":
            show_my_courses()
        elif your_choice == "4":
            budget_menu()
        elif your_choice == "5":
            exitt()


### 1-Add course to his/her course
def add_courses_to_my_courses():
    print("Course name          Credit")
    number = 1
    for i in list_courses:
        print(number, i, "            ", list_courses[i])
        number += 1
    number1 = 1

    # # While loop part does not allow to enter an invalid character. such as str
    while True:
        user_choice = input("Which course do you want to take (Enter 0 to go to main menu)?: ")
        if user_choice == "0":
            student_menu()
        elif int(user_choice) <= len(list_courses) and user_choice != "":
            for j in list_courses:
                if user_choice == str(number1) and user_choice != "":
                    ### IF COURSE NOT IN USER'S LIST AND USER HAVE ENOUGH MONEY, COURSE WİLL BE ADDED TO LIST
                    if j not in student_users[username][2] and student_users[username][1] > list_courses[j] * 100:
                        student_users[username][2].append(j)  # COURSE ADDED
                        student_users[username][1] -= list_courses[j] * 100  # CREDITS * 100$ SUBTRACT HIS/HER ACCOUNT
                        print("\n", j, "has been successfully added to your courses.\n")
                        student_menu()
                    ### IF COURSE NOT IN USER's LIST AND USER DOESN'T HAVE ENOUGH MONEY,COURSE WON'T BE ADDED TO LIST AND USER_CHOICE WİLL REPEAT
                    elif j not in student_users[username][2] and student_users[username][1] < list_courses[j] * 100:
                        print(
                            "You don't have enough money in your account.Please deposit money or choose a course with lesser credits")

                    ### IF COURSE IN USER'S LIST, COURSE WON'T BE ADDED TO LIST AND USER_CHOICE WILL REPEAT
                    elif j in student_users[username][2]:
                        print("This course is already in your profile, please choose another course:")
                number1 += 1
            number1 = 1


### 2-Delete course
def delete_a_course_from_my_courses():
    print("Course name          Credit")
    number = 1
    for i in student_users[username][2]:  # it shows courses that user have
        print(number, "-", i, "        ", list_courses[i])
        number += 1

    while True:
        your_choice = input("Which course do you want to remove?: ")
        if your_choice <= str(number - 1) and your_choice != "":

            number1 = 1
            for j in student_users[username][2]:
                if int(your_choice) == number1:
                    print("You have chosen: " + j)
                    print(list_courses[j] * 100, "will be returned to your account")
                    while True:
                        yes_no = input("Are you sure that you want to remove this course?[Y/N]: ")
                        if yes_no == "Y":
                            student_users[username][2].remove(j)  # it removes the course from user's account
                            student_users[username][1] += list_courses[j] * 100  # then, it gives them money back
                            student_menu()
                        elif yes_no == "N":
                            student_menu()

                number1 += 1


# 3- Show user's courses
def show_my_courses():
    print("Course name          Credit")
    number = 1
    for i in student_users[username][2]:
        print(number, "-", i, "        ", list_courses[i])
        number += 1

    student_menu()


# 4- Budget menu
# users add money themselves
def budget_menu():
    print("#### BUDGET MENU #####")
    print("Your budget is: " + str(student_users[username][1]) + "$\n")
    print("What do you want to do?")
    print("1-Add Money")
    print("2-Go to main menu")
    while True:
        your_choice = input("Your choice: ")

        if your_choice == "1":
            added_money = input("Amount of money: ")
            student_users[username][1] += int(added_money)
            print("\nYour budget has been updated.")
            student_menu()

        elif your_choice == "2":
            student_menu()


login()
