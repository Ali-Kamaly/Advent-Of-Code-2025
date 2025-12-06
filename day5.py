def read_file():
    fresh_range = []
    next_data = False
    with open("day5.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line == "\n":
                next_data = True
            else:
                if next_data:
                    pass
                else:
                    fresh_range.append(line)

    return fresh_range

def find_ranges(data):
    new_data = []
    for i in range(len(data)):
        lower_bound,upper_bound = str(data[i]).split("-")
        lower_bound,upper_bound = int(lower_bound), int(upper_bound)
        
        new_data.append((lower_bound, upper_bound))
    return new_data

def simplify_intervals(data):
    new_data = []
    print("data: ", data)
    try:
        for _ in range(len(data)):
    
            try:
                smallest, up_limit = min(data)
            except ValueError:
                break
            loc = data.index((smallest, up_limit))
            data.pop(loc)
            current_start = smallest
            current_end = up_limit

            while data:
                try:
                    smaller, upper_lim = min(data)
                except ValueError:
                    break

                if smaller <= current_end + 1:
                    current_end = max(upper_lim, current_end)
                    data.pop(data.index((smaller,upper_lim)))
                else:
                    break
            new_data.append((current_start, current_end))

    except IndexError:
        pass

    return (new_data)

def total_num(data):
    total = 0
    for i in range(len(data)):
        lb, ub = data[i]
        total += (ub-lb)+1
    return total

def main():
    fresh_range = read_file()
    fresh_range = find_ranges(fresh_range)
    simplified_intervals = simplify_intervals(fresh_range)
    print(total_num(simplified_intervals))

if __name__ == "__main__":
    main()