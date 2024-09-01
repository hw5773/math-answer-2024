import re
import argparse
import logging
import copy
import time
from operators import *

def extract_variables(expression):
    sorted_variable_set = sorted(set(re.findall(r'\b[a-z]\b', expression)))
    return sorted_variable_set

def truth_table(expression):
    raise NotImplementedError

def print_truth_table(expression):
    raise NotImplementedError

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
