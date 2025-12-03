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
        number = ""
        digits_found = 0

        while digits_found !=12:
            try:
                max_digit_found = max(temp_list[:(-11+digits_found)])
            except ValueError:
                max_digit_found = max(temp_list)
            finally:
                digit_loc = temp_list.index(max_digit_found)
                temp_list = temp_list[digit_loc+1:]
                digits_found +=1
                number = number + str(max_digit_found)
        jolts.append(int(number))
        
    return sum(jolts)

def main():
    lines = read_file()
    print(calculate_jolts(lines))


if __name__ == "__main__":
    main()