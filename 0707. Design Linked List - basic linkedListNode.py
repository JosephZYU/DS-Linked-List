"""
Linked List = Data Structures of Nodes

Each Node consist of {Value} + {Pointer}

Head, Node, Node, ... , Tail

 - Singly linked list (单向链结串列)

 - Doubly linked list (双向链表)

1. Value - value at given index, can be any characters, strings, integers and even objects
2. Pointer - point to the Next Node

"""

# "2 Simple Ways To Code Linked Lists In Python"
# 🎬 https://youtu.be/6sBsF13n5ig

# Method 1 of 2: create node class and simply pointing each node to the next node
# Set up a constructor that takes in a value and automatically assigns the next to none


class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

# "3" -> "7" -> "10"
# Create 3 isolated nodes by themselves - NOT connected / linked


node1 = linkedListNode("3")

node2 = linkedListNode("7")

node3 = linkedListNode("10")

node4 = linkedListNode("77")

# Connect the above 3 together
# node1 -> node2 -> node3

node1.nextNode = node2  # node1 -> node2, "3" -> "7"

node2.nextNode = node3  # node2 -> node3, "7" -> "10"

node3.nextNode = node4  # node3 -> node4, "10" -> "77"

# Manually set currentNode as node1 and print all nodes
currentNode = node1

while True:
    print(currentNode.value, "->",)

    # Test if it is last node, break the loop
    if currentNode.nextNode is None:
        print("None")
        break

    # If not last node, set current node to be the next node and continue the loop
    currentNode = currentNode.nextNode
