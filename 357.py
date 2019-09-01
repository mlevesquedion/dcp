def solve(tree):
    running_depth = 0
    max_depth = 0
    for c in tree:
        if c == '(':
            running_depth += 1
            max_depth = max(max_depth, running_depth)
        elif c == ')':
            running_depth -= 1
    return max_depth - 1


print(solve('((((00)0)0)0)'))
