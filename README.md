# Boggle-Solver
solves n x n boggle board

Here I developed an algorithm to efficiently find all valid words in a boggle board.
I used the "dict_new.txt" file as my dictionary of more than two hundred thousand words. 
I have then created a dictionary which holds the index of where to find any word starting 
with some two or three letter combination. Then I can easily search a slice of the dictionary
to see if there are any words starting with a certain letter combination.

Run the program with "quick_solver.py" which will create a boggle board of dim x dim. 
Once yoou press ENTER, the valid answers found in the dictionary will be printed.

