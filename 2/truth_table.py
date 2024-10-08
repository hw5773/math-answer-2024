import re
import argparse
import logging
import copy
import time
from operators import *

def extract_variables(expression):
    sorted_variable_set = sorted(set(re.findall(r'\b[a-z]\b', expression)))
    return sorted_variable_set

def make_combinations(n):
    if n == 1:
        return [[True], [False]]
    else:
        tmp = make_combinations(n-1)
        ret = []
        for c in tmp:
            c1 = copy.copy(c)
            c1.append(True)
            c2 = copy.copy(c)
            c2.append(False)
            ret.append(c1)
            ret.append(c2)
        return ret

def truth_table(expression):
    vlst = extract_variables(expression)
    n = len(vlst)
    combinations = make_combinations(n)

    for c in combinations:
        for idx in range(len(vlst)):
            exec("{}={}".format(vlst[idx], c[idx]))
        ret = eval(expression)
        c.append(ret)

    return combinations

def print_truth_table(expression):
    table = truth_table(expression)
    vlst = extract_variables(expression)
    logging.debug("vlst: {}".format(vlst))
    logging.debug("table: {}".format(table))

    for v in vlst:
        print ("{}\t".format(v), end="")
    print("{}".format(expression))

    for row in table:
        for elem in row:
            print ("{}\t".format(elem), end="")
        print("")

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--exp", required=True, help="Expression", type=str)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")

    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    logging.info("Expression: {}".format(args.exp))
    logging.debug("  Extracted variables: {}".format(extract_variables(args.exp)))
    print_truth_table(args.exp)

if __name__ == "__main__":
    main()
