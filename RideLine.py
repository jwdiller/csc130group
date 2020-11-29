# [PERSON CLASS] #
# holds the next person and person name
class Person:

    # Constructor
    def __init__(self, name):
        self.name = name;
        self.next = None;



# [LINE CLASS] #
# handles the line
# holds peoples name in a queue
class Line:
    
    # Constructor
    def __init__(self):
        self.head = None; # Start of line
        self.tail = None; # End of line
        self.size = 0;    # Size


    # Adds a person to the end of the queue
    def add(self, newPerson):
        
        # if there is no head then this is where we start
        if(self.head == None):

            # in this case the person would be head + tail
            self.head = newPerson;
            self.tail = newPerson;
            
        else:

            # run through to the end of the queue
            probe = self.head;

            while probe.next != None:
                probe = probe.next;

            # add the person and mark the new tail
            probe.next = newPerson;
            self.tail = newPerson;

        # update size
        self.size += 1;


    # Returns the next person in the queue
    def acceptNext(self):

        # Make sure queue is not empty
        if(self.head != None):

            # return and remove next person in queue
            nextAccepted = self.head;
            
            self.head = self.head.next;
            self.size -= 1;

            if(self.size == 0):
                self.tail = None;
            
            return nextAccepted;


    # Prints the line in this format
    # "[NUMBER_IN_QUEUE]-PERSON_NAME"
    def print(self):
        _id = 1;
        probe = self.head;

        while probe.next != None:
            print("[%s]-%s" % (_id, probe.name));
            _id += 1
            probe = probe.next;

        # dont forget to print the last person
        print("[%s]-%s" % (_id, probe.name));


    # Clears the queue
    def clear(self):
        self.head = None;
        self.tail = None;
        self.size = 0;


        
# Returns only a number input
def nInput(_input):
    # if we catch an exception we return -1
    try:
        return int(input(_input));
    except:
        return -1;



# Globals 
RIDE_LINE = Line();
PROGRAM_RUNNING = False;



# entry point
def main():
    
    RIDE_LINE.clear();
    PROGRAM_RUNNING = True;

    print("[Ride Line Manager]");
    print("");

    # Program Loop
    while PROGRAM_RUNNING:
        
        # print menu
        print("[1]: Add Person");
        print("[2]: Accept Next");
        print("[3]: Print Line");
        print("[4]: Quit");
        print("");

        # ask for input command  
        userChoice = nInput(": ");
        print("");

        # execute according command

        # [ADD PERSON] #
        if(userChoice == 1):
            personName = input("Person name: ");
            
            RIDE_LINE.add(Person(personName));

        # [ACCEPT NEXT PERSON] #
        if(userChoice == 2):
            person = RIDE_LINE.acceptNext();

            if(person != None):
                print("Now Accepting: %s" % person.name);
            else:
                print("Line is empty.");

        # [PRINT LINE] #
        if(userChoice == 3):
            RIDE_LINE.print();

        # [ADD PERSON] #
        if(userChoice == 4):
            PROGRAM_RUNNING = False;

        # {Print stats} #
        
        statSize = RIDE_LINE.size
        statTail = "none";
        statHead = "none";

        if(RIDE_LINE.head != None):
            statHead = RIDE_LINE.head.name;
            
        if(RIDE_LINE.tail != None):
            statTail = RIDE_LINE.tail.name;

        print("\n---------------------------------");
        print("* Line size: %s" % statSize);
        print("* Head: %s" % statHead);
        print("* Tail: %s" % statTail);
        print("---------------------------------\n");

main();
