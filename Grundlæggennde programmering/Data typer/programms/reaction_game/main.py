from random import randrange
import time
import readkeys
import os

class game():

    multiplayer_mode = False
    player_1_name = 'you'
    keys_to_press = 'ANY KEY'

    def start_game(self):
        clear = lambda: os.system('cls')
        clear()
        print('Welcome to the greatest game ever made!')
        if input('Press m and enter to for multiplayer mode. Enter any other key for single player: ') == 'm' or input == 'M':
            self.multiplayer_mode = True
            self.player_1_name = 'Player 1'
            self.keys_to_press = 'A OR L'

        clear()
        print(self.player_message())
        print('Press A to start the game: ')
        try:
            user_input = readkeys.getch()
            if user_input == 'a' or user_input == 'A':
                clear()
                print('Wait for it')
                self.sleep()
                print('PRESS {} NOW'.format(self.keys_to_press))
                start = time.time()
                key = readkeys.getch()
                end = time.time()
                if key == 'a' or key == 'A':
                    if end - start < 0.01:
                        print('{} cheating bastard!. Do not press a before the message appears'.format(self.player_1_name + ' is a'))
                    else:
                        print("Player 1 wins! You did it in {} seconds".format(end - start))

                if key == 'l' or key == 'L' and self.multiplayer_mode == True:
                    if end - start < 0.01:
                        print('Player 2 is a cheating bastard!. Do not press a before the message appears')
                    else:
                        print("Player 2 wins! You did it in {} seconds".format(end - start))

                input("Good job! Press any key and press enter to continue")
                print('Press a to try again. Press any other key to exit')
                user_input = readkeys.getch()
                if user_input == 'a' or user_input == 'A':
                    self.start_game()
                else:
                    print('You pressed another key. GG and Goodbye!')
                    return False
        except:
            print('Wrong button. Try again')

    def sleep(self):
        time.sleep(randrange(2, 7))

    def player_message(self):
        if not self.multiplayer_mode:
            return 'Singleplayer mode active. After you start the game, be ready to press any key as fast as you can when the next message appears'
        else: return 'Multiplayer mode active. Player 1, be ready to press A. Player 2, be ready to press L - after the next message'

self = game()

while self.start_game():
    self.start_game()
