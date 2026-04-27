from collections import deque


# Task 1
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test
print("Task 1:", two_sum([2, 7, 11, 15], 9))


# Task 2
def first_unique_char(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1

# Test
print("Task 2:", first_unique_char("leetcode"))
print("Task 2:", first_unique_char("loveleetcode"))


# Task 3
def is_isomorphic(s, t):
    s_to_t = {}
    t_to_s = {}
    for cs, ct in zip(s, t):
        if cs in s_to_t:
            if s_to_t[cs] != ct:
                return False
        else:
            if ct in t_to_s:
                return False
            s_to_t[cs] = ct
            t_to_s[ct] = cs
    return True

# Test
print("Task 3:", is_isomorphic("egg", "add"))
print("Task 3:", is_isomorphic("foo", "bar"))



# Task 4
def is_happy(n):
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return True

# Test
print("Task 4:", is_happy(19))
print("Task 4:", is_happy(2))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):

    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root



# Task 5
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

# Test
tree5 = build_tree([3, 9, 20, None, None, 15, 7])
print("Task 5:", level_order(tree5))


# Task 6
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Test
tree6 = build_tree([3, 9, 20, None, None, 15, 7])
print("Task 6:", max_depth(tree6))   # 3


# Task 7
def is_symmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val
                and is_mirror(left.left, right.right)
                and is_mirror(left.right, right.left))

    return is_mirror(root.left, root.right) if root else True

# Test
tree7a = build_tree([1, 2, 2, 3, 4, 4, 3])
tree7b = build_tree([1, 2, 2, None, 3, None, 3])
print("Task 7:", is_symmetric(tree7a))
print("Task 7:", is_symmetric(tree7b))



# Task 8
def longest_consecutive(root):
    max_len = [0]

    def dfs(node, parent_val, length):
        if not node:
            return
        if node.val == parent_val + 1:
            length += 1
        else:
            length = 1
        max_len[0] = max(max_len[0], length)
        dfs(node.left, node.val, length)
        dfs(node.right, node.val, length)

    dfs(root, float('-inf'), 0)
    return max_len[0]

tree8 = TreeNode(1)
tree8.right = TreeNode(3)
tree8.right.left = TreeNode(2)
tree8.right.right = TreeNode(4)
tree8.right.right.right = TreeNode(5)
print("Task 8:", longest_consecutive(tree8))


# Task 9
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

# Test
print("Task 9:", sort_colors([2, 0, 2, 1, 1, 0]))


# Task 10
def quick_sort(nums, low=0, high=None):
    if high is None:
        high = len(nums) - 1

    def partition(low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    if low < high:
        pi = partition(low, high)
        quick_sort(nums, low, pi - 1)
        quick_sort(nums, pi + 1, high)
    return nums

# Test
print("Task 10:", quick_sort([3, 6, 8, 10, 1, 2, 1]))


# Task 11
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])


    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1
    return nums

# Test
print("Task 11:", merge_sort([5, 2, 4, 6, 1, 3]))



# Task 12
def heap_sort(nums):
    n = len(nums)

    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and nums[left] > nums[largest]:
            largest = left
        if right < n and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(i, 0)

    return nums

# Test
print("Task 12:", heap_sort([12, 11, 13, 5, 6, 7]))