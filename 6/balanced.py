import argparse
import logging

def remove_others(exp):
    ret = ""
    for c in exp:
        if c == "(":
            ret += "("
        elif c == ")":
            ret += ")"
    return ret

def find_pair_index(exp):
    ret = 1
    cnt = 0

    for i in range(len(exp)):
        if exp[i] == "(":
            cnt += 1
        elif exp[i] == ")":
            cnt -= 1

        if cnt == 0:
            ret = i
            break

    if cnt > 0:
        ret = -1

    return ret

# string -> bool
# The function checks if the expression contains the balanced parantheses.
# If it is, the function returns True; otherwise, it returns False
def is_balanced(exp):
    if exp == "()":
        return True
    elif len(exp) > 2:
        if exp[0] == "(" and exp[1] == ")":
            return is_balanced(exp[2:])
        elif exp[-2] == "(" and exp[-1] == ")":
            return is_balanced(exp[:-2])
        elif exp[0] == "(" and find_pair_index(exp) > 0:
            idx = find_pair_index(exp)
            return is_balanced(exp[1:idx]) and is_balanced(exp[idx+1:])
    elif len(exp) == 0:
        return True
    else:
        return False


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
    parentheses = remove_others(args.exp)
    logging.info("Result: {}".format(is_balanced(parentheses)))

if __name__ == "__main__":
    main()
