def read_file(directions):
    with open ("puzzle_input.txt") as file:
        for i in file:
            directions.append(i)

def clean_data(directions):
    for i in directions:
        i.replace("\n","")
    #removing the \n from each instruction

def calculate_password(directions):
    value_at = 50
    num_zeros = 0
    for i in directions:
        if i[0] == "R":
            value_at += int(i[1:])
            if value_at >99:
                value_at = value_at % 100
                #looping around from 99 to 0
        else:
            value_at -= int(i[1:])
            if value_at <0:
                value_at = value_at % 100
                #looping around from 0 to 99
        if value_at == 0:
            num_zeros += 1
    return num_zeros

def main():
    directions = []
    read_file(directions)
    clean_data(directions)
    print(calculate_password(directions))

main()