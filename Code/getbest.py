#!/usr/bin/env python3

import sys

def getCols(f):
    ''' Identify the columns that contain the marks and student numbers '''
    # Course,Student Number,Mark,Comment
    headings = f.readline().strip().split(",")
    i=0
    num_col = 0                             # Initialising the index
    mark_col = 0
    for head in headings:
        if head == "Student Number":
            num_col=i                    # Updating the index
        elif head == "Mark" : 
            mark_col = i

        i = i + 1

    return (num_col, mark_col)

def findTop(f, num_col, mark_col):
    ''' finds the top student in the class '''
    best = 0
    best_idx = 0                            # Initialising index
    for line in f:
        data = line.strip().split(",")
        if data[0] != "Course":
            mark = int(data[mark_col])
            if mark > best:
                best = mark
                best_idx = data[num_col]   # Allowing the student number of the top student to display
    return best_idx, best

if __name__ == '__main__':
    f = open(sys.argv[1])
    num_col, mark_col = getCols(f)
    best_idx, best = findTop(f, num_col, mark_col)
    f.close()
    print("The top student was student %s with %d"%(best_idx,best))
