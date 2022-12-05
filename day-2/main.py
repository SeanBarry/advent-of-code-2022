def part_one(data):
    score = 0

    wins = {'X':'C','Y':'A','Z': 'B'}
    draws = {'X':'A','Y':'B','Z':'C'}
    # x lose, y draw, z win
    for game in data:
        them, us = game.split()
        score += list(wins.keys()).index(us) + 1

        if wins[us] == them:
            score += 6
        elif draws[us] == them:
            score += 3
    return score

        
def part_two(data):
    score = 0
    mapping = {"AX":3,"AY":4,"AZ":8,"BX":1,"BY":5,"BZ":9,"CX":2,"CY":6,"CZ":7}
    
    for game in data:
        fixture = game.replace(' ', '')

        score += mapping[fixture]
    return score

with open('./data.txt') as data:
    rounds = [line.rstrip() for line in data]
    one = part_one(rounds)
    two = part_two(rounds)

    print(f'Score for ONE is: {one}')
    print(f'Score for TWO is: {two}')

