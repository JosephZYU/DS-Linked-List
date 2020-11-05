# "2 Simple Ways To Code Linked Lists In Python"
# 🎬 https://youtu.be/6sBsF13n5ig?t=342 ⏰

class linkedListNode:

    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class linkedList:

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        """   
        Step 1 - create a node from the value pass in
        """
        node = linkedListNode(value)

        """
        Step 2.1 - Special Case: Empty list (Due-diligence)
        Check if there is no existing 0️⃣ node already in the list - Empty List scenario
        If there is NO head, set the head to the NEW node we just created. 
        There is nothing to append, simply Return.
        """
        if self.head is None:
            self.head = node
            return

        """
        Step 2.2 - Normal: Non-empty list
        If there are existing nodes, traverse through ⏩ the ENTIRE linked list to find the tail
        Make sure we insert the new node at the tail element
        """
        currentNode = self.head
        while True:
            # If there is no more node 🧐 after the current node we're at, make the next node our node
            # ONLY when the node is at the tail 🔚, we will make the nextNode our node (pass-in value)
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            # Otherwise, we should continue traversing until we find the tail node
            currentNode = currentNode.nextNode

    def printLinkedList(self):
        """
        Create print function to track the progress
        """
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "-> ", end='')
            currentNode = currentNode.nextNode
        print("None")


# Testing

ll = linkedList()
ll.printLinkedList()

ll.insert("33")
ll.printLinkedList()

ll.insert("44")
ll.printLinkedList()

ll.insert("55")
ll.printLinkedList()
