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
    char_len = len(char)
    password = ""
    for i in range(0, pass_len):
        x = random.randint(0, char_len)
        password += string.printable[x]

    print(password)
    print("Password is save to password.txt file \n")
    with open("password.txt", mode="w") as pass_file:
        pass_file.write("\nCurrent Generated Password is : ")
        pass_file.write(password)
        pass_file.write("\n")


while True:
    try:
        pass_len = int(input("Enter Password Length : "))
        password_generator(pass_len)
    except ValueError:
        print("Invalid Input")
        print("\n")