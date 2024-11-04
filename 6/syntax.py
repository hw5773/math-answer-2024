import argparse
import logging

alphabets = set("abcdefghijklmnopqrstuvwxyz")

def is_integer(exp):
    try:
        a = int(exp)
        return True
    except:
        return False

def eval(exp):
    exp = exp.strip()
    if is_integer(exp):
        return True
    elif exp == "true":
        return True
    elif exp == "false":
        return True
    elif len(exp) == 1 and exp in alphabets:
        return True
    elif exp[0:3] == "not":
        return eval(exp[3:])
    elif "+" in exp:
        idx = exp.index("+")
        return eval(exp[0:idx]) and eval(exp[idx+1:])
    elif "*" in exp:
        idx = exp.index("*")
        return eval(exp[0:idx]) and eval(exp[idx+1:])
    else:
        return False

def syntax_checker(statement):
    s = statement.strip()
    if s[0:3] == "x:=":
        return eval(s[3:])
    elif ";" in s:
        idx = s.index(";")
        return syntax_checker(s[0:idx]) and syntax_checker(s[idx+1:])
    elif s[0:2] == "if" and "then" in s and "else" in s:
        idx1 = s.index("then")
        idx2 = s.index("else")
        return eval(s[2:idx1]) and syntax_checker(s[idx1+ 4:idx2]) and syntax_checker(s[idx2+4:])
    else:
        return False

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--statement", required=True, help="Statement to be proved", type=str)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")

    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    logging.info("statement: {}".format(args.statement))
    logging.info("syntax check result: {}".format(syntax_checker(args.statement)))

if __name__ == "__main__":
    main()
