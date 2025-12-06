def read_file():
    fresh_range = []
    ingredient_data = []
    next_data = False
    with open("day5.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line == "\n":
                next_data = True
            else:
                if next_data:
                    ingredient_data.append(int(line))
                else:
                    fresh_range.append(line)

    return fresh_range, ingredient_data

def find_ranges(data):
    new_data = []
    for i in range(len(data)):
        lower_bound,upper_bound = str(data[i]).split("-")
        lower_bound,upper_bound = int(lower_bound), int(upper_bound)
        
        new_data.append((lower_bound, upper_bound))
    return new_data
        
def check_fresh(fresh_range, ingredient_data):
    total_fresh = 0
    fresh_found = False
    for food_id in ingredient_data:
        fresh_found = False
        if not fresh_found:
            for i in range(len(fresh_range)):
                lower_bound, upper_bound = fresh_range[i]
                if int(lower_bound)<=food_id<=int(upper_bound):
                    total_fresh+=1
                    fresh_found = True
                    break
    return total_fresh

def main():
    fresh_range, ingredient_data = read_file()
    fresh_range = find_ranges(fresh_range)
    print("Fresh-range: ", fresh_range)

    print(check_fresh(fresh_range, ingredient_data))

if __name__ == "__main__":
    main()