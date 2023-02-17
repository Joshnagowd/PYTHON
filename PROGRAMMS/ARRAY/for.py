from array import *
vals = array("i",[1,-2,3,5])
newarray =array(vals.typecode,(a for a in vals))
for e in newarray:
    print(e)