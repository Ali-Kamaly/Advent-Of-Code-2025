def read_file():
    with open("day2.txt") as file:
        for i in file:
            ranges = i.split(",")
            data = ranges
    return data

def convert_to_intervals(data):
    intervals_data = []
    for i in data:
        index_location = i.index("-")
        lower_bound = int(i[:index_location])
        upper_bound = int(i[index_location+1:])
        intervals_data.append([lower_bound,upper_bound])
    return intervals_data

def find_invalid_ids(data):
    invalid_ids = []
    for interval in data:
        lower_bound, upper_bound = interval[0], interval[1]+1
        for i in range(lower_bound, upper_bound):
            mid_index = len(str(i))//2
            if str(i)[:mid_index] == str(i)[mid_index:]:
                invalid_ids.append(i)
    return sum(invalid_ids)

def main():
    data = read_file()
    intervals_data = convert_to_intervals(data)
    print(find_invalid_ids(intervals_data))


if __name__ == "__main__":
    main()