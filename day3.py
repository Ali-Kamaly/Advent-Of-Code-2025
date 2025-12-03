def read_file():
    lines = []
    with open("day3.txt") as file:
        for i in file.readlines():
            lines.append(str(int(i)))
    return lines

def calculate_jolts(lines):
    jolts = []
    for i in lines:
        temp_list = []
        max_digit_found = 0
        for j in i:
            temp_list.append(j)
        
        max_digit_found = max(temp_list[:-1])
        max_digit_loc=temp_list.index(max_digit_found)

        next_max = max(temp_list[max_digit_loc+1:])
        value = int(str(max_digit_found) + str(next_max))

        jolts.append(value)
    return sum(jolts)

def main():
    lines = read_file()
    print(calculate_jolts(lines))


if __name__ == "__main__":
    main()