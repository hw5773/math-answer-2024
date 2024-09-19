import argparse
import logging
import copy

# TODO: the function returns True if the first argument is the subset of the second argument
# list * list -> bool
def is_subset(a, b):
    ret = True
    for e in a:
        if e not in b:
            ret = False
            break
    return ret

# TODO: the function returns the cardinality of a given set
# list -> int
def get_cardinality(a):
    return len(a)

# TODO: the function returns the power set of a given set
# list -> list of list
def generate_power_set(a):
    if len(a) == 1:
        return [[], a]
    else:
        x = a[0]
        tmp = sorted(generate_power_set(a[1:]))
        lst1 = copy.deepcopy(tmp)
        lst2 = copy.deepcopy(tmp)
        for e in lst2:
            e.append(x)
            e = sorted(e)
        ret = sorted(lst1 + lst2)
        return ret

# TODO: the function returns the cartesian product of two given sets
# list * list -> list of pairs
def generate_cartesian_product(a, b):
    ret = []
    for e1 in a:
        for e2 in b:
            ret.append((e1, e2))
    return ret

# TODO: the function returns the union of two sets
# list * list -> list
def union(a, b):
    ret = copy.copy(a)
    for e in b:
        if e not in a:
            ret.append(e)
    return ret

# TODO: the function returns the intersection of two sets
# list * list -> list
def intersection(a, b):
    ret = []
    for e in a:
        if e in b:
            ret.append(e)
    return ret

# TODO: the function returns A - B
# list * list -> list
def difference(a, b):
    ret = []
    for e in a:
        if e not in b:
            ret.append(e)
    return ret

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--elements-a", nargs="*", required=True, help="Elements of Set A", type=int)
    parser.add_argument("-b", "--elements-b", nargs="*", required=True, help="Elements of Set B", type=int)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")

    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    a = args.elements_a
    b = args.elements_b

    logging.info("Set A: {}".format(a))
    logging.info("Set B: {}".format(b))
    logging.info("")

    logging.info("A is the subset of B: {}".format(is_subset(a, b)))
    logging.info("Cardinality of A: {}".format(get_cardinality(a)))
    logging.info("Cardinality of B: {}".format(get_cardinality(b)))
    logging.info("")

    logging.info("Power Set of A: {}".format(generate_power_set(a)))
    logging.info("Power Set of B: {}".format(generate_power_set(b)))
    logging.info("")

    logging.info("Cartesian Product of A and B: {}".format(generate_cartesian_product(a, b)))
    logging.info("")

    logging.info("Union of A and B: {}".format(union(a, b)))
    logging.info("Intersection of A and B: {}".format(intersection(a, b)))
    logging.info("Difference of A and B: {}".format(difference(a, b)))

if __name__ == "__main__":
    main()
