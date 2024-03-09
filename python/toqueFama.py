from random import randint


number_length = 9
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

def lopp_game():
    lifes = number_length
    toques = 0
    famas = 0
    save_number = check_number()
    while (lifes != 0):
        i = 0
        user_guess = input(f"Debes ingresar una secuencia {number_length} digitos")
        while len(user_guess) < number_length:
            user_guess = input(f"Debes ingresar una secuencia {number_length} digitos, Intentalo nuevamente: ")

        
        print(save_number)
        for x in user_guess:
            # print(x, str(save_number[i]))
            if (x in str(save_number)):
                toques+= 1
                print(toques)
            lifes -= 1

            i+=1
    return f"toques: {toques}"      
print(lopp_game())
