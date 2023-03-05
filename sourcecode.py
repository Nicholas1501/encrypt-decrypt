def ceaser(text: str, key: int, encrypted: bool) -> str:
    key = key % 26
    output_text = ''

    for char in text:
        #if character is not a letter, continue
        if not char.isalpha():
            output_text += char
            continue

        #find the position of char from 0 to 25
        char_index = ord(char) - 97 if char.islower() else ord(char) - 65

        #if we need to decript the text, new_char will be 'key' letters back
        #else, 'key' letters forward
        new_char_index = (char_index - key) % 26 if encrypted else (char_index + key) % 26
        new_char_ascii = new_char_index + 97 if char.islower() else new_char_index + 65
        new_char = chr(new_char_ascii)

        #add generated char to the output_text
        output_text += new_char

    return output_text

def main():
    pass

if __name__ == '__main__':
    print('')
    main()