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
    save_secret = "132" 
    while lifes != 0:
        user_guess = "123"
        z = 0
        lifes-=1
        for x in user_guess:
            
            if (x in (save_secret)):
                toques += 1
                print(toques)
                if user_guess[0] == save_secret[0]:
                    famas += 1
                            
                    


            
                
                        
        print(f"Toques: {toques} Famas: {famas} user {user_guess} code{save_secret}")
        toques = 0
        famas = 0



print(user())
    
# def start_game():
#     return check_toques()

# print(start_game())

