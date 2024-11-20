"""
THIS CLASS IS ONLY FOR GUIDED LEARNING.

If you are struggling, use this file to help you code.
"""

import random

# TreeNode class
class TreeNode:
    """
    Define how you want. Suggested implementation.
    """
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right
    

    """
    Given method to display the Binary Tree.

    Call with: BinaryTree.root.display()
    """
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)


    """
    Given helper method to display the Binary Tree.

    **Do not touch**
    """
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinaryTree:
    """
        Define how you want. Suggested implementation.
    """
    def __init__(self):
        self.root = None
        self.height = 0
        self.num_nodes = 0


    """
        Helper class so python's 'len' can be used to get nunber of nodes in the tree
        :param self:
        :return: number of nodes in the tree 
        """
    def __len__(self):
        return self.num_nodes


    """
        Perform an in-order traversal for the tree
        :param self:
        :return:
        """
    def in_order_traversal(self, root):
        # Edge Case: is tree empty?

        # recursive call for left side

        # print value

        # recursive call for right side
        pass


    """
        perform a pre-order traversal of the tree
        :param self:
        :return:
        """
    def pre_order_traversal(self, root):
        # Edge Case: is tree empty?

        # print value

        # recursive call for left side

        # recursive call for right side
        pass


    """
        perform a post-order traversal of the tree
        :param self:
        :return:
        """
    def post_order_traversal(self, root):
        # Edge Case: is tree empty?

        # recursive call for left side

        # recursive call for right side

        # print value
        pass


    """
        find the node whose val = val
        :param val:
        :return node/None:
        """
    def tree_search(self, root, val):
        # Edge Case: is tree empty?

        # else, traverse the tree and return node if val is found

        # else, return None
        return None


    """
        find the max of the tree
        :param self:
        :return val:
        """
    def tree_maximum(self, root):
        # Edge Case: is tree empty?

        # you want to use a temp node as to not lose pointer to root of BST
        traversal_node = self.root   

        # by bst definition, greater values are to the right, so traverse the right side

        pass


    """
        find the min of the tree
        :param self:
        :return val:
        """
    def tree_minimum(self, root):
        # by bst definition, smaller values are to the left, so traverse the left side
        pass


    """
        find the successor of val given
        :param val:
        :return:
        """
    def tree_successor(self, root):
        # if right subtree isn't empty, successor is leftmost node in
        #       its right subtree

        # else, successor is the lowest ancestor of current tree node whose
        #       right child is also an ancestor of tree node
        pass


    """
        find the predecessor of val
        :param val:
        :return:
        """
    def tree_predecessor(self, root):
        # if left subtree isn't empty, predecessor is rightmost node in
        #       its left subtree

        # else, predecessor is the lowest ancestor of current tree node whose
        #       left child is also an ancestor of tree node
        pass


    """
        given two random values, find their lowest common ancestor
        :param root:
        :param val1:
        :param val2:
        :return:
        """
    def lowest_common_ancestor(self, root, val1, val2):
        # Do we already have both vals as children of our root?

        # else, traverse the tree and return the lowest common ancestor
        #       of the two values
        #           search left
        #           search right
        pass


    """
    Function to insert values into a Binary Tree and returns the root of the BT.
    :param: BinaryTree() root 
    :param: val
    :return: root
    """
    def tree_insert(self, val):
        # Empty Tree
        if self.root is None:
            self.root = TreeNode(val)
            return self.root
        # Else
        else:
            # Edge case: val equal to root
            
            # Val greater than root
            
            # Val less than root
            pass


    # given the root of a tree and a value to delete, delete the node from the BT
    def delete(self, root, val):
        # if val is in tree, delete it
        # else, do nothing
        pass


    # given the root of a tree, balance the tree
    def balance_bst(self, root):
        # if tree is already balanced, do nothing

        # else, do a in-order traversal and create a new BST
        # return the root of the new BST

        # you can use the insert method to insert values into the new BST
        pass



def main():
    mytree = BinaryTree()
    # set the root for the binary tree
    mytree.root = TreeNode(50)
    # insert random values into the Binary Tree
    my_random = random.randint(0, 99)
    my_random_two = random.randint(1, 12)
    my_random_three = random.randint(13, 35)
    for _ in range(50):
        # if _ == random.randint(1, 12):
        if _ == my_random_two:
            mytree.tree_insert(my_random_two)
            mytree.num_nodes +=1
        # if _ == random.randrange(13, 35):
        if _ == my_random_three:
            mytree.tree_insert(my_random_three)
            mytree.num_nodes +=1
        if _ == 2:
            mytree.tree_insert(my_random)
            mytree.num_nodes +=1
        else:
            mytree.tree_insert(random.randint(0, 98))
            mytree.num_nodes +=1
        
    
    # Display the Binary Tree
    mytree.root.display()
    

    # Traversal
    print ("In-order Traversal:")
    mytree.in_order_traversal()
    print ("\nPre-order Traversal:")
    mytree.pre_order_traversal() 
    print ("\nPost-order Traversal:")
    mytree.post_order_traversal()


    # Max/Min
    print ("\nMaximum value of tree:", mytree.tree_maximum().val)
    print ("\nMinimum value of tree:", mytree.tree_minimum().val)

        
    # Search
    print ("\nDoes", my_random, "exist in the tree?", end=" ")
    mynode = mytree.tree_search(my_random)
    if mynode is not None: 
        print ("Yes.")
    else:
        print ("No.")
    
    
    # Succession
    successor = mytree.tree_successor(mynode)
    if successor is not None:
        print ("\nMy TreeNode's (", mynode.val,") successor is", successor.val)
    else:
        print ("\n", mynode.val, "has no successor.")

    # Predecession
    predecessor = mytree.tree_predecessor(mynode)
    if predecessor is not None:
        print ("\nMy TreeNode's (", mynode.val,") predecessor is", predecessor.val)
    else:
        print ("\n", mynode.val, "has no predecessor.")


    # Balance the Binary Tree
    mytree.balance_tree()
    print("\n")
    mytree.root.display()

    print ("\nAttempting a Deletion of", mytree.root.left.val, "now.")
    mytree.delete(mytree.root.left.val)
    mytree.root.display()

    print ("\nAttempting a Deletion of", mytree.root.right.val, "now.")
    mytree.delete(mytree.root.right.val)
    mytree.root.display()


    # Common Ancestor
    my_c_ancestor = mytree.lowest_common_ancestor(my_random_two, my_random_three)
    # The only reason this if exists is because of how the tree is setup. RARELY, there is a case when the random nodes won't be inserted into the tree.
    #   JUST IGNORE and rerun the program
    try:
        print ("\nThe lowest common ancestor between", my_random_two, "and", my_random_three, "is", my_c_ancestor.val)
        # if my_c_ancestor is not None:
    except: 
        print("\nRandom Nodes were not inserted because of the design of insertion. Ignore and restart program.")
        print ("\n*There is no common ancestor between*", my_random_two, "and", my_random_three)

    # Current Common Ancestor code breaks the tree.   



if __name__ == "__main__":
    print("STARTING PROGRAM\n")
    main()
    print("\nEXITING PROGRAM")
    exit()

    
