from random import randint


number_length = 3
# int(input("Set the length of your code: "))
secret_number = []


def random_number():
    return randint(1, 9)

def secret_code():
    while (len(secret_number) < number_length):
        current_number = random_number() 
        if (current_number not in secret_number):
            secret_number.append(current_number)
    return secret_number

def user():
    lifes = number_length
    toques = 0
    famas = 0
    save_secret = secret_code()
    y=1
    while lifes != 0:
        user_guess ="123" 
        #input("Ingresa un numero: ")
        lifes-=1
        for x in user_guess:
    
            if (x in str(save_secret)):
                toques += 1

            else:
                index = []
                for z in range(len(user_guess)):
                    for i in range(len(save_secret)):
                        if str(user_guess[z]) == str(save_secret[i]):
                            famas += 1
                        
        print(f"Toques: {toques} Famas: {famas} user {user_guess} code{save_secret}")
        toques = 0
        famas = 0



print(user())
    
# def start_game():
#     return check_toques()

# print(start_game())

