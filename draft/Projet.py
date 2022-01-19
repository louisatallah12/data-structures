
class Player(object):
    def __init__(self, score):
        self.name = 0
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

# AVL tree class which supports the 
# Insert operation 
class AVL_Tree_Player(object): 

    # Recursive function to insert player in 
    # subtree rooted with node and returns 
    # new root of subtree. 

    def insert(self, root, player): 
        # Step 1 - Perform normal BST 
        if not root:
            return player 
        elif player.score < root.score: 
            root.left = self.insert(root.left, player) 
        else: 
            root.right = self.insert(root.right, player) 

        # Step 2 - Update the height of the 
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right)) 

        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
        # Step 4 - If the node is unbalanced, 
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and player.score < root.left.score: 
            return self.rightRotate(root) 

        # Case 2 - Right Right 
        if balance < -1 and player.score > root.right.score: 
            return self.leftRotate(root) 

        # Case 3 - Left Right 
        if balance > 1 and player.score > root.left.score: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 

        # Case 4 - Right Left 
        if balance < -1 and player.score < root.right.score: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 

        return root 
    

    def delete(self, root, player) : 
        # Step 1 - Perform standard BST delete
        if not root: 
            return root 
        elif player.score < root.score: 
            root.left = self.delete(root.left, player) 
        elif player.score > root.score: 
            root.right = self.delete(root.right, player) 
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
            temp = self.getMinValueNode(root.right) 
            root.score = temp.score 
            root.right = self.delete(root.right, 
                                      temp) 
  
        # If the tree has only one node, 
        # simply return it 
        if root is None: 
            return root 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                            self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and self.getBalance(root.left) >= 0: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and self.getBalance(root.right) <= 0: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
        return root 

    def leftRotate(self, z): 

        y = z.right 
        T2 = y.left 

        # Perform rotation 
        y.left = z 
        z.right = T2 

        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
        self.getHeight(y.right)) 

        # Return the new root 
        return y 

    def rightRotate(self, z): 

        y = z.left
        T3 = y.right 

        # Perform rotation 
        y.right = z 
        z.left = T3 

        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
        self.getHeight(y.right)) 

        # Return the new root 
        return y 

    def getHeight(self, root): 
        if not root: 
            return 0

        return root.height 

    def getBalance(self, root): 
        if not root: 
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right) 

    # method that reaches the minimum node
    def getMinValueNode(self, root): 
        if root is None or root.left is None: 
            return root 
  
        return self.getMinValueNode(root.left) 
    
    # method that reaches the maximum node
    def getMaxValueNode(self, root) :
        if root is None or root.right is None :
            return root
        
        return self.getMaxValueNode(root.right) 

    def preOrder(self, root): 
        
        if not root: 
            return

        print("{0} ".format(root.score), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 
    
    def display(self, root):
        if root is None:
            print("Sorry nothing to show")
        else:
            lines, *_ = self._display_aux(root)
            for line in lines:
                print(line)

    def _display_aux(self, root):

        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if root is None:
            print("sorry nothing to show")
        elif root.right is None and root.left is None:
            line = '%s' % root.score
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if root.right is None:
            lines, n, p, x = self._display_aux(root.left)
            s = '%s' % root.score
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if root.left is None:
            lines, n, p, x = self._display_aux(root.right)
            s = '%s' % root.score
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
            # Two children.
        left, n, p, x = self._display_aux(root.left)
        right, m, q, y = self._display_aux(root.right)
        s = '%s' % root.score
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

    # method that checks whether a value is in the database 
    # To search a player according to his score
    def search(self,root_node,value):
        if root_node.score == value:
            return root_node
        elif root_node.right is not None and root_node.score < value:
            return self.search( root_node.right,value)
        elif root_node.left is not None and root_node.score > value:
            return self.search( root_node.left,value)
        else:
            return None
    
    # To search a player's score  
    def search_node(self,root_node, player):
        print("HEY")

        if  root_node.name == player.name :
            return root_node
        if root_node.right is not None :
            return self.search_node( root_node.right,player)
        if root_node.left is not None :
            return self.search_node( root_node.left,player)
        else:
            return None
        return root_node

# To balance the tree
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

#--3-- method that attributes a random score between 0 and 12 for each player in the game    
def Random_Score(player, win_Crewmate) : 
    if player.cat == "Impostor" : 
        
        if win_Crewmate == False : 
            return rd.choice( range(10,13) )  # if the impostors win, 10 points for victory at least
        
        else : 
            return rd.choice(range(0,10)) # score between 0 and 8 (amid kills & undiscovered murders)
    
    elif player.cat == "Crewmate" : 
        
        if win_Crewmate == True : 
            return rd.choice(range(5,13)) # Crewmates win = 5 points up to 12 points

        else : 
            return rd.choice([1,3,4]) # Crewmate loss represents 1 (solo task achieved) 3(1 of 2 impostors demasked) 4 (if they both did the task and find the impostor)
    
    else : 
        print("Give a player type please")  
        return None

# method that enables to get the score by the player's name entity in the dico
def Get_Player_In_Dict(id) :
    i=0
    var = 0
    for k in dico.keys():
        if i == id :
            var = k
        i = i+1
    return var        # returns the player whose player.name = id

#--4-- update the score in the database and in the dictionnary
"""def Update_Score(root, id, new_score) : 

    play = Get_Player_In_Dict(id)
    print(play)

    Tree.delete(root, play)

    print(play)
    play.score = new_score

    dico[play] = play.score
    root = Tree.insert(root, play)
    print("Tree updated")
"""

Tree = AVL_Tree_Player()
root = None
import random as rd

#--1-- We have picked a dictionnary to store the players and their scores 
dico = {}

for i in range(100):
    player = Player(0)
    
    player.name = i
    dico[player] = player.score
    root = buildTree(root)
    root = Tree.insert(root,player)

Tree.display(root)
print(dico)
print()
root = buildTree(root)


#--5-- Simulation of random games
def Simulate_Random_Game() :
    players = []
    games = []
    count = 1
    while count<3 :             # simulation of 3 games
        for k in dico.keys() : 
            players.append(k)
        for i in range(0,100,10) : 
            games.append(players[i:i+10])

        for liste in games : 
        
            for i in range(len(liste)) :                    # by default we initialize every players with the Crewmate class
                liste[i].cat = "Crewmate"
        
            index_impostor = rd.sample(range(0, 10), 2)

            for i in range(2):                              # for 2 of them they will be Impostors
                liste[index_impostor[i]].cat = "Impostor"
           
        
            win = rd.getrandbits(1)                     # random victory or loss 
            r_boolean = bool(win)
        
            for i in range(len(liste)) : 
            
                liste[i].score = int((dico[liste[i]]+Random_Score(liste[i], r_boolean))/count)          # the score is mean of the several games
                dico[liste[i]] = liste[i].score
        count = count +1
        
Simulate_Random_Game()

# Second method for question 4 based on the database :
def Simulate_Random_Game_2() : 
    players = []
    games = []
    count = 1
    while count<3 :             # simulation of 3 games
        index_impostor = rd.sample(range(0, 100), 100)
        for i in range(len(index_impostor)) :
            players.append(Get_Player_In_Dict(index_impostor[i]))
        
        for i in range(0,100,10) : 
            games.append(players[i:i+10])

        for liste in games : 
        
            for i in range(len(liste)) :                    # by default we initialize every players with the Crewmate class
                liste[i].cat = "Crewmate"
        
            index_impostor = rd.sample(range(0, 10), 2)

            for i in range(2):                              # for 2 of them they will be Impostors
                liste[index_impostor[i]].cat = "Impostor"
           
        
            win = rd.getrandbits(1)                     # random victory or loss 
            r_boolean = bool(win)
        
            for i in range(len(liste)) : 
            
                liste[i].score = int((dico[liste[i]]+Random_Score(liste[i], r_boolean))/count)          # the score is mean of the several games
                dico[liste[i]] = liste[i].score
        count = count +1   

#Simulate_Random_Game_2()


from collections import OrderedDict     # to have a sorted dictionnary and keep the same format as a dictionnary

#--6-- Simulates games based on ranking
def Simulate_Ranking_Game() :
    players = []
    games = []
    count = 1
    while count<3 :             # simulation of 3 games
        dico_sorted = OrderedDict(sorted(dico.items(), key=lambda t: t[1]))
        for k in dico_sorted.keys() : 
            players.append(k)
        for i in range(0,100,10) : 
            games.append(players[i:i+10])

        for liste in games : 
        
            for i in range(len(liste)) :                    # by default we initialize every players with the Crewmate class
                liste[i].cat = "Crewmate"
        
            index_impostor = rd.sample(range(0, 10), 2)

            for i in range(2):                              # for 2 of them they will be Impostors
                liste[index_impostor[i]].cat = "Impostor"
           
        
            win = rd.getrandbits(1)                     # random victory or loss 
            r_boolean = bool(win)
        
            for i in range(len(liste)) : 
            
                liste[i].score = int((dico[liste[i]]+Random_Score(liste[i], r_boolean))/count)          # the score is mean of the several games
                dico[liste[i]] = liste[i].score
        count = count +1
        
#Simulate_Ranking_Game()

dico_sorted = OrderedDict(sorted(dico.items(), key=lambda t: t[1]))


def Drop_Last_Ten() : 
    for i in range(10) : 
        min_node = Tree.getMinValueNode(root)
        Tree.delete(root, min_node)
#Drop_Last_Ten()
#buildTree(root)
print()
root = buildTree(root)
Tree.display(root)
print()
print(dico_sorted)
print()

#--8-- Display for the final
def Display_Top_Players() :
    dico_sorted = sorted(dico.items(), key=lambda t: t[1])
    top_players = []
    print()
    print("******Voici le top 10 des joueur*******")
    print()
    place = 1
    print("rk  :  Player     -  Points ")
    print()
    for i in range(99,89,-1) : 
        top_players.append(dico_sorted[i])
        if place < 4 :
            print(place,"  : ", dico_sorted[i][0]," - ",dico_sorted[i][1], "    PODIUM ! ")
            print()
        else :
            print(place,"  : ", dico_sorted[i][0]," - ",dico_sorted[i][1])
            print()
        place = place + 1
#Display_Top_Players()

print(Tree.getMinValueNode(root))
print(dico[Get_Player_In_Dict(0)])

#--Step 2-- 

#--1--
player_0 = Player(0)
player_0.name = 0
player_1 = Player(0)
player_1.name = 1
player_2 = Player(0)
player_2.name = 2
player_3 = Player(0)
player_3.name = 3
player_4 = Player(0)
player_4.name = 4
player_5 = Player(0)
player_5.name = 5
player_6 = Player(0)
player_6.name = 6
player_7 = Player(0)
player_7.name = 7
player_8 = Player(0)
player_8.name = 8
player_9 = Player(0)
player_9.name = 9
graph = {player_0 : [player_1,player_4,player_5],
            player_1 : [player_0, player_2, player_6],
            player_2 : [player_1, player_3, player_7],
            player_3 : [player_2, player_4, player_8],
            player_4 : [player_0, player_3, player_9],
            player_5 : [player_0, player_7, player_8],
            player_6 : [player_1, player_8, player_9],
            player_7 : [player_2, player_5, player_9],
            player_8 : [player_3, player_5, player_6],
            player_9 : [player_4, player_6, player_7]}
for k in graph.keys() : 
    print(str(k)+" has seen "+ str(graph[k]))
print()

# method to find the impostors after a death
def Find_Impostors(dead_player) :

    suspects = graph[dead_player]   # suspects are the players who have met the dead player
    print("suspects are "+str(suspects))
    print()
    print("if "+str(suspects[0])+ " is an impostor, the other one is one of them : "+str(set(graph[suspects[1]])^set(graph[suspects[2]])))      # the operation ^ selects the non common elements in the 2 sets
    print()                                                                                                                                     # it enables to exclude the dead player who is obviously not an impostor
    print("if "+str(suspects[1])+ " is an impostor, the other one is one of them : "+str(set(graph[suspects[0]])^set(graph[suspects[2]])))
    print()
    print("if "+str(suspects[2])+ " is an impostor, the other one is one of them : "+str(set(graph[suspects[1]])^set(graph[suspects[0]])))
    print()

Find_Impostors(player_0)

