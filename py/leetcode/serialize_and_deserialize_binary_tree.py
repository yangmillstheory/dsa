DELIMITER = '_'
NULL_CHAR = '*'


def _serialize(root, res=None):
    if res is None:
        res = []
    if not root:
        res.append(NULL_CHAR)
    else:
        res.append(str(root.val))
        _serialize(root.left, res)
        _serialize(root.right, res)
    return res


def _deserialize(tokens, i=0):
    if not tokens or i >= len(tokens) or tokens[i] == NULL_CHAR:
        return None, i+1
    root = TreeNode(tokens[i])
    root.left, i = _deserialize(tokens, i+1)
    root.right, i = _deserialize(tokens, i)
    return root, i


class Codec:
    def serialize(self, root):
        '''Serialize a binary tree in O(n) time and O(h) space.'''
        return DELIMITER.join(_serialize(root))

    def deserialize(self, data):
        '''Deserialize a binary tree in O(n) time and O(h) space.'''
        return _deserialize(data.split(DELIMITER))[0]

