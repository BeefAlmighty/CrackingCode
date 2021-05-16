# Implementation of Tree data structure.  Implementing "right-sibling" version
# for general trees.


class Tree:
    def __init__(self, item=None):
        if isinstance(item, TreeNode):
            self._root = item
        elif item:
            self._root = TreeNode(item)
        else:
            self._root = None

    def get_root(self):
        return self._root

    def traverse(self, kind="in_order"):
        if kind == "in_order":
            self.get_root().in_order_traversal()
        elif kind == "post_order":
            self.get_root().post_order_traversal()
        elif kind == "pre_order":
            self.get_root().pre_order_traversal()
        else:
            print("Incorrect specification of traversal.  Aborting.\n")


class BinaryTree(Tree):
    def __init__(self, item=None):
        super(BinaryTree, self).__init__(item)


class TreeNode:

    def __init__(self, item=None, left=None, right_sibling=None, parent=None):
        self._item = item
        self._left = left
        self._right_sibling = right_sibling
        self._parent = parent

    def __repr__(self):
        ans = f"({self.get_item()})"
        if self._left:
            ans += f"\n /"
        return ans

    def in_order_traversal(self):
        children = self.get_children()
        if children:
            left = children.pop(0)
        else:
            left = None
        if left:
            left.in_order_traversal()
        self.visit()
        for item in children:
            item.in_order_traversal()
        return

    def pre_order_traversal(self):
        self.visit()
        for item in self.get_children():
            item.pre_order_traversal()
        return

    def post_order_traversal(self):
        for item in self.get_children():
            item.post_order_traversal()
        self.visit()
        return

    def visit(self):
        print(self)

    def get_item(self):
        return self._item

    def get_parent(self):
        return self._parent

    def get_left_child(self):
        return self._left

    def get_right_sibling(self):
        return self._right_sibling

    def get_children(self):
        ans = []
        if self.get_left_child():
            temp = self.get_left_child()
            ans.append(temp)
            while temp.get_right_sibling():
                temp = temp.get_right_sibling()
                ans.append(temp)
        return ans

    def get_children_items(self):
        ans = self.get_children()
        return [item.get_item() for item in ans]


class BinaryNode(TreeNode):

    def __init__(self, item=None, left=None, right=None, parent=None):
        super().__init__(item, parent=parent, left=left, right_sibling=None)
        self._right = right

    def __repr__(self):
        ans = f"  ({self.get_item()})  "
        if self.get_left_child():
            ans += "\n /  "
            if self.get_right_child():
                ans += " \\ "
        return ans

    def get_right_child(self):
        return self._right

    def in_order_traversal(self):
        if self.get_left_child():
            self.get_left_child().in_order_traversal()
        self.visit()
        if self.get_right_child():
            self.get_right_child().in_order_traversal()


    def pre_order_traversal(self):
        self.visit()
        if self.get_left_child():
            self.get_left_child().pre_order_traversal()
        if self.get_right_child():
            self.get_right_child().pre_order_traversal()


    def post_order_traversal(self):
        if self.get_left_child():
            self.get_left_child().post_order_traversal()
        if self.get_right_child():
            self.get_right_child().post_order_traversal()
        self.visit()



def main():
    mid_left = TreeNode(1)
    leaf_1 = TreeNode(5, parent=mid_left)
    par = TreeNode(3, left=mid_left)

    mid_node = TreeNode(4, parent=par)
    leaf_2 = TreeNode(1, right_sibling=TreeNode(8, parent=mid_node),
                      parent=mid_node)
    mid_node._left = leaf_2

    mid_right = TreeNode(1, parent=par)
    leaf_3 = TreeNode(11, parent=mid_right,
                      right_sibling=TreeNode(9, parent=mid_right,
                                             right_sibling=TreeNode(6,
                                                                    parent=mid_right)))
    mid_right._left = leaf_3

    mid_node._right_sibling = mid_right
    mid_left._right_sibling = mid_node
    mid_left._left = leaf_1

    tree = Tree(par)
  #  tree.traverse(kind="post_order")

    b_node_1 = BinaryNode(2)
    b_node_2 = BinaryNode(7)

    low_mid_1 = BinaryNode(1)
    low_mid_2 = BinaryNode(5, left=b_node_1, right=b_node_2)
    b_node_1._parent = low_mid_2
    b_node_2._parent = low_mid_2

    b_node_3 = BinaryNode(4)
    b_node_4 = BinaryNode(9)
    b_node_5 = BinaryNode(2)
    b_node_6 = BinaryNode(16)

    low_mid_3 = BinaryNode(13, left=b_node_3)
    b_node_3._parent = low_mid_3

    low_mid_4 = BinaryNode(3, left=b_node_4, right=b_node_5)
    b_node_4._parent = low_mid_4
    b_node_5._parent = low_mid_4

    low_right = BinaryNode(9, left=low_mid_4, right=b_node_6)
    b_node_6._parent = low_right
    low_mid_4._parent = low_right

    first_left = BinaryNode(17, left = low_mid_1, right=low_mid_2)
    low_mid_1._parent = first_left
    low_mid_2._parent = first_left

    first_right = BinaryNode(41, left = low_mid_3, right=low_right)
    low_mid_3._parent = first_right
    low_right._parent = first_right

    root = BinaryNode(3, left = first_left, right=first_right)
    first_left._parent = root
    first_right._parentt = root

    bTree = BinaryTree(root)
    bTree.traverse("pre_order")


if __name__ == "__main__":
    main()
