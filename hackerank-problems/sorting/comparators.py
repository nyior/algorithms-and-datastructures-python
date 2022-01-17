""""
   Comparators are used to compare two objects. 
   In this challenge, you'll create a comparator and use it to sort an array. 
   The Player class is provided in the editor below. It has two fields:
   1. name: String
   2. score: integer

   Given an array of  Player objects, write a comparator that sorts them in order of decreasing score. 
   If  or more players have the same score, sort those players alphabetically ascending by name. 
   
"""

class Player:
 
    # we have 2 instance variables - name and age
    def __init__(self, name, age):
        self.name = name
        self.score = score
 
    # we have to define the 'less than' function to let Python know how to interpret the < operator
    # when we use < then Python calls this function to decide what object is smaller and what is greater
    def __lt__(self, other):
        if other.score == self.score: # If they have thesame score, sort based on name
            return self.name > other.name

        return self.score < other.score

    # string representation of the object (when we use the print() function then this function is called)
    def __repr__(self):
        return f"{self.name}: {self.score}"
 
 
# we can use the exact same insertion sort algorithm we have implemented
def insertion_sort(players):
 
    for i in range(len(players)):
 
        j = i
 
        while j > 0 and players[j - 1] < players[j]:
            players[j], players[j-1] = players[j-1], players[j]
            j = j - 1
 
 
if __name__ == '__main__':
 
    n = [
            Player('Adam', 23), 
            Player('Becca', 17),
            Player('Ana', 18), 
            Player('Ana', 17),  
            Player('Kevin', 32),
            Player('Daniel', 37)
        ]
    insertion_sort(n)
    print(n)

# TODO: understand the cmp_to_key from functools in Python