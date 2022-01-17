import pickle
import config 

class TrieNode:
        def __init__(self, letter):
            self.letter = letter
            self.children = {}
            self.is_word = False
        
        def is_end(self):
            return len(self.children) == 0

class Trie:
    def __init__(self):
        self.root = TrieNode('')
    
    def add_word(self, word):
        node = self.root
        i = 0
        while i < len(word):
            letter = word[i]
            if i < (len(word) - 1) and (word[i:i + 2]) == "qu":
                letter = "qu"
                i += 1
            if letter in node.children:
                node = node.children[letter]
            else:
                node.children[letter] = TrieNode(letter)
                node = node.children[letter]
            i += 1
        node.is_word = True

    def check_word_from_string(self, word):
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return (False, None)
        return (node.is_word, node)

    def has_children_n(self, node):
        assert(isinstance(node, TrieNode))
        return len(node.children) != 0
    
    def has_children_s(self, word):
        assert(isinstance(word, str))
        is_word, node = self.check_word(word)
        if node:
            return node.children
        else:
            return -1

    def add_dict(self, filename):
        for line in open(filename):
            word = line.strip()
            self.add_word(word)

# myTrieTree = Trie()
# myTrieTree.add_dict(config.dict_file_name)

# filehandler = open(config.pickle_file_name, 'wb') 
# pickle.dump(myTrieTree, filehandler)