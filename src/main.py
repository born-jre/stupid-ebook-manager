import sem
import os


ebookList = []

path = os.path.abspath('.')
s = sem.Sem()
s.add_dir(path)
s.update_database()
s.write_to_disk('../myhashmap.json')