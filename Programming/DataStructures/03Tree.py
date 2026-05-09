"""

Binary Tree - each node has at most 2 children. Not necessarily ordered.

Binary Search Tree (BST) - a tree where each node has at most 2 children,
left child < parent < right child. Enables efficient search, insert, delete.

Tree Terminology:
- Full Tree:    every node has 0 or 2 children (never 1)
- Perfect Tree: all interior nodes have 2 children, all leaves at same level
- Complete Tree: all levels filled except possibly last, filled left to right
- Balanced Tree: height is O(log n) — e.g. AVL, Red-Black trees
- Unbalanced:  degenerates to a linked list in worst case, height O(n)

Height:
- Empty tree  → -1
- Single node → 0
- Balanced    → O(log n)
- Unbalanced  → O(n)

Space complexity of recursive calls depends on tree height:
- Balanced tree: O(log n) call stack frames
- Unbalanced tree: O(n) call stack frames → risk of stack overflow

Why iterative over recursive?
- Recursion uses the call stack (typically ~8MB per thread, fixed).
- Iterative uses heap memory (limited only by RAM) — safer for deep trees.

DFS — explores depth-first, implemented via recursion or explicit stack.
    preOrder  : node → left → right  | use: copy/serialize a tree
    inOrder   : left → node → right  | use: sorted output from BST
    postOrder : left → right → node  | use: deletion, evaluate expressions

BFS — explores level by level, implemented via queue.
    levelOrder: visit all nodes at depth d before depth d+1

| Operation      | Avg (Balanced) | Worst (Unbalanced) |
|----------------|----------------|--------------------|
| insert         | O(log n)       | O(n)               |
| height         | O(n)           | O(n)               |
| preOrder       | O(n)           | O(n)               |
| inOrder        | O(n)           | O(n)               |
| postOrder      | O(n)           | O(n)               |
| levelOrder     | O(n)           | O(n)               |

Space complexity per traversal (call stack / auxiliary structure):
| Operation      | Balanced       | Unbalanced         |
|----------------|----------------|--------------------|
| recursive DFS  | O(log n)       | O(n)               |
| iterative DFS  | O(log n)       | O(n)               |
| levelOrder BFS | O(n) *         | O(n)               |
* BFS queue holds up to an entire level — worst case the last level ~ n/2 nodes.
"""

from collections import deque

class TreeImpl:
    class Node:
        def __init__(self, val=None):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # Time: O(log n) avg, O(n) worst | Space: O(log n) avg, O(n) worst (call stack)
    def insertHelper(self, val, current):
        if current is None:
            return self.Node(val)
        if val < current.val:
            current.left = self.insertHelper(val, current.left)
        elif val > current.val:
            current.right = self.insertHelper(val, current.right)
        return current

    def insert(self, val):
        self.root = self.insertHelper(val, self.root)

    # Time: O(n) — must visit every node | Space: O(log n) avg, O(n) worst
    def heightHelper(self, current):
        if current is None:
            return -1                          # empty tree height = -1
        return 1 + max(self.heightHelper(current.left), self.heightHelper(current.right))

    def height(self):
        return self.heightHelper(self.root)

    # --- Recursive DFS ---
    # All three: Time O(n), Space O(log n) avg / O(n) worst (call stack)

    def preOrderHelper(self, current, myList):
        """node → left → right"""
        if current is None:
            return
        myList.append(current.val)
        self.preOrderHelper(current.left, myList)
        self.preOrderHelper(current.right, myList)

    def preOrder(self):
        printableList = []
        self.preOrderHelper(self.root, printableList)
        return printableList

    def inOrderHelper(self, current, myList):
        """left → node → right  |  produces sorted output for a BST"""
        if current is None:
            return
        self.inOrderHelper(current.left, myList)
        myList.append(current.val)
        self.inOrderHelper(current.right, myList)

    def inOrder(self):
        printableList = []
        self.inOrderHelper(self.root, printableList)
        return printableList

    def postOrderHelper(self, current, myList):
        """left → right → node  |  children processed before parent"""
        if current is None:
            return
        self.postOrderHelper(current.left, myList)
        self.postOrderHelper(current.right, myList)
        myList.append(current.val)

    def postOrder(self):
        printableList = []
        self.postOrderHelper(self.root, printableList)
        return printableList

    # --- Iterative DFS ---
    # All three: Time O(n), Space O(log n) avg / O(n) worst (explicit stack on heap)

    def preOrderIterative(self):
        """Push right before left so left is popped first."""
        printableList = []
        myStack = [self.root]
        while myStack:
            current = myStack.pop()
            printableList.append(current.val)
            if current.right:
                myStack.append(current.right)   # right pushed first
            if current.left:
                myStack.append(current.left)    # left popped first
        return printableList

    def inOrderIterative(self):
        """Drill left as far as possible, process node, then go right."""
        printableList = []
        myStack = []
        curr = self.root
        while curr or myStack:
            while curr:                 # go left as far as possible
                myStack.append(curr)
                curr = curr.left
            curr = myStack.pop()        # process node
            printableList.append(curr.val)
            curr = curr.right           # then explore right subtree
        return printableList

    def postOrderIterative(self):
        """Peek at stack top; only pop after right subtree is fully visited."""
        printableList = []
        myStack = []
        current = self.root
        last_visited = None
        while current or myStack:
            while current:
                myStack.append(current)
                current = current.left
            peek = myStack[-1]
            # if right child exists and hasn't been visited yet, go right first
            if peek.right and last_visited != peek.right:
                current = peek.right
            else:
                printableList.append(peek.val)
                last_visited = myStack.pop()
        return printableList
    
    def postOrderIterativeAlternative(self):
        printableList = []
        stack = [self.root]
        mySet = set()  # to track visited nodes
        
        while stack:
            node = stack[-1]

            if node.left and node.left not in mySet:
                stack.append(node.left)
            elif node.right and node.right not in mySet:
                stack.append(node.right)
            else:
                node = stack.pop()
                mySet.add(node)
                printableList.append(node.val)
        
        return printableList

    # --- BFS ---
    # Time: O(n) | Space: O(n) — queue can hold up to ~n/2 nodes (last level)
    def levelOrder(self):
        """Visit nodes level by level using a queue."""
        printableList = []
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            printableList.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return printableList


items = [50, 40, 60, 45, 32, 33, 65, 62, 70]
myTree = TreeImpl()
for item in items:
    print("Inserting:", item)
    myTree.insert(item)

print("Preorder traversal:", myTree.preOrder())
print("Preorder traversal With Stack:", myTree.preOrderIterative())
print("Inorder traversal:", myTree.inOrder())
print("Inorder traversal With Stack:", myTree.inOrderIterative())
print("Postorder traversal:", myTree.postOrder())
print("Postorder traversal With Stack:", myTree.postOrderIterative())
print("Postorder traversal With Stack Alternative:", myTree.postOrderIterativeAlternative())
print("Height of the tree:", myTree.height())
print("Level order traversal:", myTree.levelOrder())