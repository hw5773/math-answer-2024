import sys
import argparse
import logging

def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n-1)
    else:
        return 0

def permutation(n, r, repeat):
    if repeat:
        return n ** r
    else:
        return int(factorial(n) / factorial(n-r))

def combination(n, r, repeat):
    if repeat:
        return combination(n + r - 1, r, False)
    else:
        return int(permutation(n, r, False) / factorial(r))

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--function", required=True, metavar="<function (permutation/combination)>", help="Function to be used", choices=["combination", "permutation"])
    parser.add_argument("-n", "--number", required=True, metavar="<total number of objects>", help="Total number of objects", type=int)
    parser.add_argument("-r", "--select", required=True, metavar="<number of selected objects>", help="Number of selected objects", type=int)
    parser.add_argument("-s", "--repeat", help="Repetition", action="store_true", default=False)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")

    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    if args.repeat:
        logging.info("function: {} with repetition".format(args.function))
    else:
        logging.info("function: {}".format(args.function))
        logging.debug("n: {}".format(args.number))
        logging.debug("r: {}".format(args.select))
        logging.debug("repeat: {}".format(args.repeat))

        if args.function == "permutation":
            ret = permutation(args.number, args.select, args.repeat)
        elif args.function == "combination":
            ret = combination(args.number, args.select, args.repeat)

        if ret:
            logging.info("result: {}".format(ret))
        else:
            logging.info("no result")

if __name__ == "__main__":
    main()
