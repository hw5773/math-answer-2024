import argparse
import logging

def reverse(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="Input string", type=str)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")

    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    logging.info("Input string: {}".format(args.input))
    output = reverse(args.input)
    logging.info("Reversed string: {}".format(output))

if __name__ == "__main__":
    main()
