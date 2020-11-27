class ticket:
    def __init__(self, PatientInfo):
        self.info = PatientInfo
        self.next=None

x=-1
head=None
tail=None
size=0
while x != 0:
    print("\nWelcome to the Doctor's Office!")
    print("There are currently",size,"patient(s) in line.")
    print("[1] Take a ticket")
    print("[2] Call in a patient")
    print("[3] See who is next")
    print("[3] Quit")
    x = int(input("Enter a number : "))
    if x == 1:
        print("Adding another person to the line :")
        newTicket=ticket(input("What is your name? "))
        if size==0:
            head=newTicket
            tail=newTicket
        else:
            tail.next = newTicket
            tail=tail.next
        size+=1
    if x == 2:
        if size==0:
            print("There is no one in line!")
        else:
            print("Seeing the next patient...")
            print(head.info,"please come in")
            head=head.next
            size-=1
    if x == 3:
        if size > 0:
            print(head.info, " is next.")
        else:
            print("No one!")
print("Office is closing...")
