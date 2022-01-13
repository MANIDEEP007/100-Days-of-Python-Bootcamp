'''
Casear Cipher to encode or decode by a given shift
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
            'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  #If decode, shift backwards
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #Logic to handle symbols, numbers, spaces
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#Print ASCII art for Logo
from Cipher_Art import logo
print(logo)


choice = "yes"

#Run Program Until user want to exit
while choice == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #Using Modulus to handle large shifts
  caesar(text,shift%26,direction)
  choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
  if choice == "no":
    print("Good Bye")
