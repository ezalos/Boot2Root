import sys
import re

reg_1 = r"(ft_fun/([0-9A-Za-z]+.pcap)?\d+ \dustar  nnmusers)"
reg = r"//file(\d+)"

def split(content):
    new = ""
    for i in content:
        if i >= 20 and i < 127:
            new += chr(i)
    after = re.sub(reg_1, r"KEYHERE\n//\1\n", new)
    after = re.sub(reg, r"EREHYEK\1", after)
    res = after.split("KEYHERE")
    new = []
    for i in res:
        duo = i.split("EREHYEK")
        try:
            duo[1] = int(duo[1])
            new.append(duo)
        except:
            pass
    new.sort(key=lambda x : x[1])
    output = ""
    for i in new:
        output += i[0] + "\n"
    return output #re.sub(r";}void", r";}\nvoid", output)

def get_file(path):
    with open(path, "rb") as f:
        return f.read()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: " + sys.argv[0] + " ./path/to/fun")
        sys.exit(1)
    hmm = get_file(sys.argv[1])
    ohh = split(hmm)
    print(ohh)
