# Schuyler Sloman

import random
import math
import sys

class Graph:
    def __init__(self, dimension):
        self.dimension = dimension
        self.node_array = ([[(i,j) for i in range(dimension)] for j in range(dimension)])
        self.dictionary = {}
        self.path = [[[(i,j)] for i in range (dimension) for j in range(dimension)]]
 
    def find_adj(self, node):
        adj = []
        (i,j) = node
        #bot right
        if (i+1) < self.dimension and (j+1) < self.dimension:
            adj.append((i+1,j+1))
        #top right
        if (i+1) < self.dimension and (j-1) > -1:
            adj.append((i+1, j-1))
        # top left
        if (i-1) > -1 and (j-1) > -1:
            adj.append((i-1, j-1))  
        # bot left
        if (i-1) > -1 and (j+1) < self.dimension:
            adj.append((i-1, j+1))
        #bot    
        if (j+1) < self.dimension:
            adj.append((i,j+1))       
        #top
        if (j-1) > -1:
            adj.append((i, j-1))
        #  left
        if (i-1) > -1:
            adj.append((i-1, j))
         # right   
        if (i+1) < self.dimension:
            adj.append((i+1, j))
        return adj

    def populate_dict(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.dictionary[(i,j)] = self.find_adj((i,j))   

    def get_node_num(self):
        #print(self.dictionary)
        return len(self.dictionary)
     
    def get_adj(self, node_num):
        return self.dictionary[node_num]
    

    def Paths(self):
        list_addition = []
        for i in self.path[0]:
            adj = self.get_adj(i[-1])
            for j in adj:
                if j not in i:
                    new_path = i[:]
                    new_path.append(j)
                    list_addition.append(new_path)
        if list_addition != []:
            self.path.append(list_addition)
        if len(self.path[-1][-1]) == self.get_node_num():
            return 
        return self.Paths()
        
class GoogleBoggle:
    def __init__(self, dimension, letters):
        self.dimension = dimension
        self.letters = letters
        self.graph = Graph(dimension)
        self.graph.populate_dict()
        self.letter_dict = {}
        self.answers = []
        self.pop_dict()
        self.Paths()
        
    def list2string(self, l: list):
        s = ""
        for i in l:
            s += i
        return s     

    def Paths(self):
        list_addition = []
        for i in self.graph.path[-1]:
            adj = self.graph.get_adj(i[-1])
            for j in adj:
                if j not in i:

                    new_path = i[:]
                    new_path.append(j)

                    string = self.list2string([self.letter_dict[i] for i in new_path])

                    if len(string) < 2:
                        list_addition.append(new_path)
                    
                    elif lookup_all(string):
                        list_addition.append(new_path)
                        if (is_a_word_all(string)) and (string not in self.answers):     
                            self.answers.append(string)
                            # print(string)

        if list_addition != []:
            self.graph.path.append(list_addition)
            return self.Paths()
        elif len(self.graph.path[-1][-1]) == self.graph.get_node_num():
            return
        else:
            return
    
    def pop_dict(self):

        nodes_to_list = []
        for i in range(self.dimension):
            for j in range(self.dimension):
                nodes_to_list.append((i,j))
            #[...(1,0),(1,1)...]        
        for i in range(len(self.letters)):
            self.letter_dict[nodes_to_list[i]] = self.letters[i]


def word_reader(filename):
    return [word.strip() for word in open(filename)]

word_dict = word_reader("./dict_new")
key = word_reader("./key.txt")
value = word_reader("./value.txt")
key2 = word_reader("./key2.txt")
value2 = word_reader("./value2.txt")

id_dict = dict(zip(key,value))
id_dict2 = dict(zip(key2, value2))

for key in id_dict:
    id_dict[key] = int(id_dict[key])

for key2 in id_dict2:
    id_dict2[key2] = int(id_dict2[key2])

id_dict_final = {**id_dict,**id_dict2}

id_dict_final["__"] = len(id_dict) - 1
id_dict_final["___"] = -1

def next_all(s):
    """
    finds the index of the next 2 or 3 letter entry
    i.e. if we want to find words starting with "ala",
    then we want to check where the indexes for "ala" and "alb" are
    """
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    if len(s) == 2: 
        if s[0:2] == "zz":
            return "__"
        first = alphabet.index(s[0])
        second = alphabet.index(s[1])
        if second == 25:
            s = alphabet[(first + 1)] + alphabet[1]
        else:
            s = alphabet[first] + alphabet[(second + 1)]
        return s
    elif len(s) >= 3:
        if s[0:3] == "zzz":
            return "__"
        first = alphabet.index(s[0])
        second = alphabet.index(s[1])
        third = alphabet.index(s[2])
        if (third == 25) and (second == 25):
            s = alphabet[(first + 1)] + alphabet[1] + alphabet[1]
        elif third == 25:
            s = alphabet[first] + alphabet[(second + 1)] + alphabet[1]
        else:
            s = alphabet[first] + alphabet[second] + alphabet[(third + 1)]
    return s

def lookup_all(s):
    """
    return True or False if s starts a word
    """
    if len(s) == 2:
        key = s
        if id_dict_final[key] == -1:
            return False
        else:
            key2 = next_all(s)
            while id_dict_final[key2] == -1:
                key2 = next_all(key2)

        for i in word_dict[id_dict_final[key]:id_dict_final[key2]]:
            if i.startswith(s):
                return True 
    elif len(s) >= 3:
        key = s[0:3]
        if id_dict_final[key] == -1:
            return False
        else:
            key2 = next_all(s)
            while id_dict_final[key2] == -1:
                key2 = next_all(key2)

        for i in word_dict[id_dict_final[key]:id_dict_final[key2]]:
            if i.startswith(s):
                return True 
    return False

def is_a_word_all(s):
    """
    return True or False if s is a word longer than 3 letters
    """

    if len(s) >= 3:
        key = s[0:3]
        if id_dict_final[key] == -1:
            return False
        else:
            key2 = next_all(s)
            while id_dict_final[key2] == -1:
                key2 = next_all(key2)

        if s in word_dict[id_dict_final[key]:id_dict_final[key2]]:
            return True 
    return False

alphabet = list('abcdefghijklmnopqrstuvwxyz')

def makeRandomboard(dim=4, letters=alphabet):
    toReturn = []
    n = (dim*dim)
    for _ in range(n):
        add = random.choice(letters)
        if add == "q":
            add += "u"
        toReturn.append(add)
    return toReturn

def printBoggleBoard(bList):
    n = len(bList)
    dim = round(math.sqrt(n))
    space = " "*3
    top = space + "—"*(3*dim)
    sys.stdout.write("  " + top + "\n")
    for i in range(0,n,dim):
        row = bList[i:i+dim]
        sys.stdout.write(space + "|  ")
        for l in row:
            sys.stdout.write(l.ljust(3))
        sys.stdout.write("|")
        sys.stdout.write("\n")
    sys.stdout.write("  " + top + "\n")
    
## INTERACTIVE SECTION
dim = int(input("Please choose board dimension: "))
sys.stdout.write("\n")

randBoard = makeRandomboard(dim)
printBoggleBoard(randBoard)
sys.stdout.write("\n")

input("press enter when you want the answers...")
boggle = GoogleBoggle(dim, randBoard)
print(boggle.answers)





"""
to test
randBoard = ["n", "a", "b", "a", "qu", "a", "u", "l", "y", "z", "v", "t", "i", "s", "v", "f"]

test the time:
python -m cProfile -s "cumulative" quick_solver.py
"""
