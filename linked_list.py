# Import necessary modules
from sys import argv  # Import argv from the sys module to access command-line arguments
from time import sleep  # Import sleep from the time module to add delays in the program

# Define a Node class to represent individual elements in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Initialize data for the node
        self.next = None  # Initialize the next reference to None

# Initialize head and temp pointers for the linked list
head = None  # Represents the head of the linked list
temp = None  # Temporary pointer used for various operations

# Function to insert a new element at the start of the linked list
def insert_at_start():
    global head  # Use the global head pointer
    temp = head  # Assign the current head to temp
    data = input("Enter element to insert at the start:")  # Get user input for the new element
    new_node = Node(data)  # Create a new Node with the input data
    new_node.next = temp  # Set the next reference of the new node to the current head
    head = new_node  # Update the head to point to the new node

# Function to insert a new element at a specific position in the linked list
def insert_at_position():
    temp = head  # Start at the head of the linked list
    i = 1  # Initialize a counter
    position = int(input("Enter position:"))  # Get the position where the new element should be inserted
    while i < position - 1:  # Traverse the list to reach the position before the desired insertion point
        temp = temp.next
        i += 1
    data = input("Enter element to insert at position:")  # Get user input for the new element
    new_node = Node(data)  # Create a new Node with the input data
    new_node.next = temp.next  # Update the next reference of the new node to the next node of temp
    temp.next = new_node  # Update the next reference of temp to the new node

# Function to insert a new element at the end of the linked list
def insert_at_end():
    temp = head  # Start at the head of the linked list
    data = input("Enter element to insert at end:")  # Get user input for the new element
    new_node = Node(data)  # Create a new Node with the input data
    while temp.next is not None:  # Traverse the list to reach the last node
        temp = temp.next
    temp.next = new_node  # Set the next reference of the last node to the new node

# Function to delete the first element from the linked list
def delete_at_start():
    global head  # Use the global head pointer
    temp = head  # Assign the current head to temp
    head = head.next  # Update the head to point to the next node, effectively removing the first node

# Function to delete an element at a specific position in the linked list
def delete_at_position():
    temp = head  # Start at the head of the linked list
    position = int(input("Enter position to delete element:"))  # Get the position of the element to delete
    i = 1  # Initialize a counter
    while i < position:
        prev_node = temp  # Keep track of the previous node
        temp = temp.next  # Move to the next node
        i += 1
    prev_node.next = temp.next  # Update the next reference of the previous node to skip the deleted node

# Function to delete the last element from the linked list
def delete_at_end():
    temp = head  # Start at the head of the linked list
    while temp.next is not None:  # Traverse the list to reach the second-to-last node
        prev_node = temp  # Keep track of the previous node
        temp = temp.next  # Move to the next node
    prev_node.next = None  # Set the next reference of the second-to-last node to None, effectively removing the last node

# Function to print the elements of the linked list
def print_function():
    temp = head  # Start at the head of the linked list
    while temp is not None:  # Traverse the list until the end is reached
        print(temp.data, end=" ")  # Print the data of the current node
        temp = temp.next  # Move to the next node
    print()  # Print a newline to separate the output

# Main program execution
if __name__ == "__main__":
    # Create a linked list using command-line arguments
    for i in range(1, len(argv)):
        new_node = Node(argv[i])  # Create a new Node with command-line argument data

        if head is None:  # If the linked list is empty, set head and temp to the new node
            temp = head = new_node
        else:  # Otherwise, update the next reference of temp to the new node and move temp to the new node
            temp.next = new_node
            temp = new_node

    # User interaction loop
    while True:
        try:
            print("\nMenu:")
            print("1. Insert at the start")
            print("2. Insert at a specific position")
            print("3. Insert at the end")
            print("4. Delete at the start")
            print("5. Delete at a specific position")
            print("6. Delete at the end")
            print("7. Print linked list")
            print("8. Exit")
            choice = int(input())  # Get the user's choice
            if choice == 1:
                insert_at_start()  # Call the appropriate function based on the user's choice
            elif choice == 2:
                insert_at_position()
            elif choice == 3:
                insert_at_end()
            elif choice == 4:
                delete_at_start()
            elif choice == 5:
                delete_at_position()
            elif choice == 6:
                delete_at_end()
            elif choice == 7:
                print_function()
                sleep(1)  # Add a 1-second delay to make the output more readable
            elif choice == 8:
                print("Exiting the program...")
                break  # Exit the loop and end the program
            else:
                print("Invalid choice, enter again")  # Handle invalid user input
        except:
            pass  # Ignore exceptions to keep the program running smoothly
