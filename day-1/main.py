if __name__ == '__main__':
    with open('./data.txt') as data:
        data =  data.readlines()

        max_calories = float('-inf')
        current_total = 0

        for line in data:
            if line == '\n':
                max_calories = max(current_total, max_calories)
                current_total = 0
                continue

            current_total += int(line.strip())

        print('max', max_calories)


            
