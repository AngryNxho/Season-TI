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
    return str(secret_number)

def user():
    lifes = number_length
    toques = 0
    save_secret = secret_code()
    print(save_secret)
    while lifes != 0:
        user_guess = input("Ingresa un numero: ")
        lifes-=1
        for x in user_guess:
            if (x in save_secret):
                toques += 1
        print(f"Toques: {toques}")
        toques = 0

    return "hola"

print(user())
    
# def start_game():
#     return check_toques()

# print(start_game())

