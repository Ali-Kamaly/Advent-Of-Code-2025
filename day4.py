def read_file():
    data = []
    with open("day4.txt") as file:
        for i in file.readlines():
            data.append(list(i.strip()))
    return data

def find_accessible_paper(data, papers_accessible = 0):
    accessible_paper = papers_accessible
    paper_indexes = []
    try:
        total_lines = len(data)
    except TypeError:
        return accessible_paper
    edits = 0 
    
    for line in range(total_lines):
        for char in range(len(data[line])):
            if data[line][char] == "@":
                paper_indexes.append([line,char])
    
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

        if 0<=num_adjacent_paper<4:
            accessible_paper+=1
            data[line_num][index] = "x"
            edits+=1

    while edits!= 0 :
        accessible_paper, edits = find_accessible_paper(data, accessible_paper)

    return accessible_paper, edits

def main():
    data = read_file()
    accessible_paper, edits = find_accessible_paper(data)
    print(accessible_paper)

if __name__ == "__main__":
    main()