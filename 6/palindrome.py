import argparse
import logging

def is_palindrome(s):
    if len(s) == 0:
        return True
    elif len(s) == 1:
        return True
    elif len(s) >= 2:
        head = s[0]
        tail = s[-1]
        if head == tail:
            return is_palindrome(s[1:-1])
        else:
            return False
    else:
        return False

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
    result = is_palindrome(args.input)
    logging.info("Is palindrome? {}".format(result))

if __name__ == "__main__":
    main()
