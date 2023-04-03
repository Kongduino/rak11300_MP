from BST import *

bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(9)
bst.insert(6)
print("Search for 7: {}".format(bst.search(7)))
bst.delete(7)
print("Search again for 7: {}".format(bst.search(7)))
print("Lookup 8: {}".format(bst.lookup(8)))
n = bst.lookup(9)
print("Lookup 9: {}".format(n))
bst.show(n)
v = bst.lookup(n.left.val)
print("Lookup {}: {}".format(n.left.val, n))
bst.show(v)
