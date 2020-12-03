#!/usr/bin/env python3

import copy

def split(w):
    return [c for c in w]

def print_course(course, num_rows=0):
    if num_rows == 0: num_rows = len(course)
    for i,row in enumerate(course):
        if i < num_rows:
            print(row)

with open('./input.txt', 'r') as f:
    course = [split(line.strip()) for line in f.readlines()]

# gonna try to do this in functional programming, even though i think it'd be more fun to use a class...
def navigate_right(course):
    new_course = []
    for row in course:
        x = row.pop(0)
        row.append(x)
        new_course.append(row)
    return new_course

def navigate_down(course):
    if not course:
        return None
    new_course = course
    new_course.pop(0)
    return new_course

def traverse_course(course, right, down):
    course = copy.deepcopy(course)
    score = 0
    while True:
        if not course:
            break
        if course[0][0] == '#':
            score += 1
        for i in range(0,right):
            course = navigate_right(course)
        for i in range(0,down):
            course = navigate_down(course)
    return score

first_ans = traverse_course(course, 3,1)
print(first_ans)

score = 1
score *= traverse_course(course, 1, 1)
score *= traverse_course(course, 3, 1)
score *= traverse_course(course, 5, 1)
score *= traverse_course(course, 7, 1)
score *= traverse_course(course, 1, 2)

print(score)
