def evaluate_calorie_count(count, top3):
    if count < top3[2]:
        return
    elif count > top3[0]:
        top3[2], top3[1], top3[0] = top3[1], top3[0], count
    elif count > top3[1]:
        top3[2], top3[1] = top3[1], count
    elif count > top3[2]:
        top3[2] = count

def part_two(data):
    top_three = [float('-inf') for i in range(3)]
    
    current_total = 0
    for line in data:
        if line == '\n':
            evaluate_calorie_count(current_total, top_three)
            current_total = 0
            continue

        current_total += int(line.strip())
            
    return top_three


if __name__ == '__main__':
    with open('./data.txt') as data:
        data =  data.readlines()
        
        top3 = part_two(data)

        print(f"Part One Answer: {top3[0]}")
        print(f"Part Two Answer: {sum(top3)}")

