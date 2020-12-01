#!/usr/bin/env python3

e = [int(e.strip()) for e in open('input.txt', 'r').readlines()]
print([i*j for j in e for i in e if i + j == 2020][0])
print([i*j*k for k in e for j in e for i in e if i + j == 2020][0])
