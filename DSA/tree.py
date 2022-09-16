class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    
class tree:
    
    def __init__(self, val):
        self.root = val
        self.queue = list()
        self.levelMarked = {}
        self.maxLevel = -1

    def getRoot(self):
        return self.root

    def preOrder(self, root):
        if not root:
            return 
        print(root.data, end= ' ')
        self.preOrder(root.left)
        self.preOrder(root.right)
    
    def inOrder(self, root):
        if not root:
            return 
        self.inOrder(root.left)
        print(root.data, end=' ')
        self.inOrder(root.right)
    
    def postOrder(self, root):
        if not root:
            return 
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end= ' ')

    def levelOrder(self, root):
        if not root:
            return 
        self.queue.append(root)
        self.queue.append(None)

        while self.queue:
            last_el = self.queue.pop(0)
            if last_el is None:
                continue
            print(last_el.data, end = ' ')
            if last_el.left:
                self.queue.append(last_el.left)
            if last_el.right:
                self.queue.append(last_el.right)
            if self.queue[0] is None and len(self.queue) >1:
                self.queue.pop(0)
                self.queue.append(None)
                print()
            
    def maximumValue(self, root):
        if not root:
            return float('-inf')
        
        return max(self.maximumValue(root.left),  self.maximumValue(root.right), root.data)

    def minimumValue(self, root):
        if not root:
            return float('inf')
        return min(self.minimumValue(root.left), self.minimumValue(root.right), root.data)

    def sizeOfTree(self, root):
        if not root:
            return 0
        return self.sizeOfTree(root.left) + self.sizeOfTree(root.right) + 1

    def heightOfTree(self, root):
        if not root:
            return 0
        return max(self.heightOfTree(root.left), self.heightOfTree(root.right)) + 1

    def leftView(self, root, level):
        if not root:
            return
        if level not in self.levelMarked.keys():
            self.levelMarked[level] = root
        
        self.leftView(root.left, level+1)
        self.leftView(root.right, level+1)
    
    def showLeftView(self, root):
        if not root:
            print("No left view")
            return 
        self.leftView(root, 0)
        for i in self.levelMarked:
            print(self.levelMarked[i].data, end=' ')
        
        self.levelMarked.clear()

    def rightView(self, root, level):
        if not root:
            return 
        
        self.levelMarked[level] = root
        self.rightView(root.left, level+1)
        self.rightView(root.right, level +1)
    
    def showRightView(self, root):
        if not root:
            print("No right view")
            return 
        self.rightView(root, 0)
        for i in self.levelMarked:
            print(self.levelMarked[i].data, end = ' ')

        self.levelMarked.clear()

    def topView(self, root, level):
        if not root:
            return
        
        if level not in self.levelMarked.keys():
            self.levelMarked[level] = root

        self.topView(root.left, level -1)
        self.topView(root.right, level +1)

    def showTopView(self, root):
        if not root:
            print("No top view")
            return 
        
        self.topView(root, 0)
        for i in sorted(self.levelMarked):
            print(self.levelMarked[i].data, i , end = ' ')

        self.levelMarked.clear()

    def bottomView(self, root, level):
        if not root:
            return 
        
        self.levelMarked[level] = root

        self.bottomView(root.left, level -1)
        self.bottomView(root.right, level +1)

    def showBottomView(self, root):
        if not root:
            print("No bottom view")
            return
        self.bottomView(root, 0)
        for i in sorted(self.levelMarked):
            print(self.levelMarked[i].data , end =' ')
        
        self.levelMarked.clear()

    def leftViewIMP(self, root, level):
        if not root:
            return 
        
        if self.maxLevel < level:
            print(root.data, end=' ')
            self.maxLevel  = level
        
        self.leftViewIMP(root.left, level +1)
        self.leftViewIMP(root.right, level + 1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.left.right.left.left = Node(9)

t = tree(root)
# t.inOrder(t.getRoot())
# print()
# t.preOrder(t.getRoot())
# print()
# t.postOrder(t.getRoot())
# t.levelOrder(root)
# print(t.heightOfTree(root))
t.leftViewIMP(root, 0)