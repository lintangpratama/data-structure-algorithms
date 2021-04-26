# Define the Node class
class Node:
  # Define the constructor to add the data to the node
  def __init__(self, dataval):
    self.dataval = dataval
    self.nextval = None

# Define the Single Linked List class
class SLinkedList:
  # Define the constructor of SLinkedList class.
  def __init__(self):
    self.headval = None

  # Printing method
  def listprint(self):
    printval = self.headval
    while printval is not None:
      print(printval.dataval)
      printval = printval.nextval

  # Made a method to add data to the first node (linked list head)
  def atBeginning(self, newdata):
    NewNode = Node(newdata)
    # Update headval with the new data
    NewNode.nextval = self.headval
    self.headval = NewNode
    
  # Made a method to add data to the middle of the linked list
  def inBetween(self, middle_node, newdata):
    if middle_node is None:
      print("The mentioned node is absent.")
      return

  # Define the atEnd function to adding a new node to the last linked list
  def atEnd(self, newdata):
    NewNode = Node(newdata)
    # Updating the data from the last linked list
    # If the headval is none, the new data becomes the headval
    if self.headval is None:
      self.headval = NewNode
      return
    # If the headval is defined, the the NewNode will be added to last node nextval.
    last = self.headval
    while last.nextval:
      last = last.nextval
    last.nextval = NewNode

  # Removing node method
  def RemoveNode(self, Removekey):
    HeadVal = self.headval
    if (HeadVal is not None):
      if (HeadVal.dataval == Removekey):
        self.headval = HeadVal.nextval
        HeadVal = None
        return
    
    while (HeadVal is not None):
      if HeadVal.dataval == Removekey:
        break
      prev = HeadVal
      HeadVal = HeadVal.nextval
    
    if (HeadVal == None):
      return
    
    prev.nextval = HeadVal.nextval
    HeadVal = None

# Made the instance of linked list class and node class
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Made the pointer of headval to e2 object
list.headval.nextval = e2

# Define the nextval
e2.nextval = e3

# Print the whole linked list
list.listprint()