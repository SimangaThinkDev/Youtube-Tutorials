import argparse

parser = argparse.ArgumentParser(description="return sum of specified number")
parser.add_argument("first", type=int, help="first number")
parser.add_argument("second", type=int,help="second number")
parser.add_argument("third", type=int, help="third number")

arguments = parser.parse_args()

def get_sum(first, second, third):
    return sum([first, second, third])

first = arguments.first
second = arguments.second
third = arguments.third

print(get_sum(first, second, third))