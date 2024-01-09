#Q4

def encrypt_message():
    message = input("Enter a message: ")
    encrypted_message = message.replace(" ", "")[::-1]
    print("The encrypted message is: %s" % encrypted_message)

encrypt_message()