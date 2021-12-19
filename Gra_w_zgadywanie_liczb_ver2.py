def user_input():
    possible_input = ["malo", "duzo", "wygrales"]
    while True:
        user_answer = input().lower()
        if user_answer in possible_input:
            break
        print("Input is not in ['malo', 'duzo', 'wygrales']")
    return user_answer


def guess_the_number():
    print("Wybierz liczbę od 0 do 1000!")
    print("Wcisnij 'Enter' by przejsc dalej")
    input()
    min_number = 0
    max_number = 1000
    user_answer = ""
    while user_answer != "wygrales":
        guess = (max_number - min_number) // 2 + min_number
        print(f"Twoja liczba to: {guess}")
        user_answer = user_input()
        if user_answer == "duzo":
            max_number = guess
        elif user_answer == "malo":
            min_number = guess

    return ("Mam Cie, WYGRALEM!")


print("Uzywaj operatorów: 'malo', 'duzo', 'wygrales'\n")
x = guess_the_number()
print(x)