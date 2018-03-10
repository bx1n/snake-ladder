import socket

BUFFER_SIZE = 1024
MESSAGE = '{"player_count":3,"board_dimension":6,"ladders":{"19":24,"27":34,"28":31,"32":33},"snakes":{"6":5,"11":8,"30":29,"35":17},"die_tosses":{"1":{"1":5,"2":1,"3":5},"2":{"1":5,"2":1,"3":6},"3":{"1":5,"2":3,"3":3},"4":{"1":4,"2":1,"3":5},"5":{"1":1,"2":3,"3":3},"6":{"1":6,"2":6,"3":6},"7":{"1":3,"2":6,"3":3},"8":{"1":5,"2":3,"3":4},"9":{"1":1,"2":4,"3":3},"10":{"1":1,"2":2}}}\n'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostname()
port = 8080
s.connect((ip, port))

s.send(MESSAGE)

data = s.recv(BUFFER_SIZE)
print data


data = s.recv(BUFFER_SIZE)
print data

s.close()
