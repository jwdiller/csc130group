class office:

    def __init__(self, size):
        self.size = size
        self.seats = [None]*size
        self.cursorBegin = 0
        self.cursorEnd = 0
        self.occupied = 0

    def add(self, name):
        if self.occupied == self.size:
            print("There are no seats left!")
        else:
            self.seats[self.cursorEnd] = name
            self.cursorEnd += 1
            if self.cursorEnd == self.size:
                self.cursorEnd = 0
            self.occupied += 1

    def pop(self):
        if self.occupied == 0:
            print("There is no one here!")
            return None
        else:
            name = self.seats[self.cursorBegin]
            self.seats[self.cursorBegin] = None
            self.occupied -= 1
            self.cursorBegin += 1
            if self.cursorBegin == self.size:
                self.cursorBegin = 0
            return name

    def peek(self):
        return self.seats[self.cursorBegin]

    def seeAll(self):
        return self.seats

print("Congrats on your new office, Doctor.")
newOffice = office(int(input("How many seats should your waiting room have? ")))
choice = -1
while choice != 0:
    print("\nWelcome to the Doctor's Office!")
    print("There are",newOffice.size,"seat(s) and",newOffice.occupied,"are being used.")
    print("[1] Take a ticket")
    print("[2] Call in a patient")
    print("[3] See who is next")
    print("[4] See all")
    print("[0] Quit")
    choice = int(input("Enter a number : "))
    if choice == 1:
        newOffice.add(input("What is your name, patient? "))
    elif choice == 2:
        print("Now seeing", newOffice.pop())
    elif choice == 3:
        print(newOffice.peek(),"is next.")
    elif choice == 4:
        print(newOffice.seeAll())
print("Office is closing...")
