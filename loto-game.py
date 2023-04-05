import random

class the_card_class:
# что можно сделать с карточкой?
# generate_the_str_card - вытянуть карточку=сгенерировать
# print_the_card - вывести на экран
# cross_out_the_number - зачеркнуть элемент
# game_over - проверка на заполненость карточки

    def generate_the_str_card(self):
        random_number_all = random.sample([x for x in range(1, 91)], 15)

        random_number_all = [[str(x)+' '*random.sample([3,5],1)[0] if len(str(x))==1 else str(x)+' '*random.sample([2,4],1)[0]  for x in sorted(random_number_all[:5])],
                             [str(x)+' '*random.sample([3,5],1)[0] if len(str(x))==1 else str(x)+' '*random.sample([2,4],1)[0]  for x in sorted(random_number_all[5:10])],
                             [str(x)+' '*random.sample([3,5],1)[0] if len(str(x))==1 else str(x)+' '*random.sample([2,4],1)[0]  for x in sorted(random_number_all[10:15])]]


        return random_number_all

    def print_the_card(self, user_card, user, name_us = 'игрок_'):
        print('-' * 2 + name_us + '-' * 2)
        for rows_elements in user_card:
            null_list = ''
            for el in rows_elements:
                null_list += el
            print(null_list)
        print('-'*20)

    def game_over(self,user_card):
        check_0 = list(map(lambda st: str.replace(st, " ", ""), user_card[0]))
        check_1 = list(map(lambda st: str.replace(st, " ", ""), user_card[1]))
        check_2 = list(map(lambda st: str.replace(st, " ", ""), user_card[2]))
        check = set(check_0 + check_1 + check_2)
        return check

    def cross_out_the_number(self, user_card , user , cross, rand_int):
        '''
        :param user_card: исходная карточка
        :param user: 0 - компьютер
        :param cross: - (y)зачеркнуть или (n)нет
        :param rand_int: карточка с зачеркнутым или нет числом
        :return:
        '''
        check_0 = [x for x in list(map(lambda st: str.replace(st, " ", ""), user_card[0])) if x == str(rand_int)]
        check_1 = [x for x in list(map(lambda st: str.replace(st, " ", ""), user_card[1])) if x == str(rand_int)]
        check_2 = [x for x in list(map(lambda st: str.replace(st, " ", ""), user_card[2])) if x == str(rand_int)]
        check = check_0 + check_1 + check_2

        if (len(check)>0 ) and (user==0) :
            cross = 'y'
        elif (len(check)<0 ) and (user==0) :
            cross = 'n'

        if (len(check) > 0) and (cross == 'y'):
            for rows_elements in range(len(user_card)):
                for el in range(len(user_card[rows_elements])):
                    if str.replace(user_card[rows_elements][el], " ", "") == str(rand_int):
                        user_card[rows_elements][el] = "-" + ' ' * (len(user_card[rows_elements][el]) - 1)
            return user_card
        elif (len(check) <= 0) and (cross != 'y'):
            return user_card
        else:
            game_over = 'вы проиграли!'
            return game_over

# Играем
if __name__ == '__main__' :
    lg = the_card_class()
    user_1 = lg.generate_the_str_card()
    user_2 = lg.generate_the_str_card()

    us_1 = int(input('Выберете игрока 1: 1 - играет человек, 0 - играет компьютер'))
    us_2 = int(input('Выберете игрока 2: 1 - играет человек, 0 - играет компьютер'))
    name_us_1 = 'игрок 1 '
    name_us_2 = 'игрок 2 '
    lg.print_the_card(user_1, user = us_1, name_us = 'игрок 1 ')
    lg.print_the_card(user_2, user = us_2, name_us = 'игрок 2 ')

    #
    for i in random.sample([x for x in range(1, 91)], 90):
        print('Новый бочонок:',i)


        if us_1 != 0 : #если второй игрок не человек, то спрашиваем зачеркиает ли он карточку?
            cross_1 = input('Вопрос игроку 1 : Зачеркнуть? ответьте y/n')
        elif us_1 == 0:
            cross_1 = 0
        if us_2 != 0 : #если второй игрок не человек, то спрашиваем зачеркиает ли он карточку?
            cross_2 = input('Вопрос игроку 2 :Зачеркнуть? ответьте y/n')
        elif us_2 == 0:
            cross_2 = 0

        user_1 = lg.cross_out_the_number(user_1, user=us_1, cross=cross_1, rand_int=i)
        user_2 = lg.cross_out_the_number(user_2, user=us_2, cross=cross_2, rand_int=i)
        result_user_1 = lg.game_over(user_1)
        result_user_2 = lg.game_over(user_2)

        if len(result_user_1) ==1 :
            print('выйграл игрок 1!')
            break
        elif len(result_user_2) ==1 :
            print('выйграл игрок 2!')
            break
        elif 'вы проиграли!' == user_1:
            print('Игрок 1 проиграл!')
            break
        elif 'вы проиграли!' == user_2:
            print('Игрок 2 проиграл!')
            break
        elif 'вы проиграли!' != user_1:
            lg.print_the_card(user_1, user = us_1, name_us = 'игрок 1 ')
            lg.print_the_card(user_2, user = us_2, name_us = 'игрок 2 ')

#
