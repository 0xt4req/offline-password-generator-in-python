import random,string

print("############################################################")
print("#    Code For       : Offline Password Generator           #")
print("#    Code Language  : Python                               #")
print("#    Code Author    : Md. Tareq Ahamed Jony                #")
print("#    Member OF      : Knight Squad                         #")
print("#    Position       : Learner (Knight_VIII)                #")
print("#    Team           : Knight Squad                         #")
print("#    Team Leader    : Noman Prodhan                        #")
print("############################################################")
print("\n")

def password_generator(num):
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.+-*/~`!@#$%^&*()_|/,{}''[]:" # you can add more
    char_len = len(char) # length of the char variable
    password = "" # declearing an empty string
    for i in range(0, pass_len):
        x = random.randint(0, char_len) # to change the password randomly
        password += string.printable[x] # adding the characters to the password variable as string

    print(password)
    print("Password is save to password.txt file \n")
    with open("password.txt", mode="w") as pass_file: # creating a new .txt file to store the password 
        pass_file.write("\nCurrent Generated Password is : ") # writing on the file
        pass_file.write(password) # saving the password to the file
        pass_file.write("\n") # printing newline


while True: # to run the program as much as user wants
    try: # exception heandling 
        pass_len = int(input("Enter Password Length : "))
        password_generator(pass_len)
    except ValueError: # detecting error
        print("Invalid Input") # if user gives invalid input
        print("\n")
