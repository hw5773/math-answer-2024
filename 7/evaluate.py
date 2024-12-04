import sys
import argparse
import logging
import time
import random
from sorting import bubble, insertion, mergesort

def generate_random_list(n):
    ret = []

    while n > 0:
        num = random.randint(1, n * 100)
        if num not in ret:
            ret.append(num)
            n -= 1
    return ret

def evaluate(func, lst):
    start = time.time()
    ret = func(lst)
    end = time.time()
    return ret, end - start

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True, help="Name of the sorting algorithm", choices=["bubble", "insertion", "merge"])
    parser.add_argument("-i", "--input", help="List to be sorted", type=int, nargs="+")
    parser.add_argument("-e", "--elements", help="Number of elements", type=int)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")

    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    if not args.input and not args.elements:
        logging.error("You need to specify either of an input list (--input) or the number of elements (--elements)")
        sys.exit(1)

    logging.info("Sorting algorithm: {}".format(args.name))

    if args.elements and args.elements > 0:
        lst = generate_random_list(args.elements)
    else:
        lst = args.input

    if args.name == "bubble":
        ret, et = evaluate(bubble, lst)
    elif args.name == "insertion":
        ret, et = evaluate(insertion, lst)
    elif args.name == "merge":
        ret, et = evaluate(mergesort, lst)

    logging.debug("Original list: {}".format(args.input))
    logging.debug("Sorted list: {}".format(ret))
    logging.info("Length of the list: {}".format(len(ret)))
    logging.info("Elapsed time: {}s".format(et))

if __name__ == "__main__":
    main()
