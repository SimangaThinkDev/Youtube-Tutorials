import sys

# Case Study
# 2, 4, 7
# python3 argv_program.py 2 4 7

#sys.argv

first = int(sys.argv[1])
second = int(sys.argv[2])
third = int(sys.argv[3])

def get_sum(first, second, third):
    return sum([first, second, third])

print(get_sum(first, second, third))