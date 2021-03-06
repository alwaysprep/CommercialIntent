import random


def clean_me(file_name, write_file_name):
    """
        Cleans the file and write it to specified file with
            ->removing duplicate lines
            ->shuffling data
        Does not modify given file
    """
    mydic={}
    for line in open(file_name):
        if line in mydic:
            mydic[line] += 1
        else:
            mydic[line] = 1

    w = open(write_file_name,"w")

    my_lis = []
    for line, count in mydic.items():
        if count>6:
            count=6

        for c in range(count):
            my_lis.append(line)

    del mydic

    random.shuffle(my_lis)

    for line in my_lis:
        w.write(line)

    w.close()


clean_me("data.csv", "cleaned_data.csv")