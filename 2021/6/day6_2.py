with open('day6_2.txt') as file:
    day_limit = 256
    lines = [int(x) for x in file.readlines()[0].strip().split(',')]
    jellies = [(0, int(x)) for x in lines]
    jelly_records = {}

    def check_total_offsprings(parent_jelly):
        if parent_jelly[0] > day_limit:
            return 0
        parent_jelly_key = str(parent_jelly[0]) + ',' + str(parent_jelly[1])
        if parent_jelly_key not in jelly_records:
            count = 0
            while parent_jelly[0] <= day_limit:
                baby_jelly = (parent_jelly[0] + parent_jelly[1] + 1, 8)
                count += check_total_offsprings(baby_jelly)
                parent_jelly = (parent_jelly[0] + parent_jelly[1] + 1, 6)
            count += 1
            jelly_records[parent_jelly_key] = count
        return jelly_records[parent_jelly_key]

    count1 = 0
    for jelly in jellies:
        count1 += check_total_offsprings(jelly)
    print(count1)