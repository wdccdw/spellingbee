import sys


# return true if iterable a only contains members of iterable b.
def only_has(a, b):
    for ch in a:
        if ch not in b:
            return False
    return True


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dict", help="specify an alternate dictionary")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--pangrams", action="store_true", help="highlight pangrams")
    parser.add_argument('letters', nargs=1,
                        help='the list of letters')
    parser.add_argument('mandatory', nargs=1,
                        help='the mandatory letter')
    args = parser.parse_args()

    d = '/usr/share/dict/words'

    if args.dict:
        d = args.dict

    # the list of outer letters
    l = [x.lower() for x in args.letters[0]]
    # the mandatory center letter
    m = args.mandatory[0].lower()

    ag = set(l)
    ag.add(m)


    if args.debug:
        sys.stderr.write('l: ' + ' '.join(l) + "\n")
        sys.stderr.write('m: ' + m + "\n")
        sys.stderr.write('ag: ' + ' '.join(sorted(ag)) + "\n")



    with open(d) as f:
        for line in f:
            # line must have mandatory letter
            if m not in line:
                continue

            line = line.rstrip().lower()

            # NYT only accepts words of 4 or more letters
            if len(line) < 4:
                continue

            if only_has(line, ag):
                if args.pangrams and only_has(ag,line):
                    print(line + "*")
                else:
                    print(line)
                     