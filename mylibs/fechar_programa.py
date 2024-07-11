import keyboard


comando = True

def fechar():
    print('Pressione "F" para fechar...')
    while comando:
        if keyboard.is_pressed('f'):
            break