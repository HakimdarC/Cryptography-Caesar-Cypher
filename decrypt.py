def caesar_decrypt(key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    n=len(message)
    decrypt_message = ""
    for i in range(n):
        lett = message[i]
        char_pos = alphabets.find(lett)
        new_loc = (char_pos - key) % 26
        decrypt_message += alphabets[new_loc]
    print(decrypt_message)
message = input("Enter your message: ")
key = int(input("Enter the key:"))
caesar_decrypt(key)



