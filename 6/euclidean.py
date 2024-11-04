import argparse
import logging

def euclidean(first, second):
    if second == 0:
        return first
    return euclidean(second, first % second)

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--first", required=True, help="First number", type=int)
    parser.add_argument("-b", "--second", required=True, help="Second number", type=int)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")

    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    logging.info("First number: {}".format(args.first))
    logging.info("Second number: {}".format(args.second))

    gcd = euclidean(args.first, args.second)
    logging.info("GCD of two: {}".format(gcd))

if __name__ == "__main__":
    main()
