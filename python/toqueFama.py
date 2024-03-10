from random import randint


number_length = 3
# int(input("Set the length of your code: "))
secret_number = []

def random_number():
    return randint(1, 9)

def check_number():
    while (len(secret_number) < number_length):
        current_number = random_number() 
        if (current_number not in secret_number):
            secret_number.append(current_number)
    return secret_number


def loop_game():
    lifes = number_length
    while lifes >= 1:
        user_guess = "123"
        
        lifes-=1

def start_game():
    print(random_number())
    print(check_number())
    print(loop_game())
    # lifes = number_length
    # famas = 0
    # i = 0
    # user_guess = "123" 
    # # input(f"Debes ingresar una secuencia {number_length} digitos: ")
    # while len(user_guess) != number_length :
    #     user_guess = "123"
    #     # input(f"Debes ingresar una secuencia {number_length} digitos, Intentalo nuevamente: ")
    #     if len(user_guess) == number_length:
    #         break
    
    # return user_guess;      
print(start_game())



