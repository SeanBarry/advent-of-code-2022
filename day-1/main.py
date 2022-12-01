from typing import List

def evaluate_calorie_count(count: int, top3: List[int]):
    if count <= top3[2]:
        return
    elif count > top3[0]:
        top3[2], top3[1], top3[0] = top3[1], top3[0], count
    elif count > top3[1]:
        top3[2], top3[1] = top3[1], count
    elif count > top3[2]:
        top3[2] = count


def find_top_three_calorie_counts(data: List[str]) -> List[str]:
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
        
        top3 = find_top_three_calorie_counts(data)

        print(f"Part One Answer: {top3[0]}")
        print(f"Part Two Answer: {sum(top3)}")

