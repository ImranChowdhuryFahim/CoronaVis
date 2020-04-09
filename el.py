listy=["eat", "tea", "tan", "ate", "nat", "bat"]
from collections import defaultdict
retDict = {}
for i in listy:
    if "".join(sorted(i)) not in retDict:
        retDict["".join(sorted(i))]=[]
        retDict["".join(sorted(i))].append(i)
    else:
        retDict["".join(sorted(i))].append(i)

a=retDict.values()
a.sort(key=len)
print(a)
