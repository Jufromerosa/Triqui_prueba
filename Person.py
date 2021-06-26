class Person:

    def __init__(self):
        self.bot_on = False
    
    #Set
    def set_bot_status(self, status):        
        self.bot_on = status
    #Get
    def get_bot_status(self):
        return self.bot_on


class Player(Person):

    __turns = []
    __last_round = 1    

    def __init__(self, name='', sign=''):
        Person.__init__(self)
        self.__sign = sign
        self.__player_is_bot = False
        if name == '':            
            name = 'BOT'
            self.__player_is_bot = True
            Person.set_bot_status(self,True)            

        self.__name = name
        self.__moves = []

    def switch_round(self):
        print("switched")
        if self.__last_round == 1:
            self.__last_round = 2
        else:
            self.__last_round = 1

    #Set
    def set_name(self, name):
        self.__name = str(name)

    def set_sign(self, sign):
        self.__sign = sign

    def set_move(self, move):
        if move in range(1, 9):
            self.__moves.append(move)
            self.set_turn_p(move)

    def set_turn_p(self, turn):
            self.__turns.append(turn)
    
    #Get
    def get_if_player_bot(self):
        return self.__player_is_bot

    def get_name(self):
        return self.__name

    def get_sign(self):
        return self.__sign

    def get_moves(self):
        return self.__moves

    def get_last_round(self):
        return self.__last_round

    def get_turns(self):
        return self.__turns