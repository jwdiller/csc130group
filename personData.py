class personData:

    leftChild = None
    rightChild = None

    def __init__(self, name="John Doe", phoneNumber="000-000-0000"):
        self.name = name
        self.phoneNumber = phoneNumber

    def add(self, child):
        if (child.name < self.name):
            if (self.leftChild == None):
                self.leftChild=child
            else:
                self.leftChild.add(child)
        else:
            if (self.rightChild == None):
                self.rightChild=child
            else:
                self.rightChild.add(child)

    def remove(self, name):
        if self.name==name:
            if self.leftChild=null:
                self=self.rightChild
            else:

