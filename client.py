import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostname()
port = 8080

soc.connect((ip, port))
soc.send('{"player_count":3,"board_dimension":6,"ladders":{"19":24,"27":34,"28":31,"32":33},"snakes":{"6":5,"11":8,"30":29,"35":17},"die_tosses":{"1":{"1":5,"2":1,"3":5},"2":{"1":5,"2":1,"3":6}}}\n')
soc.close()
