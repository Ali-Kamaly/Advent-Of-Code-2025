def read_file(directions):
    with open ("day1.txt") as file:
        for i in file:
            directions.append(i)

def clean_data(directions):
    return [i.replace("\n","") for i in directions]

def calculate_password(movements):
    value_at = 50
    previous_value = 0
    num_zeros = 0
    #number of times zero has been landed on
    zero_passed_counter = 0
    for i in movements:
        if i[0] == "R":
            value_at += int(i[1:])
            if value_at >99:
                previous_value = value_at
                value_at = value_at % 100
                #looping around from 99 to 0

                if value_at != 0:
                    zero_passed_counter += previous_value//100
                    #checks how many times it went past zero
                else:
                    zero_passed_counter += (previous_value//100) -1
                    #to prevent double counting (when on 0, counter will be incremented further, later)

        else:
            before_movement = value_at
            value_at -= int(i[1:])
            if value_at <0:
                previous_value = value_at
                value_at = value_at % 100
                #looping around from 0 to 99

                if value_at != 0 and before_movement!= 0:
                    zero_passed_counter += ((abs(previous_value)+100)//100)
                    #checks how many times it went past zero
                else:
                    zero_passed_counter += ((abs(previous_value)+100)//100)-1
                    #to prevent double counting (when on 0, counter will be incremented further, later)

        if value_at == 0:
            num_zeros += 1

    total_zeros = num_zeros + zero_passed_counter
    return (total_zeros)

def main():
    directions = []
    read_file(directions)
    movements = clean_data(directions)
    print(calculate_password(movements))

main()