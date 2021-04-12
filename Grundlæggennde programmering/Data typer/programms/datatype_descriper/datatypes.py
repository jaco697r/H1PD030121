import sys

def datatype_size():
    print('Write Something To Check Variable Bytes:')
    user_input = input()
    try:
        user_input = int(user_input)
    except:
        print('Not int')
        try:
            user_input = float(user_input)
        except:
            print('not float')
            try:
                user_input = str(user_input)
            except:
                print('not str')
                try:
                    user_input = list(user_input)
                except:
                    print('not any known data type')


    print('Variable Type = {} Number of bytes = {}'.format(type(user_input), sys.getsizeof(user_input)))
    print('This data type can hold {} different numbers'.format(2**sys.getsizeof(user_input)))

    if input('Press b and enter to try again: \n') == 'b':
        datatype_size()


datatype_size()