def print_elem(letter, count): 
    for i in range(count): 
        print(letter, end = "") 
 
def print_group(corner_char, fill_char, fill_count): 
    print_elem(corner_char, 1) 
    print_elem(fill_char, fill_count) 
 
def print_line(corner_char, fill_char, fill_count, rep): 
    for i in range(rep): 
        print_group(corner_char, fill_char, fill_count) 
    print_elem(corner_char, 1) 
    print() 
 
def print_grids(corner_char, rows, cols): 
    for i in range(rows): 
        print_line('+', '-', 4, cols) 
        for i in range(4): 
            print_line('|', ' ', 4, cols) 
    print_line('+', '-', 4, cols) 
 
print_grids('+', 2, 3) 
