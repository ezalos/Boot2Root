import sys
from subprocess import Popen, PIPE, STDOUT
import itertools

phases_inputs = ["Public speaking is very easy.",
                "1 2 6 24 120 720",
                "1 b 214",
                "9",
                "opekma"]

phases_outputs = []

bad = b"Welcome this is my little bomb !!!! You have 6 stages with\nonly one life good luck !! Have a nice day!\nPhase 1 defused. How about the next one?\nThat's number 2.  Keep going!\nHalfway there!\nSo you got that one.  Try this one.\nGood work!  On to the next...\n\nBOOM!!!\nThe bomb has blown up.\n"

def get_inputs():
    base = ""
    for i in phases_inputs:
        base += i + "\n"

    arg_comb = list(itertools.permutations(["1", "2", "3", "5", "6"], 5))
    #print(arg_comb)
    n = base + "4" + " "
    for comb in arg_comb:
        h = n[:]
        for i in comb:
            h += i + " "
        h += "\n"
        yield h


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: " + sys.argv[0] + " ./path/to/bomb")
        sys.exit(1)
    for data in get_inputs():
        p = Popen(sys.argv[1], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        r = bytearray(data, 'ascii')
        stdout_data = p.communicate(input=r[:-1])[0]
        if stdout_data != bad:
            print("Input: ", data)
            print("Ouptut: ", stdout_data)
            good_pass = ""
            for i in data:
                if i != " " and i != "\n":
                    good_pass += i
            print("Here is the password: ", good_pass)
