import sys
import argparse
import logging
from counting import combination

def pascal_triangle(n):
    ret = []
    for i in range(n+1):
        ret.append(combination(n, i, False))
    return ret

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--row", required=True, metavar="<nth row>", help="nth row", type=int)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")

    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    logging.info("n: {}".format(args.row))

    ret = pascal_triangle(args.row)

    logging.info("result: {}".format(ret))

if __name__ == "__main__":
    main()
