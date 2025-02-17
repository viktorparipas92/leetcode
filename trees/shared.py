class TreeNode(object):
    def __init__(self, value: int = 0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def inorder(self):
        if self.left:
            yield from self.left.inorder()
        yield self.value
        if self.right:
            yield from self.right.inorder()

    def preorder(self):
        yield self.value
        if self.left:
            yield from self.left.preorder()

        if self.right:
            yield from self.right.preorder()


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    return (
        p.value == q.value
        and is_same_tree(p.left, q.left)
        and is_same_tree(p.right, q.right)
    )