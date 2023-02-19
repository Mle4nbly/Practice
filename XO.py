class XOgame:
    def __init__(self):
        self.ground = {
            1: 1, 2: 2, 3: 3,
            4: 4, 5: 5, 6: 6,
            7: 7, 8: 8, 9: 9
        }

        self.win_combos = [
            [1,2,3],[4,5,6],[7,8,9],
            [1,4,7],[2,5,8],[3,6,9],
            [3,5,7],[1,5,9]
        ]

        self.winner = 0

    def show_ground(self):
        print(
            f" _____ _____ _____ \n"
            f"|     |     |     |\n"
            f"|  {self.ground[1]}  |  {self.ground[2]}  |  {self.ground[3]}  |\n"
            f"|_____|_____|_____|\n"
            f"|     |     |     |\n"
            f"|  {self.ground[4]}  |  {self.ground[5]}  |  {self.ground[6]}  |\n"
            f"|_____|_____|_____|\n"
            f"|     |     |     |\n"
            f"|  {self.ground[7]}  |  {self.ground[8]}  |  {self.ground[9]}  |\n"
            f"|_____|_____|_____|"
            )
        
    def x_player(self, choice_x: int):
        while self.ground[choice_x] != 'X':
            if choice_x in self.ground.keys() and self.ground[choice_x] == choice_x:
                self.ground[choice_x] = 'X'
            elif choice_x in self.ground.keys() and self.ground[choice_x] != choice_x:
                choice_x = int(input('На этой клетке уже поставлена отметка, выберите другую:'))
            else:
                choice_x = int(input('Выбирайте из доступных вариантов'))
            
        for win_combo in self.win_combos:
            combo = []
            for key in self.ground.keys():
                if self.ground[key] == 'X':
                    combo.append(key)
            counter = 0
            for x in win_combo:
                if x in combo:
                    counter += 1
            if counter == 3:
                self.winner = 'X-player победил'
                print(self.winner)
                xo.show_ground()
        
    def o_player(self, choice_o: int):
        while self.ground[choice_o] != 'O':
            if choice_o in self.ground.keys() and self.ground[choice_o] == choice_o:
                self.ground[choice_o] = 'O'
            elif choice_o in self.ground.keys() and self.ground[choice_o] != choice_o:
                choice_o = int(input('На этой клетке уже поставлена отметка, выберите другую:'))
            else:
                choice_o = int(input('Выбирайте из доступных вариантов:'))

        for win_combo in self.win_combos:
            combo = []
            for key in self.ground.keys():
                if self.ground[key] == 'O':
                    combo.append(key)
            counter = 0
            for x in win_combo:
                if x in combo:
                    counter += 1
            if counter == 3:
                self.winner = 'O-player победил'
                print(self.winner)
                xo.show_ground()
                    
if __name__ == '__main__':
    counter = 0
    xo = XOgame()
    while xo.winner == 0:
        xo.show_ground()
        choice_x = input('Ваш символ - X, выберите позицию на поле, куда хотели бы поставить символ:')
        xo.x_player(choice_x=int(choice_x))
        counter += 1
        if counter == 9:
            print('Ничья')
            xo.show_ground()
            break
        if xo.winner == 'X-player победил':
            break
        else:
            xo.show_ground()
            choice_o = input('Ваш символ - O, выберите позицию на поле, куда хотели бы поставить символ:')
            xo.o_player(choice_o=int(choice_o))
            counter += 1
            if counter == 9:
                xo.show_ground()
                print('Ничья')
                break 