print('if you need help enter h')
command=''
#to help in check the state of the car
start=False
stop=False
while True:
    command=input('> ')
    if command.lower()=='h':
        print('''
        enter s to run the car
        enter st to stop the car
        enter q to exit 
        ''')
        #.lower() to ensure that the program will will alweys check lower case of the char
    elif command.lower()=='s':
        if start:
            print('the car already running')
        else:
            print('go,running now')
            start=True
            stop=False
    elif command.lower()=='st':
        if stop:
            print('the car already stopped')
        else:
            print('stop now , stopped')
            stop==True
            start=False
    elif command.lower()=='q':
        break




