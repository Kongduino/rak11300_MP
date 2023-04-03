class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, cur_node):
        if val < cur_node.val:
            if cur_node.left is None:
                cur_node.left = Node(val)
            else:
                self._insert(val, cur_node.left)
        elif val > cur_node.val:
            if cur_node.right is None:
                cur_node.right = Node(val)
            else:
                self._insert(val, cur_node.right)
        else:
            print("Value already in tree!")

    def lookup(self, val):
        if self.root is not None:
            return self._lookup(val, self.root)
        else:
            return None

    def _lookup(self, val, cur_node):
        if val == cur_node.val:
            return cur_node
        elif val < cur_node.val and cur_node.left is not None:
            return self._lookup(val, cur_node.left)
        elif val > cur_node.val and cur_node.right is not None:
            return self._lookup(val, cur_node.right)
        return None

    def search(self, val):
        if self.root is not None:
            return self._search(val, self.root)
        else:
            return False

    def _search(self, val, cur_node):
        if val == cur_node.val:
            return True
        elif val < cur_node.val and cur_node.left is not None:
            return self._search(val, cur_node.left)
        elif val > cur_node.val and cur_node.right is not None:
            return self._search(val, cur_node.right)
        return False

    def delete(self, val):
        self.root = self._delete(val, self.root)

    def _delete(self, val, cur_node):
        if cur_node is None:
            return cur_node
        if val < cur_node.val:
            cur_node.left = self._delete(val, cur_node.left)
        elif val > cur_node.val:
            cur_node.right = self._delete(val, cur_node.right)
        else:
            if cur_node.left is None:
                return cur_node.right
            elif cur_node.right is None:
                return cur_node.left
            temp_node = self._find_min(cur_node.right)
            cur_node.val = temp_node.val
            cur_node.right = self._delete(temp_node.val, cur_node.right)
        return cur_node

    def _find_min(self, cur_node):
        while cur_node.left is not None:
            cur_node = cur_node.left
        return cur_node

    def show(self, cur_node):
        if cur_node is None:
            print("None")
            return
        lVal = "None"
        if cur_node.left is not None:
            lVal = cur_node.left.val
        rVal = "None"
        if cur_node.right is not None:
            rVal = cur_node.right.val
        lVal = " Left: {} ".format(lVal)
        rVal = " Right: {}".format(rVal)
        nVal = "Value: {}".format(cur_node.val)
        print("{}{}".format((" "*(len(lVal)+1)), nVal))
        print("{} {} {}".format(lVal, (" "*(len(nVal))), rVal))

