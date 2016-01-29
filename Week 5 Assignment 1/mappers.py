def split_fileA(line):
    # split the input line in word and count on the comma
    wc = line.split(",")
    word = wc[0]
    count = wc[1]
    # turn the count to an integer  
    count = int(count)
    return (word, count)



def split_fileB(line):
    # split the input line into word, date and count_string
    wc = line.split(",")
    word = wc[0].split(" ")[1]
    date = wc[0].split(" ")[0]
    count_string = wc[1]
    return (word, date + " " + count_string) 