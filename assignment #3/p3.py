class User():

    def __init__(self, username, password, budget):
        self.username = username
        self.password = password
        self.budget = budget
        self.registered_courses = []

    def display(self):
        return self.username + "           " + str(self.budget)

    def canTakeCourse(self, selected_course):
        if selected_course * 100 < self.budget:
            return True
        else:
            return False

    def courseExists(self, course):
        if course not in self.registered_courses:
            return False
        else:
            return True


class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.registered_user = []

    def display(self):  # it shows students information
        return self.name + "               " + str(self.credits)

    def deleteCourse(self):
        if username == "admin":
            for user in obj1.users:
                if self in obj1.users[user][
                    3]:  # if admin delete a course, course will be deleted and students taking that course, will give their money back
                    obj1.users[user][3].remove(self)
                    obj1.users[user][2] += self.coursePrice()
            obj1.courses.remove(self)
            obj1.showAdminMenu()
        elif username != "admin":
            for user in obj1.users:
                if username == obj1.users[user][0]:
                    obj1.users[user][3].remove(self)
                    obj1.users[user][2] += self.coursePrice()
            obj1.showStudentMenu()

    def coursePrice(self):
        return 100 * int(self.credits)


class Menu:
    def __init__(self, header):
        self.header = header
        self.items = []

    def display(self):  # it displays the items attribute
        print(self.header + "\n")
        for i in self.items:
            print(i.displayMenuItem())

    def addMenuItem(self, number, text):  # it creates a MenuItem objects and add to items attribute
        self.items.append(MenuItem(number, text))


class MenuItem:
    def __init__(self, number, text):
        self.number = number
        self.text = text

    def displayMenuItem(self):
        return str(self.number) + " - " + self.text


