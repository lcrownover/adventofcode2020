#!/usr/bin/env python3


def lower_half(elems):
    return elems[: len(elems) // 2]


def upper_half(elems):
    return elems[len(elems) // 2 :]


def row(boarding_pass):
    rows = list(range(0, 128))
    chars = list(boarding_pass[:7])
    for c in chars:
        if c == "F":
            rows = lower_half(rows)
        else:
            rows = upper_half(rows)
    return rows[0]


def column(boarding_pass):
    columns = list(range(0, 8))
    chars = list(boarding_pass[-3:])
    for c in chars:
        if c == "L":
            columns = lower_half(columns)
        else:
            columns = upper_half(columns)
    return columns[0]


def seat_id(boarding_pass):
    r = row(boarding_pass)
    c = column(boarding_pass)
    s_id = r * 8 + c
    return s_id


def highest_id(boarding_passes):
    return list(sorted([seat_id(bp) for bp in boarding_passes]))[-1]


def missing_seat(boarding_passes):
    seat_ids = list(sorted([seat_id(bp) for bp in boarding_passes]))
    for i, x in enumerate(seat_ids):
        if seat_ids[i + 1] != x + 1:
            return x + 1


with open("input.txt", "r") as f:
    boarding_passes = [line.strip() for line in f.readlines()]

print(highest_id(boarding_passes))
print(missing_seat(boarding_passes))


# print(seat_id("BFFFBBFRRR"))
# print(seat_id("FFFBBBFRRR"))
# print(seat_id("BBFFBBFRLL"))
