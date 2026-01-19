import queue

''' A binary tree node has data, pointer to left child
   and a pointer to right child '''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# This function sorts by pushing and popping the
# Cartesian Tree nodes in a pre-order like fashion
def pQBasedTraversal(root):
    # We will use a priority queue to sort the
    # partially-sorted data efficiently.
    # Unlike Heap, Cartesian tree makes use of
    # the fact that the data is partially sorted
    pQueue = queue.PriorityQueue()
    pQueue.put((root.data, root))
    
    # Resembles a pre-order traverse as first data
    # is printed then the left and then right child.
    while not pQueue.empty():
        popped_pair = pQueue.get()
        print(popped_pair[0], end=' ')

        if popped_pair[1].left is not None:
            pQueue.put((popped_pair[1].left.data, popped_pair[1].left))

        if popped_pair[1].right is not None:
            pQueue.put((popped_pair[1].right.data, popped_pair[1].right))

def buildCartesianTreeUtil(root, arr, parent, leftchild, rightchild):
    if root == -1:
        return None

    temp = Node(arr[root])
    temp.left = buildCartesianTreeUtil(leftchild[root], arr, parent, leftchild, rightchild)
    temp.right = buildCartesianTreeUtil(rightchild[root], arr, parent, leftchild, rightchild)

    return temp

# A function to create the Cartesian Tree in O(N) time
def buildCartesianTree(arr, n):
    # Arrays to hold the index of parent, left-child,
    # right-child of each number in the input array
    # Initialize all array values as -1
    parent = [-1] * n
    leftchild = [-1] * n
    rightchild = [-1] * n

    
    ''' 'root' and 'last' stores the index of the root and the
     last processed of the Cartesian Tree.
     Initially we take root of the Cartesian Tree as the
     first element of the input array. This can change
     according to the algorithm '''
    root, last = 0, 0
    
    
    # Starting from the second element of the input array
    # to the last on scan across the elements, adding them
    # one at a time.
    for i in range(1, n):
        last = i-1
        rightchild[i] = -1
            
            
        # Scan upward from the node's parent up to
        # the root of the tree until a node is found
        # whose value is smaller than the current one
        # This is the same as Step 2 mentioned in the
        # algorithm
        while arr[last] >= arr[i] and last != root:
            last = parent[last]

        # arr[i] is the smallest element yet; make it
        # new root
        if arr[last] >= arr[i]:
            parent[root] = i
            leftchild[i] = root
            root = i
        
        
        # Just insert it
        elif rightchild[last] == -1:
            rightchild[last] = i
            parent[i] = last
            leftchild[i] = -1
        
        # Reconfigure links
        else:
            parent[rightchild[last]] = i
            leftchild[i] = rightchild[last]
            rightchild[last] = i
            parent[i] = last
        
    # Since the root of the Cartesian Tree has no
    # parent, so we assign it -1
    parent[root] = -1

    return buildCartesianTreeUtil(root, arr, parent, leftchild, rightchild)


# Sorts an input array
def printSortedArr(arr, n):
    # Build a cartesian tree
    root = buildCartesianTree(arr, n)
    print("The sorted array is-")
    
    # Do pr-order traversal and insert
    # in priority queue
    pQBasedTraversal(root)

# Driver code

    '''  Given input array- {5,10,40,30,28},
        it's corresponding unique Cartesian Tree
        is-

        5
          \
          10
            \
             28
            /
          30
         /
        40
    '''
arr = [5, 10, 40, 30, 28]
n = len(arr)

printSortedArr(arr, n)