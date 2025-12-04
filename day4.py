def read_file():
    data = []
    with open("day4.txt") as file:
        for i in file.readlines():
            data.append(i.strip())
    return data

def find_accessible_paper(data):
    paper_indexes = []
    total_lines = len(data)
    
    for line in range(total_lines):
        for char in range(len(data[line])):
            if data[line][char] == "@":
                paper_indexes.append([line,char])

    accessible_paper = 0

    for i in paper_indexes:
        line_num, index = i[0], i[1]
        num_adjacent_paper = 0

        try:
            if data[line_num][index+1] == "@":
                num_adjacent_paper +=1
        except IndexError:
            pass
    
        try:
            if data[line_num+1][index] == "@":
                num_adjacent_paper +=1
        except IndexError:
            pass
    
        try:
            if data[line_num+1][index+1] == "@":
                num_adjacent_paper +=1
        except IndexError:
            pass


        if line_num-1>=0:
            if data[line_num-1][index] == "@":
                num_adjacent_paper +=1 
            try:
                    if data[line_num-1][index+1] == "@":
                        num_adjacent_paper +=1
            except IndexError:
                pass

        try:
            if index-1>=0:
                if data[line_num][index-1] == "@":
                    num_adjacent_paper +=1
                if data[line_num+1][index-1] == "@":
                    num_adjacent_paper +=1
        except IndexError:
            pass

        try:
            if line_num-1>=0 and index-1>=0:
                if data[line_num-1][index-1] == "@":
                    num_adjacent_paper +=1
        except IndexError:
            pass

        if num_adjacent_paper<4:
            accessible_paper+=1

    return accessible_paper




def main():
    data = read_file()
    print(find_accessible_paper(data))

if __name__ == "__main__":
    main()