from tkinter import *
from tkinter.ttk import Combobox
import pickle
import dbm


class Gui(Frame):
    def __init__(self, parent):  # Parent == root
        Frame.__init__(self, parent)
        self.restaurants = {}  # key rest name - value rest object
        self.parent = parent
        self.initUI()
        self.load_data()
        self.comboboxLoadData()

    # Creates tkinter objects
    def initUI(self):
        self.grid()

        self.custName = StringVar()
        self.custNumber = StringVar()
        self.restName = StringVar()
        self.numOfTables = StringVar()
        self.comboVar = StringVar()

        self.restaurantReservationSystemLabel = Label(self, text="Restaurant Reservation System", bg="Blue",
                                                      fg="White", width=150, height=2)

        self.restaurantNameLabel = Label(self, text="Restaurant Name")
        self.restaurantNameEntry = Entry(self, textvariable=self.restName)
        self.numberOfTablesLabel = Label(self, text="Number of Tables")
        self.numberOfTablesEntry = Entry(self, textvariable=self.numOfTables)
        self.createNewRestaurantButton = Button(self, text="Create New Restaurant", command=self.createNewRestaurant)
        self.restaurantLabel = Label(self, text="Restaurant")
        self.combobox = Combobox(self, textvariable=self.comboVar)
        self.combobox.set("Not Selected")
        self.deleteButton = Button(self, text="Delete", command=self.deleteRestaurant)

        self.tableLabel = Label(self, text="Table:    ", padx=5)
        self.tableNumberLabel = Label(self, text="[Not Selected]")
        self.customerNameLabel = Label(self, text="Customer Name: ", padx=10, pady=15)
        self.customerNameEntry = Entry(self, textvariable=self.custName, state=DISABLED)
        self.customerPhoneNumberLabel = Label(self, text="Customer Phone Number: ")
        self.customerPhoneNumberEntry = Entry(self, textvariable=self.custNumber, state=DISABLED)
        self.saveUptadeReservationButton = Button(self, text="Save/Uptade Reservation",
                                                  command=self.saveUptadeReservation)
        self.deleteReservationButton = Button(self, text="Delete Reservation", command=self.deleteReservation)
        self.tableFrame = Frame(self, highlightbackground="black", highlightthickness=2, width=1050, height=300)

        self.restaurantReservationSystemLabel.grid(columnspan=15)

        self.restaurantNameLabel.grid(row=1, column=0, sticky=W)
        self.restaurantNameEntry.grid(row=1, column=1)
        self.numberOfTablesLabel.grid(row=1, column=2)
        self.numberOfTablesEntry.grid(row=1, column=3)
        self.createNewRestaurantButton.grid(row=1, column=4)
        self.restaurantLabel.grid(row=2, column=0, sticky=W)
        self.combobox.grid(row=2, column=1, columnspan=1)
        self.combobox.bind("<<ComboboxSelected>>", self.selectedCombobox)
        self.deleteButton.grid(row=2, column=2)

        self.tableLabel.grid(row=3, column=0, sticky=W)
        self.tableNumberLabel.grid(row=3, column=1, sticky=W)
        self.customerNameLabel.grid(row=3, column=2, sticky=W)
        self.customerNameEntry.grid(row=3, column=3, sticky=W)
        self.customerPhoneNumberLabel.grid(row=3, column=4)
        self.customerPhoneNumberEntry.grid(row=3, column=5)
        self.saveUptadeReservationButton.grid(row=3, column=6)
        self.deleteReservationButton.grid(row=3, column=7)
        self.tableFrame.grid(row=4, column=0, columnspan=115, sticky=W)

    def comboboxLoadData(self):
        try:
            with dbm.open("databases.db", "c") as self.db:
                self.combobox["values"] = pickle.loads(self.db["combobox"])

        except:
            pass

    def load_data(self):
        try:
            with dbm.open("databases.db", "c") as self.db:
                self.restaurants[self.comboVar.get()].tables = pickle.loads(self.db[self.comboVar.get()])

        except:
            pass

    # it deletes all widget inside of frame
    def clearFrame(self):
        for button in self.tableFrame.winfo_children():
            button.grid_forget()

    def showButtons(self):
        self.load_data()
        self.defaultRow = 0
        self.defaultColumn = 0
        self.id = 1
        for rest in self.restaurants:
            for button in self.restaurants[self.comboVar.get()].buttons:
                if self.comboVar.get() == rest:
                    # due to database, determines the reserved table, and configure the button bg.
                    if self.restaurants[self.comboVar.get()].tables[self.id].available:
                        color = "green"
                        button.configure(bg=color)
                    elif not self.restaurants[self.comboVar.get()].tables[self.id].available:
                        color = "red"
                        button.configure(bg=color)
                    button.grid(row=self.defaultRow, column=self.defaultColumn, padx=10, pady=15)
                    self.defaultRow += 1
                    if self.defaultRow == 3:
                        self.defaultColumn += 1
                        self.defaultRow = 0
                    self.id += 1
                    # if self.id == len(self.restaurants[self.comboVar.get ()].buttons):
                    #     break

    def createNewRestaurant(self):
        # it runs if there is incompleted information /  name - phone
        if self.restName.get() == "" and str(self.numOfTables.get()) == "" or self.restName.get() == "" or str(
                self.numOfTables.get()) == "":
            self.entriesCantbeEmptyLabel = Label(self, text="Entries Cannot be Empty", fg="white", bg="red")
            self.entriesCantbeEmptyLabel.grid(row=1, column=5)
            self.entriesCantbeEmptyLabel.after(2000,
                                               self.entriesCantbeEmptyLabel.destroy)  # after 2 second it destroys itself

        else:
            # If User writes string , it runs
            try:
                str(self.numOfTables.get()) == int(self.numOfTables.get())
            except ValueError:
                self.numbersforTablesCanBeDigitsOnlyLabel = Label(self, text="Numbers for Tables Can be Digits Only",
                                                                  fg="white", bg="red")
                self.numbersforTablesCanBeDigitsOnlyLabel.grid(row=1, column=5)
                self.numbersforTablesCanBeDigitsOnlyLabel.after(2000, self.numbersforTablesCanBeDigitsOnlyLabel.destroy)


            else:

                if self.restName.get() not in self.restaurants:
                    self.restaurants[self.restName.get()] = Restaurant(self.numOfTables.get())

                    self.tableButtons()
                if self.restName.get() not in self.combobox["values"]:
                    self.combobox['values'] = (*self.combobox['values'], self.restName.get())

                    with dbm.open("databases.db", "c") as self.db:
                        self.db["combobox"] = pickle.dumps(self.combobox['values'])
                self.restaurantCreatedLabel = Label(self, text="Restaurant Created", fg="white", bg="green")
                self.restaurantCreatedLabel.grid(row=1, column=5)
                self.restaurantCreatedLabel.after(2000, self.restaurantCreatedLabel.destroy)

    def deleteRestaurant(self):
        self.clickAgainToDeleteButton = Button(self, text="Clicked Again To Delete", command=self.deleteRestaurantPart2)
        self.clickAgainToDeleteButton.grid(row=2, column=2)

    # it deletes restaurant
    def deleteRestaurantPart2(self):
        self.deletedLabel = Label(self, text="Delete", fg="white", bg="red")
        self.deletedLabel.grid(row=2, column=3)
        self.deletedLabel.after(2000, self.deletedLabel.destroy)
        self.clearFrame()

        self.combobox.set("Not Selected")
        self.clickAgainToDeleteButton.destroy()

    # when the restaurant called, self.showbuttons() runs and create buttons
    def selectedCombobox(self, event):
        for i in self.combobox['values']:
            if i == self.comboVar.get():
                self.clearFrame()
                self.showButtons()

    # the more objects created, the more tables it creates
    def tableButtons(self):

        self.defaultRow = 0
        self.defaultColumn = 0
        self.butNum = 1
        for j in range(1, self.restaurants[self.restName.get()].tableNum + 1):
            self.j = Button(self.tableFrame, text=j, width=15, height=4, bg="green", fg="white",
                            command=lambda j=j: self.selectedTable(j))
            self.restaurants[self.restName.get()].buttons.append(self.j)

    def selectedTable(self, tableNum):
        self.tableNumberLabel.configure(text=tableNum)
        # it shows the reserved restaurant information ,uptade entries
        for i in self.restaurants[self.comboVar.get()].tables:
            if self.restaurants[self.comboVar.get()].tables[i].available == False and self.tableNumberLabel[
                "text"] == i:
                self.custName.set(self.restaurants[self.comboVar.get()].tables[i].name)
                self.custNumber.set(self.restaurants[self.comboVar.get()].tables[i].phone)
            # update  entries
            elif self.restaurants[self.comboVar.get()].tables[i].available == True and self.tableNumberLabel[
                "text"] == i:
                self.custName.set("")
                self.custNumber.set("")

        self.customerNameEntry.configure(state=NORMAL)
        self.customerPhoneNumberEntry.configure(state=NORMAL)

    def saveUptadeReservation(self):
        # it runs if there is incompleted information /  name - phone
        if self.custName.get() == "" and self.custNumber.get() == "" or self.custName.get() == "" or self.custNumber.get() == "":
            self.incompletedInfo = Label(self, text="Incompleted Info", fg="white", bg="red")
            self.incompletedInfo.grid(row=3, column=8)
            self.incompletedInfo.after(2000, self.incompletedInfo.destroy)  # after 2 second it destroys itself
        else:
            # If User write string , it runs
            try:
                int(self.custNumber.get()) == str
            except ValueError:
                self.phoneNumCanBeDigitsOnlyLabel = Label(self, text="Phone Num Can be Digits Only", fg="white",
                                                          bg="red")
                self.phoneNumCanBeDigitsOnlyLabel.grid(row=3, column=8)
                self.phoneNumCanBeDigitsOnlyLabel.after(2000, self.phoneNumCanBeDigitsOnlyLabel.destroy)


            else:
                # it reserves the table and saves the database
                self.id = 1

                for tableButton in self.restaurants[self.comboVar.get()].buttons:
                    if self.tableNumberLabel["text"] == tableButton["text"]:
                        self.restaurants[self.comboVar.get()].buttons[tableButton["text"] - 1].configure(bg="red")
                        self.restaurants[self.comboVar.get()].tables[tableButton["text"]].change_info(
                            self.custName.get(), self.custNumber.get())

                        with dbm.open("databases.db", "c") as self.db:
                            self.db[self.comboVar.get()] = pickle.dumps(self.restaurants[self.comboVar.get()].tables)

                        self.savedLabel = Label(self, text="Saved", fg="white", bg="green")
                        self.savedLabel.grid(row=3, column=8)
                        self.savedLabel.after(2000, self.savedLabel.destroy)  # after 2 second it destroys itself

    def deleteReservation(self):
        for restaurant in self.restaurants:
            # if the table is not reserved, it runs
            for i in self.restaurants[restaurant].tables:
                if self.restaurants[restaurant].buttons[i - 1]["bg"] == "green" and self.tableNumberLabel["text"] == i:
                    self.tableIsNotReservedLabel = Label(self, text=" Table is not Reserved", fg="white", bg="red")
                    self.tableIsNotReservedLabel.grid(row=3, column=8)
                    self.tableIsNotReservedLabel.after(2000,
                                                       self.tableIsNotReservedLabel.destroy)  # after 2 second it destroys itself

                # if table is not selected, it runs
                if self.tableNumberLabel["text"] == "[Not Selected]":
                    self.firstSelectATableLabel = Label(self, text="First Select a Table", fg="white", bg="red")
                    self.firstSelectATableLabel.grid(row=3, column=8)
                    self.firstSelectATableLabel.after(2000,
                                                      self.firstSelectATableLabel.destroy)  # after 2 second it destroys itself


        else:

            for restaurant in self.restaurants:
                for i in self.restaurants[restaurant].tables:
                    # it deletes the table and uptades the databases
                    if self.restaurants[restaurant].buttons[i - 1]["bg"] == "red" and self.tableNumberLabel[
                        "text"] == i:
                        self.restaurants[restaurant].buttons[i - 1].configure(bg="green")
                        self.reservationDeletedLabel = Label(self, text="Reservation Deleted", fg="white", bg="red")
                        self.reservationDeletedLabel.grid(row=3, column=8)
                        self.reservationDeletedLabel.after(2000,
                                                           self.reservationDeletedLabel.destroy)  # after 2 second it destroys itself

                        self.restaurants[restaurant].tables[
                            i].delete_info()  # name-phone-informations are deleted, available attribute becomes False
                        # uptades database
                        with dbm.open("databases.db", "c") as self.db:
                            self.db[self.comboVar.get()] = pickle.dumps(self.restaurants[self.comboVar.get()].tables)


class Restaurant:
    def __init__(self, numofTables):
        self.tables = {}  # key = integer, value = Object (Table)
        self.buttons = []
        self.tableNum = int(numofTables)
        self.createTables(self.tableNum)

    def createTables(self, tableNum):
        tableNum = int(tableNum)
        self.id = 1
        for i in range(1, tableNum + 1):
            self.tables[self.id] = Table()
            self.id += 1


class Table:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.available = True

    def change_info(self, name, phone):
        self.name = name
        self.phone = str(phone)
        self.available = False

    def delete_info(self):
        self.name = ""
        self.phone = ""
        self.available = True


root = Tk()
root.title("Restaurant Reservation System")
guisystem = Gui(root)
root.mainloop()
