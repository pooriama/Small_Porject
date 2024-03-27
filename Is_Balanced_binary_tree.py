from collections import namedtuple


def is_balanced_binary_tree(tree):
    balancedstatush = namedtuple("balancedstatush", ("balanced", "height"))

    def check_balanced(tree):
        if not tree:
            return balancedstatush(True, -1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return balancedstatush(False, 0)
        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return balancedstatush(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return balancedstatush(is_balanced, height)
