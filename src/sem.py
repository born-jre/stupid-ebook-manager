#!/usr/bin/python3

import os
import hashlib, json

def __init_():
    pass

AUTOCHECK = False

class Sem(object):
    
    def __init__(self):
        self.dirs = ['/run/media/bing/stuff/dl']
        self.hashgraph = {} 
        """{
            "hashXXXXX": {
                "info": { "name": myname, "blocked":False, "fav":True },
                "dirs": [location1, location2],
            }
        }"""
        if(AUTOCHECK):
            self.update_database()
            self.write_to_disk('../myhashmap.json')
    def add_dir(self, d):
        self.dirs.append(d)
    
    def update_database(self):
        templist = []
        for d in self.dirs:
            templist +=  self.recursiveRead(d)
        for i in templist:
            value = self.generateHash(i[0])
            if value in self.hashgraph:
                tmp = self.hashgraph[value]['dirs'] + i[1]
                self.hashgraph[value] = { 'dirs':tmp, 'info': { 'name': i[0]}}
            else:
                self.hashgraph[value] = { 'dirs':i[1], 'info': { 'name': i[0]}}
        #self.hashgraph = self.byteify(self.hashgraph)

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
            json.dump(self.hashgraph, f) #ensure_ascii=True)
    
    def read_from_disk(self, path):
        with open(path, 'r') as f:
            self.hashgraph = json.load(f)
    def get_hashgraph(self):
        return self.hashgraph


    # def save_config(self):
    #     with open('../setting.json', 'w') as f:
    #         json.dump(self.config, f)
    
    # def restore_config(self):
    #     with open('../setting.json', 'r') as f:
    #         self.config = json.load(f)

#https://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-from-json
    # def byteify(self, input):
    #     if isinstance(input, dict):
    #         return {self.byteify(key): self.byteify(value) for key, value in input.iteritems()}
    #     elif isinstance(input, list):
    #         return [self.byteify(element) for element in input]
    #     elif isinstance(input, unicode):
    #         return input.encode('utf-8')
    #     else:
    #         return input