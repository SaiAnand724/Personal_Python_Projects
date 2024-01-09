# @title Morse Code Translator using Binary Search Tree
# @author Sai Anand
# @version python3 3.11.7 
# Updated - 1/05/2024

# Importing necessary libraries and dependencies
#"""
#Node class used from binarytree python library.
#Powershell command
#    pip install binarytree

#The node class represents the structure of a particular node in the binary tree. 
#The attributes of this class are values, left, right.
 
#Syntax: binarytree.Node(value, left=None, right=None)
#Parameters: 
#value: Contains the data for a node. This value must be number. 
#eft: Contains the details of left node child. 
#right: Contains details of the right node child. 

#build() function - Creates a tree from a list representation.

#"""
#from binarytree import Node, build

import sys

# tabulate module used to print morse code guide
from tabulate import tabulate

# @param 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Global dictionary meant to hold relevant characters with corresponding Morse code elements
morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }



"""
Source Link: https://www.codecademy.com/learn/learn-data-structures-and-algorithms-with-python/modules/nodes/cheatsheet
Python Node implementation
A Node is a data structure that stores a value that can be of 
    any data type and has a pointer to another node. 
The implementation of a Node class in a programming language 
    such as Python, should have methods to get the value that is 
    stored in the Node, to get the next node, and to set a link to the next node.
    
ex. 

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value
"""

def build_morse_tree():
    root = Node('')

    for char, code in morse_code_dict.items():
        current_node = root

        for digit in code:
            if digit == '.':
                if current_node.left is None:
                    current_node.left = Node('')
                current_node = current_node.left
            elif digit == '-':
                if current_node.right is None:
                    current_node.right = Node('')
                current_node = current_node.right

        current_node.data = char

    return root

# @param 
def print_morse_tree(node, depth=4):
    if node is None:
        return

    indent = '  ' * depth
    print(f"{indent}- {node.data}")

    if node.left:
        print_morse_tree(node.left, depth + 1)

    if node.right:
        print_morse_tree(node.right, depth + 1)

# @param 
def encode_morse_code(word):
    root = build_morse_tree()
    morse_code = ''

    for char in word.upper():
        if char == ' ':
            morse_code += ' / '
        else:
            current_node = root

            while current_node is not None and current_node.data != char:
                if char < current_node.data:
                    if current_node.left is None:
                        break
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        break
                    current_node = current_node.right

            if current_node is not None:
                morse_code += current_node.data + ' '

    return morse_code.strip()

# @param 
def decode_morse_code(morse_code):
    morse_code = morse_code.strip()
    morse_chars = morse_code.split(' ')

    root = build_morse_tree()
    decoded_word = ''

    for morse_char in morse_chars:
        if morse_char == '/':
            decoded_word += ' '
        else:
            current_node = root

            for digit in morse_char:
                if digit == '.':
                    if current_node.left is None:
                        break
                    current_node = current_node.left
                elif digit == '-':
                    if current_node.right is None:
                        break
                    current_node = current_node.right

            decoded_word += current_node.data

    return decoded_word


def print_morse_code_guide():
    print()
    table = []
    for letter, code in morse_code_dict.items():
        table.append([letter, code])

    headers = ['Letter', 'Morse Code']
    print(tabulate(table, headers, tablefmt="grid"))
    print()

def choice1(arg):
    print_morse_code_guide()
    # morse_code_input = input("Enter the Morse code words separated by '/': ")
    if arg == None:
        morse_code_input = input("Enter a Morse code word': ")
    else:
        morse_code_input = arg
        
    decoded_word_output = decode_morse_code(morse_code_input)
    print("Decoded word:", decoded_word_output)
    print()
    
def choice2(arg):
    if arg == None:
        word_input = input("Enter the word: ")
    else:
        word_input = arg
    
    encoded_morse_code_output = encode_morse_code(word_input)
    print("Encoded Morse code:")
    print(encoded_morse_code_output)
    print()

def choice3():
    print("Binary Tree: ")
    root_node = build_morse_tree()
    print_morse_tree(root_node)
    #print("\nBuild function from binarytree: \n", build(morse_code_dict))
    print()
                
def choice4():
    print_morse_code_guide()
    
def choice5():
    print("Exiting the program.")
    exit()
    

# Main function that runs the interface
def morse_code_interpreter(inp):
    print("\nArguments passed:", end = " ")
    for i in range(1, len(inp)):
        print(inp[i], end = " ")
    # Interface loop
    if (len(inp) == 1):
            print("\nSelect an option:")
            print("1. Morse Code to English")
            print("2. English to Morse Code")
            print("3. Print Binary Tree")
            print("4. Print Morse Code Guide")
            print("5. Exit")

            choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
    elif (len(inp) > 2):
        choice = inp[1]
        print("\n1st input", inp[1])
        arg2 = inp[2]
        print("\n2nd input", inp[2])
        
        if choice == '1':
            choice1(arg2)     
        elif choice == '2':
            choice2(arg2)
    
    else: 
        choice = inp[1]
        if choice == '3':
            choice3()
        elif choice == '4':
            choice4()
        elif choice == '5':
            choice5()
        else:
            print("Invalid choice. Please try again.\n")

# Data entry point
if __name__ == "__main__":
    # total arguments
    n = len(sys.argv)
    print("Total arguments passed:", n)

    # Arguments passed
    print("\nName of Python script:", sys.argv[0])

    print("\nArguments passed:", end = " ")
    for i in range(1, n):
        print(sys.argv[i], end = " ")
    
    # manual input
    morse_code_interpreter(sys.argv)
    


