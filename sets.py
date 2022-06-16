# create an empty set
from cgi import print_arguments


s = set()

# add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

print(s)
print(f"the set has {len(s)} elements.")
# remove
s.remove(2)
print(s)
print(f"the set has {len(s)} elements.")
