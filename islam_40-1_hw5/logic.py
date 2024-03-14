from random import randint
from decouple import config



number_list = randint(1, 31)
game_over = True
my_money = config('MY_MONEY', default=1000, cast=int)


class Game:
    def input_money(self):
        while True:
            try:
                bet = int(input(f'Ваш баланс {my_money}\nВведите сумму ставки: '))
                if bet > my_money:
                    print('У вас не достаточно денег ')
                elif bet <= 0:
                    print('Отрицательное число не принимаеться')
                else:
                    return bet

            except ValueError:
                print('ERROR\nВведите коректное число')

    def input_slot(self):
        global number_list
        while True:
            try:
                user_num = int(input('Выберите слот от 1 до 31: '))
                if 1 <= user_num <= 10:
                    return user_num
                else:
                    print('Введите число от 1 до 31')
            except ValueError:
                print('Введите правльное число!')


    def play_game(self):
        global my_money, game_over
        while my_money > 0 and game_over:
            bet_money = self.input_money()
            bet_slot = self.input_slot()

            if bet_slot == bet_money:
                win_money = bet_money * 2
                print(f"You win {win_money}$")
                my_money -= bet_money
                my_money += win_money
            else:
                print(f"You lose {bet_money}")
                my_money -= bet_money



            if my_money != 0:
                while True:
                    contin = input(f'Ваш баланс {my_money}\nВы хотите продолжать игру ( да или нет )? ').lower()
                    if contin == 'нет':
                        print(f'GAME OVER')
                        game_over = False
                        break

                    elif contin == 'да':
                        break
                    else:
                        print('Введите да или нет')

            else:
                print(f'Ваш баланс {my_money}\nYOU LOOSE!\nHA HA HA ')




