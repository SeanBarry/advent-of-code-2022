if __name__ == '__main__':
    wins = {'X':'C','Y':'A','Z': 'B'}
    draws = {'X':'A','Y':'B','Z':'C'}

    with open('./data.txt') as data:
        score = 0

        for game in [line.rstrip().split(' ') for line in data]:
            them, us = game
            score += list(wins.keys()).index(us) + 1

            if wins[us] == them:
                score += 6
            elif draws[us] == them:
                score += 3

        print(f'Total Score: {score}')
        
