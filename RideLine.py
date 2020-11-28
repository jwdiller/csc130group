# basic person class
class Person:
    def __init__(self, name):
        self.name = name;
        self.next = None;

# handles the line
class Line:
    def __init__(self):
        self.head = None;
        self.tail = None;
        self.size = 0;

    # adds a person to the back of the list
    def add(self, newPerson):

        if(self.head == None):
            self.head = newPerson;
        else:
            probe = self.head;

            while probe.next != None:
                probe = probe.next;

            probe.next = newPerson;
            probe.tail = newPerson;

        # update size
        self.size += 1;

    # removes the next person6 in the line
    def acceptNext(self):
        if(self.head != None):
            nextAccepted = self.head;
            
            self.head = self.head.next;
            self.size -= 1;

            return nextAccepted;

    # prints the line
    def print(self):
        _id = 1;
        
        probe = self.head;

        while probe.next != None:
            print("[%s]-%s" % (_id, probe.name));
            _id += 1
            probe = probe.next;
            
        print("[%s]-%s" % (_id, probe.name));

def nInput(_input):
    try:
        return int(input(_input));
    except:
        return 0;

# entry point
def main():
    line = Line();

    running = True;

    print("[Ride Line]");
    
    while running:
        # print menu
        print("[1]: Add Person");
        print("[2]: Accept Next");
        print("[3]: Print Line");
        print("[4]: Quit");
        print("");

        # ask for input        
        userChoice = nInput(":");

        # execute command
        if(userChoice == 1):
            print("");
            personName = input("Person name: ");
            
            line.add(Person(personName));

        if(userChoice == 2):
           person = line.acceptNext();

           if(person != None):
               print("");
               print("Now Accepting: %s" % person.name);

        if(userChoice == 3):
            line.print();

        if(userChoice == 4):
            running = False;

        print("Line size: %s" % line.size);
        print("");

main();
