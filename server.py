import socket
import json

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostname()
port = 8080
soc.bind((ip, port))

soc.listen(5)

while True:
    con, ip = soc.accept()
    data = con.recv(1024)

    data = json.loads(data)
    #computaion
    end = data['board_dimension'] * data['board_dimension']
    ladd = data['ladders']
    snake = data['snakes']

    cnt = data['player_count']
    pos = {}
    #dic to map position of user
    for i in range(1,cnt+1):
        pos[i] = 0


    for key, value in data['die_tosses'].iteritems():
        for k, v in value.iteritems():
            pos[int(k)]=int(pos[int(k)])+int(v)

    print pos
    # for i,j in pos:
    #     print i, j


    con.close()
