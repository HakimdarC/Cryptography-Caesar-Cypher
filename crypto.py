

def caesar_cypher(key):
    alphabets = "abcdefghijklmnopqrstuvwxyz" 
    message.lower()
    n=len(message)
    encrypt_message = ""
    for i in range(n):
        lett = message[i]
        char_pos = alphabets.find(lett)
        new_loc = (char_pos + key) % 26
        encrypt_message += alphabets[new_loc]
    return encrypt_message
     
message = input("Enter your message: ")
key = int(input("Enter the key:")) 
print("your encrypted message is: ")
print(caesar_cypher(key))

def caesar_decrypt(key):
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    message = caesar_cypher(key)
    n=len(message)
    decrypt_message = ""
    for i in range(n):
        lett = message[i]
        char_pos = alphabets.find(lett)
        new_loc = (char_pos - key) % 26
        decrypt_message += alphabets[new_loc]
    print("your original message is: ")
    print(decrypt_message)
caesar_decrypt(key)
