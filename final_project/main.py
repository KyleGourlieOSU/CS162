import time
from final_project import main

#recursion is used here as input validation
def _main_function_():
    will = str(input('Do you Want to Execute NSP Timecard Program (y/n):'))
    if will.lower() == 'y':
        print('Executing Program...')
        time.sleep(0.5)
        main()
    elif will.lower() == 'n':
        print('Exiting...')
        time.sleep(0.5)
        exit()
    else:
        print('Invalid Option. Try Again')
        time.sleep(0.5)
        _main_function_()

if __name__ == "__main__":
    _main_function_()