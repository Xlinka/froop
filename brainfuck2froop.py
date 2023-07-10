def bf_to_froop(bf_code):
    bf_to_froop_dict = {
        '>': 'Froop. Froop?', 
        '<': 'Froop? Froop.', 
        '+': 'Froop. Froop.', 
        '-': 'Froop! Froop!', 
        '.': 'Froop! Froop.', 
        ',': 'Froop. Froop!', 
        '[': 'Froop! Froop?', 
        ']': 'Froop? Froop!'
    }
    
    froop_code = ''.join(bf_to_froop_dict[c] for c in bf_code if c in bf_to_froop_dict)
    return froop_code

filename = input("Enter the filename of the Brainfuck code: ")

try:
    with open(filename, 'r') as file:
        bf_code = file.read()
        print(bf_to_froop(bf_code))
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
