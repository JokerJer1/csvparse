import csv
from thefuzz import fuzz, process

'''
with open('games.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        print(line[0])
'''

def fuzz_match(str1, str2):
    fuzz1 = fuzz.ratio(str1, str2)
    fuzz2 = fuzz.partial_ratio(str1, str2)
    w1 = .9
    w2 = .1

    return (fuzz1 * w2) + (fuzz2 * w1)


def game():
    with open('games.csv', mode = 'r') as file:
        game_title = input("Enter a game: ").lower()
        csvFile = csv.reader(file)
        for line in csvFile:
            if fuzz_match(game_title, line[0]) >= 70:
                print(f"\n{line[0]} for {line[3]} is worth ${line[1]}!\n")
        try2 = input("Would you like to try another title? y/n : ")
        if try2 == 'y':
            game()
        else:
            print("Thanks for using Game Parser!")
            return
        
game()

