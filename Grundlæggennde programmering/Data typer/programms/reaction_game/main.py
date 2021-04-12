from random import randrange
import time
import readkeys
import os

class game():

    multiplayer_mode = False
    player_1_name = 'you'
    keys_to_press = 'ANY KEY'
    end_message = "Good Job!"

    def start_game(self):
        self.clear_console()
        user_input = input('Welcome to the greatest game ever made!\n Enter m for multiplayer mode. Enter any other key for single player: ')
        # If multiplayer, set variables.
        if user_input == 'm' or user_input == 'M':
            self.multiplayer_mode = True
            self.player_1_name = 'Player 1'
            self.keys_to_press = 'A OR L'
        self.clear_console()
        print(self.player_message())
        print('Press A to start the game: ')
        # Has to be try exception block because program would crash if input was any non ascii char (for example arrow up)
        return self.play_game()

    def play_game(self):
        while True:
            try:
                user_input = readkeys.getch()
                if user_input == 'a' or user_input == 'A':
                    self.clear_console()
                    print('Wait for it')
                    self.sleep()
                    print('PRESS {} NOW'.format(self.keys_to_press))
                    start = time.time()
                    key = readkeys.getch()
                    end = time.time()
                    if key == 'a' or key == 'A':
                        if end - start < 0.01:
                            print('{} cheating bastard!. Do not press A before the message appears'.format(self.player_1_name + ' is a'))
                        else:
                            print("{} did it in {} seconds".format(self.player_1_name, end - start))
                    elif key == 'l' or key == 'L' and self.multiplayer_mode == True:
                        if end - start < 0.01:
                            print('Player 2 is a cheating bastard!. Do not press L before the message appears')
                        else:
                            print("Player 2 wins! You did it in {} seconds".format(end - start))
                    else:
                        self.end_message = "You didn't press the correct key"
                    user_input = input("{} Enter A to continue. Enter any other key to exit game".format(self.end_message))
                    if user_input == 'a' or user_input == 'A':
                        self.reset_variables()
                        self.start_game()
                    else:
                        print('You entered another key. GG and Goodbye!')
                        quit()
            except Exception as e:
                print('Wrong button. Try again')

    def sleep(self):
        time.sleep(randrange(2, 7))

    def player_message(self):
        if not self.multiplayer_mode:
            return 'Singleplayer mode active. \nAfter you start the game, be ready to press any key as fast as you can when the next message appears'
        else: return 'Multiplayer mode active. \nPlayer 1, be ready to press A. Player 2, be ready to press L - after the next message'

    def clear_console(self):
        clear = lambda: os.system('cls')
        clear()

    # If players goes from multiplayer to single player in the same instance of the class. Variables has to be reset.
    def reset_variables(self):
        self.multiplayer_mode = False
        self.player_1_name = 'you'
        self.keys_to_press = 'ANY KEY'
        self.end_message = "Good Job!"

self = game()
# run game until start_game() returns False
while self.start_game():
    self.start_game()
