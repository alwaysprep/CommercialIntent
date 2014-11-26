import random


def clean_me(file_name, write_file_name):
    mydic={}
    for line in open(file_name):
        if line in mydic:
            mydic[line] += 1
        else:
            mydic[line] = 1

    w = open(write_file_name,"w")

    #TODO clean and WRİTE to file


