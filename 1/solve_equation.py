import argparse
import logging

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--min", help="Minimum value of the solution range", type=int, default=-100)
    parser.add_argument("-n", "--max", help="Maximum value of the solution range", type=int, default=100)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")
    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    r = range(args.min, args.max)
    solutions = []

    # The following loop is added for the answer
    logging.debug("r: {}".format(r))

    for i in r:
        tmp = i ** 2 - 100 * i + 1600
        if tmp == 0:
            solutions.append(i)

    logging.info("Solutions: {}".format(solutions))

if __name__ == "__main__":
    main()
