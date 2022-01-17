# Schuyler Sloman
from collections import deque
import time
import pickle 
import config
import random
import math
import sys
sys.stdout.write("loading dictionary ... \n\n")

class BoggleBoard:
    def __init__(self, dimension, letters, trie):
        self.trie = trie 
        self.dimension = dimension
        self.letters = letters
        self.letter_dict = {} 
        self.indx_keys = []
        self.answers = set()
        self.pop_dict()
        self.paths()
    
    def pop_dict(self):
        count = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.indx_keys.append((i,j))
                if self.letters[count] == "q":
                    self.letters[count] = "qu"
                self.letter_dict[(i,j)] = self.letters[count]
                count += 1
        return 
    
    def find_adjacent(self, node):
        (i,j) = node
        adj = []
        for r in range(-1,2):
            for c in range(-1,2):
                if r == 0 and c == 0:
                    pass
                elif -1 < (i + r) < self.dimension and -1 < (j + c) < self.dimension:
                    adj.append((i + r, j + c))
        return adj

    def paths(self):
        for i,j in self.indx_keys:
            initial_letter = self.letter_dict[(i,j)]
            initial_node = self.trie.root.children[initial_letter]
            initial_set = {(i,j)}
            start = (initial_letter, initial_node, initial_set, (i,j))
            curr_found_q = deque([start]) # word, node, set, lastseen
            while curr_found_q:
                (word, trie_node, set_seen, last_seen) = curr_found_q.popleft()
                if trie_node.is_word and word not in self.answers and len(word) >= 3:
                    self.answers.add(word)
                if trie_node.is_end():
                    continue
                adj = self.find_adjacent(last_seen)
                for r,c in adj:
                    if (r,c) not in set_seen and self.letter_dict[(r,c)] in trie_node.children:
                        new_set = set_seen.copy()
                        new_set.add((r,c))
                        letter = self.letter_dict[(r,c)]
                        next_node = trie_node.children[letter]
                        curr_found_q.append((word + letter, next_node, new_set, (r,c)))

def joinHelper(s1,s2):
    s1.update(s2)
    return s1

def joinSets(listOfSets):
    if len(listOfSets) == 0:
        return {}
    if len(listOfSets) == 1:
        return listOfSets[0]
    else:
        mid = len(listOfSets)//2
    return joinHelper(joinSets(listOfSets[:mid]), joinSets(listOfSets[mid:]))

def makeRandomboard(dim=4, letters=config.dice):
    toReturn = []
    n = (dim*dim)
    for _ in range(n):
        die = random.randint(0, len(letters) - 1)
        face = random.randint(0, 5)
        add = letters[die][face]
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

if __name__ == '__main__':

    pickle_file = open(config.pickle_file_name, 'rb') 
    trie = pickle.load(pickle_file)

    dim = int(input("Please choose board dimension: "))
    sys.stdout.write("\n")

    randBoard = makeRandomboard(dim)
    printBoggleBoard(randBoard)
    sys.stdout.write("\n")

    input("press ENTER when you want the answers...")
    t = time.process_time() 
    boggle = BoggleBoard(dim, randBoard, trie)
    elapsed_time = round(time.process_time() - t, 5)

    print(sorted(boggle.answers, key=len))
    sys.stdout.write(f"\n solved in {elapsed_time} seconds\n")

# test the time:
# python -m cProfile -s "cumulative" boggle_2022.py
# """
