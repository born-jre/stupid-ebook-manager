#!/usr/bin/python3

import os
import hashlib
import json

def __init_():
    pass

class Sem(object):
    
    def __init__(self):
        self.dirs = []
        self.hashgraph = {} 
        """{
            "hashXXXXX": {
                "info": { "name": myname, "blocked":False, "fav":True },
                "dirs": [location1, location2],
            }
        }"""
        self.pdflist = []

    def add_dir(self, d):
        self.dirs.append(d)
    
    def update_database(self):
        templist = []
        for d in self.dirs:
            templist +=  self.recursiveRead(d)
        for i in templist:
            value = self.generateHash(i[0])
            if value in self.hashgraph:
                tmp = self.hashgraph[value] + i[1]
                self.hashgraph[value] = tmp
            else:
                self.hashgraph[value] = i[1]

    def recursiveRead(self, path):
        ilist = []
        for i in os.listdir(path):
            newpath = os.path.join(path, i)
            if (os.path.isfile(newpath)):
                
                if (i.endswith(".pdf")):
                     ilist.append([i, [newpath]])
            
            if os.path.isdir(newpath):
                ilist = self.recursiveRead(newpath) + ilist
        return ilist
    def generateHash(self, value):
        #return value
        
        hash_object = hashlib.sha1(value.encode('utf_8'))
        #print(hash_object)
        return str(hash_object.hexdigest())

    def print_hashmap(self):
        print(self.hashgraph)
    
    def write_to_disk(self, path):
        with open(path, 'w') as f:
            json.dump(self.hashgraph, f)
    
    def read_from_disk(self, path):
        with open(path, 'r') as f:
            self.hashgraph = json.load(f)