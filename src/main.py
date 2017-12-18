import sem
import os


ebookList = []

path = os.path.abspath('.')
s = sem.Sem()
s.add_dir(path)
#s.update_database()
#s.write_to_disk('../myhashmap.json')

s.read_from_disk('../myhashmap.json')
s.print_hashmap()
#tmp = s.hashgraph['5fc8f55ce79f54e3f27a5acb44ee2098cca5c5a0']
#print(tmp['dirs'])



