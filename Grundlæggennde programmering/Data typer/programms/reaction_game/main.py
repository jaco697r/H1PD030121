from random import randrange
import time
import readkeys
import os

class game():
    def start_game(self):
        clear = lambda: os.system('cls')
        clear()
        print('Welcome to the greatest game ever made!')
        print('After you start the game, be ready to press any key as fast as you can when the next message appears')
        print('Press a to start the game: ')
        try:
            user_input = readkeys.getch()
            if user_input == 'a' or user_input == 'A':
                print('Wait for it')
                self.sleep()
                print('PRESS ANY KEY NOW')
                start = time.time()
                key = readkeys.getch()
                if key:
                    end = time.time()
                    if end - start < 0.01:
                        print('You are a cheating bastard!')
                    else:
                        print("Well Done! You did it in {} seconds".format(end - start))
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

self = game()

while self.start_game():
    self.start_game()