class CourseManagementSystem:

    def __init__(self):
        self.users = {}  # Keys are Users object such as"<__main__.User object at 0x036A0690>", values are information
        self.courses = []  # Course objects are stored in this list
        self.current_user = []  # User objects are stored in this list as well
        self.admin_menu = Menu("Welcome to Admin Menu")  # admin menu object
        self.student_menu = Menu("Welcome to Student Menu")  # student menu object
        self.build_menus("admin")  # menuItem objects for admin menu
        self.build_menus("student")  # menuItem objects for student menu

    def login(self):
        print("****Welcome to Course Management System**** \nPlease provide login information")
        global username
        username = input("Id: ")
        password = input("Password: ")

        if username == "admin":
            if password == "sehir123":  # There is no officially admin user
                print("Successfully logged in!")
                self.showAdminMenu()
            else:
                print("Invalid id or password please try again")
                self.login()
        for user in self.users:
            if self.users[user][0] == username and self.users[user][1] == password:
                print("Successfully logged in!")
                self.showStudentMenu()
        else:
            self.login()

    # Each two menu created here
    def build_menus(self, type):
        if type == "admin":
            self.admin_menu.addMenuItem(1, "List Courses")
            self.admin_menu.addMenuItem(2, "Create a course")
            self.admin_menu.addMenuItem(3, "Delete a course")
            self.admin_menu.addMenuItem(4, "Show students registered to a course")
            self.admin_menu.addMenuItem(5, "User budget menu")
            self.admin_menu.addMenuItem(6, "List Users")
            self.admin_menu.addMenuItem(7, "Create a user")
            self.admin_menu.addMenuItem(8, "Delete a user")
            self.admin_menu.addMenuItem(9, "Exit")

        elif type == "student":
            self.student_menu.addMenuItem(1, "Add courses to my courses")
            self.student_menu.addMenuItem(2, "Delete a course from my courses")
            self.student_menu.addMenuItem(3, "Show my courses")
            self.student_menu.addMenuItem(4, "Budget Menu")
            self.student_menu.addMenuItem(5, "Exit")

    # it controls to admin menu while admin sign in
    def showAdminMenu(self):

        self.admin_menu.display()
        while True:
            choice = input("Your choice: ")
            # 1- list Courses
            if choice == "1":
                print("*** Offered Courses ***")
                print("Course name          Credit")
                number = 1
                for x in self.courses:
                    print(number, "-", x.display())  # it will print course object's information
                    number += 1
                self.showAdminMenu()

            # 2- Create a Course
            elif choice == "2":
                name = input("What is the name of the course that you want to add?: ")
                credits = input("How many credits this course has?: ")
                created_course = Course(name, credits)  # it creates a new Course object
                self.courses.append(created_course)  # it stores the created course in self.courses
                self.showAdminMenu()

            # 3- Delete Course
            elif choice == "3":
                print("*** Offered Courses ***")
                print("Course name          Credit")
                number = 1
                for course in self.courses:
                    print(number, course.display())
                    number += 1
                deleted_course = input("Which course do you want to delete(Write course name): ")
                for i in self.courses:
                    if deleted_course == i.name:
                        print(i.name, "has been deleted and money has been transferred back to student accounts\n")
                        i.deleteCourse()  # selected Course object will be deleted by using deleteCourse() method
                print("Course does not exist\n")
                self.showAdminMenu()


            # 4 - Show students to registered a course
            elif choice == "4":  # if there are no courses created , it will return to admin menu
                print("*** Offered Courses ***")
                print("Course name          Credit")
                number1 = 1
                for x in self.courses:
                    print(number1, "-", x.display())  # it will print course object's information
                    number1 += 1
                for course_obj in self.courses:
                    show_course = input("Which course do you want to show?: ")
                    while course_obj.name != show_course:
                        print("This course doesn't exist, please provide a valid input")
                        show_course = input("Which course do you want to show?: ")
                    if course_obj.name == show_course:
                        print("Course name: " + course_obj.name)
                        print("\nStudents taking " + show_course)
                        number = 1
                        for user in self.users:
                            if user.name in self.users:
                                print(str(number), "-", user.name)
                                number += 1
                self.showAdminMenu()

            # 5- User Budget Menu
            elif choice == "5":
                print("User          Money")
                number = 1
                for i in self.users:
                    print(number, i.username, "      ", self.users[i][2])  # it shows all users budget
                    number += 1

                print("What do you want to do?\n")
                print("1-Add money to user")
                print("2-Subtract money from user")
                print("3-Back to admin menu")

                your_choice1 = input("\nYour choice: ")
                while your_choice1 != "1" and your_choice1 != "2" and your_choice1 != "3":  # nothing can be written except 1-2-3
                    your_choice1 = input("\nYour choice: ")
                # Add money to user
                if your_choice1 == "1":
                    print("Which user do you want add money to their account")
                    number = 1
                    for i in self.users:
                        print(number, "-", i.username)  # choose user to add money
                        number += 1
                    while True:
                        your_choices2 = input("\nYour choice: ")
                        if your_choices2 <= str(len(self.users)) and your_choices2 != "" and your_choices2 != "0":
                            amount_money = input("How much money do you want to add?: ")

                            number1 = 1
                            for i in self.users:
                                if your_choices2 == str(number1):
                                    your_choices2 = int(your_choices2)
                                    print(amount_money + "$ " + "will be added to ", i.username)
                                    while True:
                                        answer1 = input("Are you sure?[Y/N]: ")
                                        if answer1 == "Y":
                                            self.users[i][2] += int(amount_money)  # Add money his/her account

                                            self.showAdminMenu()
                                        elif answer1 == "N":
                                            self.showAdminMenu()

                                number1 += 1
                if your_choice1 == "2":
                    print("Which user do you want subtract money to their account")
                    number = 1
                    for i in self.users:
                        print(number, "-", i.username)  # choose user to subtract money
                        number += 1

                    while True:
                        your_choices2 = input("\nYour choice: ")
                        if your_choices2 <= str(len(self.users)) and your_choices2 != "0" and your_choices2 != "":
                            amount_money = input("How much money do you want to subtract?: ")

                            number2 = 1
                            for i in self.users:
                                if int(your_choices2) == number2:
                                    print(amount_money + "$ " + "will be subtract to ", i.username)
                                    while True:
                                        answer2 = input("Are you sure?[Y/N]: ")
                                        if answer2 == "Y":
                                            self.users[i][2] -= int(amount_money)  # subtract Money his/her account
                                            self.showAdminMenu()
                                        elif answer2 == "N":
                                            self.showAdminMenu()

                                number2 += 1
                if your_choice1 == "3":
                    self.showAdminMenu()

            # 6- List Users
            elif choice == "6":
                print("Current Users:\n")
                number = 1
                for i in self.current_user:
                    print(number, "-", i.username)
                    number += 1
                self.showAdminMenu()

            # 7- Create a User
            elif choice == "7":
                username = input("What is the name of user that you want to create?: ")
                password = input("What is the password for account?: ")

                default_money = input("How much money do you want user to have?:  ")
                # it creates a new User object and stores in self.users and self.current_user
                created_user = User(username, password, int(default_money))
                self.users[created_user] = [username, password, int(default_money), []]
                self.current_user.append(created_user)

                print("\nThe new user has been added successfully!\n")
                self.showAdminMenu()

            # 8- Delete User
            elif choice == "8":
                print("Current Users:\n")
                number = 1
                for user in self.users:  # shows current student users
                    print(number, "-", user.username)
                    number += 1
                while True:
                    number1 = 1
                    deleted_user = input("Which user do you want to delete: ")
                    if int(deleted_user) < number:
                        for i in self.users:
                            if int(deleted_user) == number1:
                                self.users.pop(i)  # delete the user
                                self.current_user.remove(i)
                                print(i.username + " is deleted!")
                                self.showAdminMenu()
                            number1 += 1


            # 9- Exit
            elif choice == "9":
                self.login()


    # it controls to student menu while he/she sign in
    def showStudentMenu(self):
        self.student_menu.display()
        while True:
            choice = input("Your choice: ")

            # 1 - Adding Courses platform
            if choice == "1":
                print("Course name          Credit")
                number = 1
                for course in self.courses:  # it shows courses that user have
                    print(number, "-", course.display())
                    number += 1
                number1 = 1

                while True:
                    user_choice = input("Which course do you want to take (Enter 0 to go to main menu)?: ")
                    if user_choice == "0":
                        self.showStudentMenu()
                    elif int(user_choice) <= len(self.courses) and user_choice != "":
                        for course in self.courses:
                            for user in self.users:
                                if user_choice == str(number1) and user_choice != "":
                                    if self.users[user][0] == username and course not in self.users[user][3] and \
                                            self.users[user][2] > course.coursePrice():
                                        self.users[user][3].append(course)  # COURSE ADDED
                                        self.users[user][
                                            2] -= course.coursePrice()  # CREDITS * 100$ SUBTRACT HIS/HER ACCOUNT
                                        print("\n", course.name, "has been successfully added to your courses.\n")
                                        self.showStudentMenu()
                                    elif self.users[user][0] == username and course not in self.users[user][3] and \
                                            self.users[user][2] < course.coursePrice():
                                        print(
                                            "You don't have enough money in your account.Please deposit money or choose a course with lesser credits")

                                    elif self.users[user][0] == username and course in self.users[user][3]:
                                        print("This course is already in your profile, please choose another course:")
                            number1 += 1
                        number1 = 1

            # 2- Delete course in your account
            elif choice == "2":
                print("Course name          Credit")
                number = 1
                for user in self.users:  # it shows courses that user have
                    if self.users[user][0] == username:
                        for course in self.users[user][3]:
                            print(number, "-", course.name, "        ", course.credits)
                            number += 1
                deleted_course = input("Which course do you want to delete(Write Course name): ")
                for i in self.courses:
                    if deleted_course == i.name:
                        print(i.name, "has been deleted in your account")
                        i.deleteCourse()




            # 3- Show user's courses
            elif choice == "3":
                print("Course name          Credit")
                number = 1
                for user in self.users:
                    if self.users[user][0] == username:
                        for course in self.users[user][3]:
                            print(number, "-", course.name, "             ", course.credits)
                            number += 1

                self.showStudentMenu()

            # 4- Budget Menu
            elif choice == "4":
                for user in self.users:
                    if user.username == username:
                        print("#### BUDGET MENU #####")
                        print("Your budget is: ", self.users[user][2])
                        print("What do you want to do?")
                        print("1-Add Money")
                        print("2-Go to main menu")
                        while True:
                            your_choice = input("Your choice: ")

                            if your_choice == "1":
                                added_money = input("Amount of money: ")
                                self.users[user][2] += int(added_money)  # add money
                                print("\nYour budget has been updated.")
                                self.showStudentMenu()

                            elif your_choice == "2":
                                self.showStudentMenu()


            # 5- Exit
            elif choice == "5":
                self.login()


obj1 = CourseManagementSystem()

obj1.login()
