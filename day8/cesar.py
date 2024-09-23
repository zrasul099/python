alphabet = ['a','b','c','d','e','f','g','h','k','j','i','l','m','n','o','p','r','s','t','u','v','w','y','z','x','q']
direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n" ).lower()
text = input("Type your message:\n").lower()
shipt = int(input("Type the shift number:\n"))

def encrypt(original_text,shipt_amount ):
   for letter in original_text:
       alphabet.index(letter)

print()
print()
print()