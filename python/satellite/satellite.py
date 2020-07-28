def tree_from_traversals(preorder, inorder):
    if len(preorder) == len(inorder) == 0:
        return {}
    elif len(preorder) != len(inorder):
        raise ValueError('invalid')
    else:
        if len(set(preorder)) != len(preorder):
            raise ValueError('invalid')
        root = preorder.pop(0)
        value = {'v': root}
        left_inorder, right_inorder = find_leaves_inorder(root, inorder)
        left_preorder = [i for i in preorder if i in left_inorder]
        right_preorder = [i for i in preorder if i in right_inorder]
        value['l'] = tree_from_traversals(left_preorder, left_inorder)
        value['r'] = tree_from_traversals(right_preorder, right_inorder)
        return value

def find_leaves_inorder(root, inorder):
    root_index = inorder.index(root)
    return inorder[:root_index], inorder[root_index+1:]