count = 0

def create_file(msg):
    desktop_path = '/Users/hyh/Desktop/temp/'
    for count in range(1, 11):
        full_path = desktop_path + 'file' + str(count) + '.txt'
        file = open(full_path, 'w')
        file.write(msg)
        file.close()
        count = count + 1

create_file('hello')
