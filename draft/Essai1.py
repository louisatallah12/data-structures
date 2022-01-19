class Player(object):
    def __init__(self, score, name = 0):
        self.name = name
        self.cat = None
        self.score = score
        self.left = None
        self.right = None
        self.height = 1

    # __string__ & __repr__ for displaying a player node
    def __string__(self):
        return  self.name
    
    def __repr__(self) : 
        return 'player_'+ str(self.name) + ' '


    def insert(self, player):
        if self.score == player.score:
            return
        elif self.score < player.score:
            if self.right is None:
                self.right = Player(player.score)
            else:
                self.right.insert(player.score)
        else: # self.key > key
            if self.left is None:
                self.left = Player(player.score)
            else:
                self.left.insert(player.score)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
            # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def storeBSTNodes(root,nodes): 
      
    # Base case 
    if not root: 
        return
      
    # Store nodes in Inorder (which is sorted  
    # order for BST)  
    storeBSTNodes(root.left,nodes) 
    nodes.append(root) 
    storeBSTNodes(root.right,nodes) 
  
# Recursive function to construct binary tree  
def buildTreeUtil(nodes,start,end): 
      
    # base case  
    if start>end: 
        return None
  
    # Get the middle element and make it root  
    mid=(start+end)//2
    node=nodes[mid] 
  
    # Using index in Inorder traversal, construct  
    # left and right subtress 
    node.left=buildTreeUtil(nodes,start,mid-1) 
    node.right=buildTreeUtil(nodes,mid+1,end) 
    return node 
  
# This functions converts an unbalanced BST to  
# a balanced BST 
def buildTree(root): 

      
    # Store nodes of given BST in sorted order  
    nodes=[] 
    storeBSTNodes(root,nodes) 
  
    # Constucts BST from nodes[]  
    n=len(nodes) 
    return buildTreeUtil(nodes,0,n-1)

root = None
b = Player(0)
for i in range(1,10) : 
    b.insert(Player(i,i))
b.display()

