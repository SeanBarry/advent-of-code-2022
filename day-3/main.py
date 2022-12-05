priorities = {
    **{ chr(i): i - 96 for i in range(97, 123)},
    **{chr(i): i - 38 for i in range(65, 91)}
}

def part_one(data):
    total_sum = 0

    for s in data:
        first, second = set(s[:len(s)//2]), set(s[len(s)//2:])
        common = first.intersection(second)
        total_sum += priorities[list(common)[0]]

    return total_sum

def part_two(data):
    total_sum = 0
    chunks = [data[n:n+3] for n in range(0, len(data), 3)] 
    
    for chunk in chunks:
        total_sum += priorities[(
            list(
                set(chunk[0]).intersection(set(chunk[1]), set(chunk[2]))
            )[0]
        )]

    return total_sum

with open('./data.txt') as data:
    data = [t.strip() for t in data.readlines()]
    part_one_answer = part_one(data)
    part_two_answer = part_two(data)
    print(f"The answer to part one is {part_one_answer}") 
    print(f"The answer to part two is {part_two_answer}")
