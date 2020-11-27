import random

class Node:
    leftChild=None
    rightChild=None

    def __init__(self, name="John Doe", phoneNumber="000-000-0000"):
        self.name = name
        self.phoneNumber = phoneNumber

class personData:
    def __init__(self):
        self.size=0
        self.root=None

    def add(self, child):
        if self.size==0:
            self.root=child
            self.size = 1
            return
        current=self.root
        while current != None:
            if child.name < current.name:
                if current.leftChild != None:
                    current = current.leftChild
                else:
                    current.leftChild=child
                    self.size += 1
                    return
            elif child.name > current.name:
                if child.name > current.name:
                    if current.rightChild != None:
                        current = current.rightChild
                    else:
                        current.rightChild=child
                        self.size += 1
                        return
            elif child.name == current.name:
                return

    def remove(self, name):
        current=self.root
        parent=None

        while current != None:
            if name < self.name:
                parent=current
                current=current.leftChild
            elif name > self.name:
                parent=current
                current=current.rightChild
            elif current==None:
                return

            if current.leftChild == None:
                if parent == None:
                    root = current.rightChild
                else:
                    if current.name < parent.name:
                        parent.leftChild = current.rightChild
                    else:
                        parent.rightChild = current.rightChild
            else:
                bookmark = current
                bookmark2 = current.left

                while bookmark2 != None:
                    bookmark = bookmark2
                    bookmark2 = bookmark2.rightChild

                current.name = bookmark2.element

                if bookmark.right == bookmark2:
                    bookmark.right = bookmark2.left
                else:
                    bookmark.left = bookmark2.left

        self.size -= 1

    def contains(self, name):
        if self.size == 0:
            return False

        current=self.root
        while current != None:
            if name < current.name:
                current=current.leftChild
            elif name > current.name:
                current=current.rightChild
            else:
                return True

        return False

    def sort(self, node=0, returnList=[]):
        if node == 0:
            node = self.root
        if node.leftChild != None:
            self.sort(node.leftChild, returnList)
        returnList.append(node.name)
        if node.rightChild != None:
            self.sort(node.rightChild, returnList)
        return returnList


boatName = ["Enterprise","Saratoga","Hornet","Yorktown","Midway","Intrepid","Warspite","Yamato","Kongo","Nagato",
        "Bismarck","Kaga","Akagi","Iowa","North Carolina", "Zuikaku", "Furious", "Gambier Bay", "Johnston", "Samuel B. Roberts",
        "Akatsuki", "Hibiki", "Ikazuchi", "Inazuma"]
randWords = ["Journeys","Odyssey","Adventures","Wanderings","Misadventures","Battles","Songs","Tales",
                "Musings", "Dirge", "Fantasies", "Going-ons", "Heroes", "Lament", "News", "Confessions", "Parties"]

library = personData()

for i in range(20):
    library.add(Node(randWords[random.randint(0, len(randWords)-1)] + " of the " + boatName[random.randint(0, len(boatName)-1)]))

print(library.sort())
