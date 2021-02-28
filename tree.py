"""Tree class and tree node class."""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node {data}>".format(data=self.data)


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root={root}>".format(root=self.root)

    def get_nodes(self, data):
        """ Return a list of nodes with the given data

        For example::

            >>> b1 = Node("B")
            >>> b2 = Node("B")
            >>> e = Node("E")
            >>> c = Node("C", [ b1, e])
            >>> a = Node("A", [b2, c])
            >>> tree = Tree(a)
            >>> result = tree.get_nodes("B")
            >>> result == [b2, b1]
            True
            >>> tree.get_nodes("L")
            []

        """

        # TODO: Complete this function

       # take in a piece of data that the method is searching for
       # return a list of all of the nodes in the tree that contain that piece of data
       # The list returned should be in hierarchical order, meaning the list should be ordered from the highest ranking node to lowest ranking node. 
       # You can assume that there will be at most one node with the given data on any particular level of the tree.


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
