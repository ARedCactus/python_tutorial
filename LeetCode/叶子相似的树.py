import include.binary_treenode
class solution:
    def LeafSimilar(self, root_1, root_2):
        def GetList(node):
            if not node.left and not node.right:
                yield node.val
            else:
                if node.left:
                    yield from GetList(node.left)
                if node.right:
                    yield from GetList(node.right)
        list_1 = list(GetList(root_1)) if root_1 else list()
        list_2 = list(GetList(root_2)) if root_2 else list()
        return list_1 == list_2
            