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
    w1 = .7
    w2 = .3

    return (fuzz1 * w2) + (fuzz2 * w1)



with open('games.csv', mode = 'r') as file:
    game_title = input("Enter a game: ").lower()
    csvFile = csv.reader(file)
    for line in csvFile:
        if fuzz_match(game_title, line[0]) >= 70:
            print(f"{line[0]} for {line[3]} is worth ${line[1]}!")
            print(fuzz_match(game_title, line[0]))
            