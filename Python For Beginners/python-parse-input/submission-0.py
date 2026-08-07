from typing import List

def read_integers() -> List[int]:
    l = []
    for i in input().split(","):
        l.append(int(i))
    return l

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
