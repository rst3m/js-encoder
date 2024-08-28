import urllib.parse
import base64

# ASCII Art to display at the start
ascii_art = """
   $$$$$\ $$$$$$\        $$$$$$$$\                                 $$\                                                                 
   \__$$ $$  __$$\       $$  _____|                                $$ |                                                                
      $$ $$ /  \__|      $$ |     $$$$$$$\  $$$$$$$\ $$$$$$\  $$$$$$$ |$$$$$$\  $$$$$$\                                                
      $$ \$$$$$$\        $$$$$\   $$  __$$\$$  _____$$  __$$\$$  __$$ $$  __$$\$$  __$$\                                               
$$\   $$ |\____$$\       $$  __|  $$ |  $$ $$ /     $$ /  $$ $$ /  $$ $$$$$$$$ $$ |  \__|                                              
$$ |  $$ $$\   $$ |      $$ |     $$ |  $$ $$ |     $$ |  $$ $$ |  $$ $$   ____$$ |                                                    
\$$$$$$  \$$$$$$  |      $$$$$$$$\$$ |  $$ \$$$$$$$\\$$$$$$  \$$$$$$$ \$$$$$$$\$$ |                                                    
 \______/ \______/       \________\__|  \__|\_______|\______/ \_______|\_______\__|                                                    

"""

# Print the ASCII art at the start of the script
print(ascii_art)


def url_encode(char):
    return urllib.parse.quote(char)


def to_hexadecimal(char):
    return format(ord(char), 'x')


def to_unicode(char):
    return f'\\u{ord(char):04x}'


def to_octal(char):
    return format(ord(char), 'o')


def to_hex_numeric(char):
    return f'&#x{ord(char):x};'


def to_decimal(char):
    return str(ord(char))


def to_base64(char):
    return base64.b64encode(char.encode()).decode()


def encode_characters(choice, characters):
    encoding_functions = {
        '1': url_encode,
        '2': to_hexadecimal,
        '3': to_unicode,
        '4': to_octal,
        '5': to_hex_numeric,
        '6': to_decimal,
        '7': to_base64,
    }
    encode_func = encoding_functions.get(choice)
    if encode_func:
        return [encode_func(char) for char in characters]
    return characters


def main():
    user_input = input("Enter your JavaScript code: ")
    while True:
        characters = list(user_input)
        print("Splitted input: ", characters)

        print("Choose an encoding method:")
        print("1. URL Encoding")
        print("2. Hexadecimal")
        print("3. Unicode")
        print("4. Octal")
        print("5. Hexadecimal Numeric Character")
        print("6. Decimal")
        print("7. Base64")
        print("8. Custom Encoding Sequence")

        encoding_choice = input("Enter the number of your choice: ")

        if encoding_choice == '8':
            sequence = input("Enter the sequence of encoding methods (e.g., '132' for URL -> Hexadecimal -> Unicode): ")
            for method in sequence:
                num_to_encode = int(
                    input(f"How many characters do you want to encode with method {method}? (1-{len(characters)}): "))
                indices_to_encode = []
                for _ in range(num_to_encode):
                    index = int(
                        input(f"Enter the index (0-{len(characters) - 1}) of the character you want to encode: "))
                    indices_to_encode.append(index)
                for index in indices_to_encode:
                    if index < len(characters):
                        characters[index] = encode_characters(method, [characters[index]])[0]
        else:
            num_to_encode = int(input(f"How many characters do you want to encode? (1-{len(characters)}): "))
            indices_to_encode = []
            for _ in range(num_to_encode):
                index = int(input(f"Enter the index (0-{len(characters) - 1}) of the character you want to encode: "))
                indices_to_encode.append(index)
            for index in indices_to_encode:
                if index < len(characters):
                    characters[index] = encode_characters(encoding_choice, [characters[index]])[0]

        user_input = ''.join(characters)
        print(f"Current encoded result: {user_input}")

        continue_choice = input("Do you want to continue encoding? (Yes/No): ")
        if continue_choice.lower() != 'yes':
            break

    print(f"Final encoded result: {user_input}")


if __name__ == "__main__":
    main()
