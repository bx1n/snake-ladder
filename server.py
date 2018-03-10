import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostname()
port = 8080
s.bind((ip, port))

s.listen(5)


while 1:
    con, ip = s.accept()
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

    ladd = {int(k): int(v) for k, v in ladd.items()}
    snake = {int(k): int(v) for k, v in snake.items()}

    for key, value in data['die_tosses'].iteritems():
        for k, v in value.iteritems():
            k=int(k)
            pos[k] = int(pos[k]) + int(v)
            if ladd.get(pos[k]):
                con.send('Player ' + str(k) + " got a ladder at " + str(pos[k]) + ' to ' + str(ladd.get(pos[k])) + '\n')
                pos[k] = ladd.get(pos[k])

            if snake.get(pos[k]):
                con.send('Player ' + str(k) + " got a snake at " + str(pos[k]) + ' to ' + str(snake.get(pos[k])) + '\n')
                pos[k] = snake.get(pos[k])

            if pos[k] == 100:
                print 'Player '+str(k)+' won'


    con.close()
