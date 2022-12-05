def part_one(data):
    num_overlaps = 0
    for i in data:
        l1,l2,h1,h2 = i[0],i[1],i[2],i[3]
        if l1 <= h1 and l2 >= h2:
            num_overlaps+=1
        elif h1 <= l1 and h2 >= l2:
            num_overlaps+=1
    return num_overlaps


def part_two(data):
    num_overlaps = 0
    for i in data:
        l1,l2,h1,h2 = i[0],i[1],i[2],i[3]
        if (l1 >= h1 and l1 <= h2) or (l2 >= h1 and l2 <= h2):
            num_overlaps += 1
        elif (h1 >= l1 and h1 <= l2) or (h2 >= l1 and h2 <= l2):
            num_overlaps +=1

    return num_overlaps


with open ('./data.txt') as data:
    data = [r.strip() for r in data.readlines()]
    data = [[f.split('-') for f in d.split(',')] for d in data]
    data = [tuple(map(int, [i[0],i[1],q[0],q[1]])) for i,q in data]
    part_one_answer = part_one(data)
    part_two_answer = part_two(data)

    print(f"The answer to part one is {part_one_answer}")
    print(f"The answer to part two is {part_two_answer}")
