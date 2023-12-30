from tabulate import tabulate

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_morse_tree():
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    root = Node('')

    for char, code in morse_code.items():
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


def print_morse_tree(node, depth=0):
    if node is None:
        return

    indent = '  ' * depth
    print(f"{indent}- {node.data}")

    if node.left:
        print_morse_tree(node.left, depth + 1)

    if node.right:
        print_morse_tree(node.right, depth + 1)


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
    morse_code_guide = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    table = []
    for letter, code in morse_code_guide.items():
        table.append([letter, code])

    headers = ['Letter', 'Morse Code']
    print(tabulate(table, headers, tablefmt="grid"))
    print()


# Interface loop
while True:
    print("Select an option:")
    print("1. Morse Code to English")
    print("2. English to Morse Code")
    print("3. Print Binary Tree")
    print("4. Print Morse Code Guide")
    print("5. Exit")

    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

    if choice == '1':
        print_morse_code_guide()
        morse_code_input = input("Enter the Morse code words separated by '/': ")
        decoded_word_output = decode_morse_code(morse_code_input)
        print("Decoded word:", decoded_word_output)
        print()
    elif choice == '2':
        word_input = input("Enter the word: ")
        encoded_morse_code_output = encode_morse_code(word_input)
        print("Encoded Morse code:")
        print(encoded_morse_code_output)
        print()
    elif choice == '3':
        print("Binary Tree:")
        root_node = build_morse_tree()
        print_morse_tree(root_node)
        print()
    elif choice == '4':
        print_morse_code_guide()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.\n")
