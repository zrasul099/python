from day7.step3.main import word_len

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]

    print(f"The encoded text is: {cipher_text}")

# Example usage:
#encrypt(original_text=text,shift_amount=shift)

def decrypt(original_text,shift_amount):
    output_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"The encoded text is: {output_text}")


def ceaser(original_text,shift_amount,encoder_or_decoder):
    output_text = ""
    for letter in original_text:


        if letter not in alphabet:
            output_text +=letter
        else:
            if encoder_or_decoder == "decode":
                shift_amount *=-1

            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"The encoded text is: {output_text}")
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(original_text=text,shift_amount=shift, encoder_or_decoder=direction)
    print()

#decrypt(original_text=text,shift_amount=shift)