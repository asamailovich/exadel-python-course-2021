def collect_leaves(i) -> list:
    res = []
    if type(i) is list:
        return i
    if type(i) is dict:
        for node, values in i.items():
            if isinstance(values, list):
                res.extend(values)
            elif isinstance(values, dict):
                res.extend(collect_leaves(values))
    return res


tree0 = {"node1": [1, 2, 3], "node2": [7, 8, 9]}
tree1 = {
   "node1": {
       "node11": {
           "node111": [1, 2, 3],
           "node112": [31, 5]
       },
       "node12": [31]
   },
   "node2": [7, 8, 9]
}
tree2 = [1, 2, 3]
assert collect_leaves(tree0) == [1, 2, 3, 7, 8, 9]
assert collect_leaves(tree1) == [1, 2, 3, 31, 5, 31, 7, 8, 9]
assert collect_leaves(tree2) == [1, 2, 3]
