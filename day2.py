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

def find_all_invalid_ids(data):
    invalid_ids = []
    for interval in data:
        lower_bound, upper_bound = interval[0], interval[1]+1
        for i in range(lower_bound, upper_bound):
            num_length = len(str(i))
            max_sequence_length = num_length//2 + 1
            for sequence_length in range(1,max_sequence_length):
                required_reps = num_length//sequence_length
                if str(i) == str(i)[:sequence_length]*required_reps:
                    if i not in invalid_ids:
                        invalid_ids.append(i)
                        #prevent double counting
                else:
                    continue
    if len(invalid_ids)>1:
        return sum(invalid_ids)
    else:
        return invalid_ids


def main():
    data = read_file()
    intervals_data = convert_to_intervals(data)
    print(find_all_invalid_ids(intervals_data))


if __name__ == "__main__":
    main()