import csv

'''
with open('games.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        print(line[0])
'''

with open('games.csv', mode = 'r') as file:
    game_title = input("Enter a game: ")
    csvFile = csv.reader(file)
    for line in csvFile:
        if game_title in line:
            print(f"The game {line[0]} is worth ${line[1]}!")