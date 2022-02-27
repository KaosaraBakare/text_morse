morse_code = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += morse_code[letter] + ' '
        else:
            cipher += ' '
    print(cipher)

def decrypt(message):
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(morse_code.keys())[list(morse_code.values()).index(citext)]
                citext = ''
    return decipher

def main():
    should_continue = True
    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        message = input("Type your message:\n")
        if direction == "encode":
            result = encrypt(message.upper())
            print(result)
        elif direction == "decode":
            message = ".... . .-.. .-.. --- "
            result = decrypt(message)
            print(result)
        result = input("Type 'yes' if you want to go again.Otherwise type 'no'.\n")
        if result == "no":
            should_continue = False
            print("Goodbye")

if __name__ == '__main__':
    main()
