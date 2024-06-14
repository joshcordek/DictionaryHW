codes = {
    'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '!', 'c': '1',
    'D': '^', 'd': '<', 'E': '&', 'e': '3', 'F': '"', 'f': '^',
    'G': '(', 'g': '5', 'H': ')', 'h': '6', 'I': '+', 'i': '7',
    'J': '_', 'j': '|', 'K': '=', 'k': '}', 'L': '-', 'l': '[',
    'M': '{', 'm': ']', 'N': ']', 'n': '+', 'O': ':', 'o': ';',
    'P': '4', 'p': "'", 'Q': ')', 'q': ',', 'R': '>', 'r': '.',
    'S': '/', 's': '?', 'T': '~', 't': '`', 'U': ',', 'u': '@',
    'V': '#', 'v': '*', 'W': '%', 'w': '^', 'X': '&', 'x': '8',
    'Y': '(', 'y': '2', 'Z': '-', 'z': '_'
}

def encrypt_file(infosec_input, encrypt_output, codes):
    with open(infosec_input, 'r') as file:
        contents = file.read()
    
    encrypted_contents = ''.join(codes.get(char, char) for char in contents)
    
    with open(encrypt_output, 'w') as file:
        file.write(encrypted_contents)

infosec_input= 'info_security-1.txt'
encrypt_output = 'encrypted.txt'


encrypt_file(infosec_input, encrypt_output, codes)


