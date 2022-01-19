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
    
    

# AVL tree class which supports the 
# Insert operation 
class AVL_Tree_Player(object): 

    # Recursive function to insert player in 
    # subtree rooted with node and returns 
    # new root of subtree.
    def __init__(self):
        self.ROOT = None
        self.players = []

    def insert(self,player):
        self.players.insert(player.name,player)
        return self.insert_aux(self.ROOT,player)

    def insert_aux(self, root, player): 
        # Step 1 - Perform normal BST 
        if not root:
            self.ROOT = player
            return self.ROOT
        elif player.score < root.score: 
            root.left = self.insert_aux(root.left, player) 
        else: 
            root.right = self.insert_aux(root.right, player) 

        # Step 2 - Update the height of the 
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right)) 

        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
        # Step 4 - If the node is unbalanced, 
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and player.score <= root.left.score:
            self.ROOT = self.rightRotate(root)
            return  self.ROOT

        # Case 2 - Right Right 
        if balance < -1 and player.score >= root.right.score: 
            self.ROOT = self.leftRotate(root)
            return  self.ROOT

        # Case 3 - Left Right 
        if balance > 1 and player.score > root.left.score: 
            root.left = self.leftRotate(root.left)
            self.ROOT = self.rightRotate(root)
            return  self.ROOT

        # Case 4 - Right Left 
        if balance < -1 and player.score < root.right.score: 
            root.right = self.rightRotate(root.right)
            self.ROOT = self.leftRotate(root)
            return  self.ROOT

        self.ROOT = root
        return  self.ROOT
    
    def delete(self,player):
        self.players.remove(player)
        return self.delete_aux(self.ROOT,player)

    def delete_aux(self, root, player) : 
        # Step 1 - Perform standard BST delete
        if not root:
            self.ROOT = root
            return self.ROOT
        elif player.score < root.score: 
            root.left = self.delete_aux(root.left, player) 
        elif player.score > root.score: 
            root.right = self.delete_aux(root.right, player) 
        else: 
            if root.left is None and root.right is None :
                if(root == player) : 
                    root = None
                    return None
            if root.left is None: 
                temp = root.right 
                root = None
                self.ROOT = temp
                return self.ROOT
            elif root.right is None: 
                temp = root.left 
                root = None
                self.ROOT = temp
                return self.ROOT 
            temp = self.getMinValueNode(root.right) 
            root.score = temp.score 
            root.right = self.delete_aux(root.right, 
                                      temp) 
  
        # If the tree has only one node, 
        # simply return it 
        if root is None:
            self.ROOT = root 
            return self.ROOT
  
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
            self.ROOT =  self.rightRotate(root) 
            return self.ROOT
  
        # Case 2 - Right Right 
        if balance < -1 and self.getBalance(root.right) <= 0:
            self.ROOT = self.leftRotate(root) 
            return self.ROOT
  
        # Case 3 - Left Right 
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left)
            self.ROOT = self.rightRotate(root)
            return self.ROOT
  
        # Case 4 - Right Left 
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right)
            self.ROOT = self.leftRotate(root)
            return  self.ROOT
        self.ROOT = root
        return self.ROOT 

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

    def getBalance(self, node): 
        if not node: 
            return 0

        return self.getHeight(node.left) - self.getHeight(node.right) 

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

    def getMinValue(self, root) :
        if root is None or root.left is None: 
            return root.score
  
        return self.getMinValue(root.left) 
        
    def preOrder(self, root): 
        
        if not root: 
            return

        print("{0} ".format(root.score), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 

    def display(self):
        if self.ROOT is None:
            print("Sorry nothing to show :p")
        else:
            lines, *_ = self._display_aux(self.ROOT)
            for line in lines:
                print(line)

    def _display_aux(self, root):

        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if root is None:
            print("sorry nothing to show !!!")
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
def Get_Player_In_Dict(id, tree) :
    i=0
    var = 0
    dico = {}
    for j in tree.players : 
        dico[j]=j.score
    for k in dico.keys():
        if i == id :
            var = k
        i = i+1
    return var        # returns the player whose player.name = id

#--4-- update the score in the database and in the dictionnary
def setScoreInTree(player,newscore,tree):
    new_name = player.name
    tree.delete(player)
    player2 = Player(newscore,new_name)
    tree.insert(player2)




#--5-- Simulation of random games
def Simulate_Random_Game(tree) :
    players = []
    games = []
    count = 1
    dico ={}
    for j in tree.players : 
        dico[j]=j.score
    while count<3 :             # simulation of 3 games
        for k in dico.keys() : 
            players.append(k)
        for i in range(0,len(tree.players),10) : 
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
    
    """laliste = tree.players 
    for i in laliste : 
        setScoreInTree(i, dico[i], tree)"""
#Simulate_Random_Game()

# Second method for question 4 based on the database :
def Simulate_Random_Game_2(tree) : 
    players = []
    games = []
    count = 1
    dico = {}
    for j in tree.players : 
        dico[j]=j.score
    while count<3 :             # simulation of 3 games
        index_impostor = rd.sample(range(0, len(tree.players)), len(tree.players))
        for i in range(len(index_impostor)) :
            players.append(Get_Player_In_Dict(index_impostor[i],tree))
        
        for i in range(0,len(tree.players),10) : 
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
    """laliste = tree.players 
    for i in laliste : 
        setScoreInTree(i, dico[i], tree)"""
#Simulate_Random_Game_2()


from collections import OrderedDict     # to have a sorted dictionnary and keep the same format as a dictionnary

#--6-- Simulates games based on ranking
def Simulate_Ranking_Game(tree) :
    players = []
    games = []
    count = 1
    dico = {}
    
    while count<3 : # simulation of 3 games
        for j in tree.players : 
            dico[j]=j.score
        dico_sorted = OrderedDict(sorted(dico.items(), key=lambda t: t[1]))
        for k in dico_sorted.keys() : 
            players.append(k)
        for i in range(0,len(tree.players),10) : 
            games.append(players[i:i+10])

        for liste in games : 
        
            for i in range(len(liste)) :                    # by default we initialize every players with the Crewmate class
                liste[i].cat = "Crewmate"
        
            index_impostor = rd.sample(range(0, len(liste)), 2)

            for i in range(2):                              # for 2 of them they will be Impostors
                liste[index_impostor[i]].cat = "Impostor"
           
        
            win = rd.getrandbits(1)                     # random victory or loss 
            r_boolean = bool(win)
            
            for i in range(len(liste)) : 
                s = int((dico[liste[i]]+Random_Score(liste[i], r_boolean))/count)
                liste[i].score = s          # the score is mean of the several games
                dico[liste[i]] = liste[i].score
                
        count = count +1
    """laliste = tree.players 
    for i in laliste : 
        setScoreInTree(i, dico[i], tree)"""
        
#Simulate_Ranking_Game()

#dico_sorted = OrderedDict(sorted(dico.items(), key=lambda t: t[1]))


"""def Drop_Last_Ten(tree) : 
    the_scores = {}
    for p in tree.players : 
        the_scores[p]=p.score
    sorted_scores = OrderedDict(sorted(the_scores.items(), key=lambda t: t[1]))

    c = 0
    for i in sorted_scores : 
        Tree.delete(i)
        c=c+1
        if c==10:
            break"""
    


#--8-- Display for the final
def Display_Top_Players(tree) :
    dico = {}
    for j in tree.players : 
        dico[j]=j.score
    dico_sorted = sorted(dico.items(), key=lambda t: t[1])
    top_players = []
    print()
    print("******Voici le top 10 des joueur*******")
    print()
    place = 1
    print("rk  :  Player     -  Points ")
    print()
    for i in range(len(tree.players)-1,len(tree.players)-10,-1) : 
        top_players.append(dico_sorted[i])
        if place < 4 :
            print(place,"  : ", dico_sorted[i][0]," - ",dico_sorted[i][1], "    PODIUM ! ")
            print()
        else :
            print(place,"  : ", dico_sorted[i][0]," - ",dico_sorted[i][1])
            print()
        place = place + 1

def Drop_Last_Ten(tree) : 
    for i in range(10) : 
        print(tree.getMinValue(tree.ROOT))
        print(tree.players)
        print(tree.search(tree.ROOT,tree.getMinValue(tree.ROOT)))
        tree.delete(tree.search(tree.ROOT,tree.getMinValue(tree.ROOT)))
    

def balance_tree(array):
    '''
    Balances an unbalanced binary tree in O(n) time from the inorder traversal
    stored in an array
    steps:
        - Take inorder traversal of existing tree and store in array.
        - Find value at mid point of this array.  
        - create new binary tree using this midpoint as root node.
    '''
    if not array:
        return None
        
    midpoint = len(array) // 2
    new_root = Player(array[midpoint])
    new_root.left = balance_tree(array[ : midpoint])
    new_root.right = balance_tree(array[midpoint + 1 :])
    return new_root 

#--Step 2-- 

#--1--
player_0 = Player(0, 0)
player_1 = Player(0, 1)
player_2 = Player(0, 2)
player_3 = Player(0, 3)
player_4 = Player(0, 4)
player_5 = Player(0, 5)
player_6 = Player(0, 6)
player_7 = Player(0, 7)
player_8 = Player(0, 8)
player_9 = Player(0, 9)
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
graph2 = {0 : [1,4,5],
        1 : [0, 2, 6],
        2 : [1, 3, 7],
        3 : [2, 4, 8],
        4 : [0, 3, 9],
        5 : [0, 7, 8],
        6 : [1, 8, 9],
        7 : [2, 5, 9],
        8 : [3, 5, 6],
        9 : [4, 6, 7]}

#--4--
# method to find the impostors after a death
def Find_Impostors(dead_player) :
    suspects = graph2[dead_player.name]   # suspects are the players who have met the dead player

    dico2 = graph2
    dico_color = g1.coloration()
    for suspect in suspects :
        print()
        print("if Player "+str(suspect)+ " is an impostor, the other one is one of them : ")
        for k in dico_color.keys() :
            if dico_color[k] != dico_color[suspect] and k not in dico2[suspect] and not dead_player.name :  # if the node is not the same colour nor a neighbor  and not the dead player 
                print("  Player "+str(k), end = ", ")
        print()
    

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v):
        self.graph.append([u.name, v.name])
    def __str__(self) : 
        return str(self.graph)
    def __repr__(self) : 
        return str(self.graph)

    def coloration(self) : 
        # initializing the color list of -1 (uncolored) of each vertex
        colour = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        
        colour[0] = 0 #assignation of the first colour to the first node
        # temporary list of colors for the neighbor nodes
        temp =[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        
        for i in range(0,30,3) :    # there are 30 lists in the graph 
            
            # if the node is colored
            if colour[self.graph[i][0]] != -1 : 
                temp[self.graph[i][0]] = colour[self.graph[i][0]] # store the color in temp
            
            # if the node is not colored
            if colour[self.graph[i][1]] == -1 :
                # store the neighbors' colors in temp 
                temp.extend([colour[self.graph[3*self.graph[i][1]][1]], colour[self.graph[3*self.graph[i][1]+1][1]], colour[self.graph[3*self.graph[i][1]+2][1]]])
                for k in range(4) : 
                    if k not in temp : # assign the color not present in temp (i.e not already used by a neighbor)
                        colour[self.graph[i][1]] = k
                        break
                temp =[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
                temp[self.graph[i][0]] = colour[self.graph[i][0]]

            if colour[self.graph[i+1][1]] == -1 :
                temp.extend([colour[self.graph[3*self.graph[i+1][1]][1]], colour[self.graph[3*self.graph[i+1][1]+1][1]], colour[self.graph[3*self.graph[i+1][1]+2][1]]])

                for k in range(4) : 
                    if k not in temp : 
                        colour[self.graph[i+1][1]] = k
                        break
                temp =[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
                temp[self.graph[i][0]] = colour[self.graph[i][0]]

            if colour[self.graph[i+2][1]] == -1 :
                temp.extend([colour[self.graph[3*self.graph[i+2][1]][1]], colour[self.graph[3*self.graph[i+2][1]+1][1]], colour[self.graph[3*self.graph[i+2][1]+2][1]]])

                for k in range(4) : 
                    if k not in temp : 
                        colour[self.graph[i+2][1]] = k
                        break
                temp =[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

            temp[self.graph[i][0]] = -1

        for i in range(10) : 
            print("Player "+str(i)+" ----> "+str(colour[i]))
        dico = {}
        for i in range(10) : 
            dico[i] = colour[i]
        return dico

g1 = Graph(10)
for k in graph : 
    for i in range(3) :
        g1.add_edge(k, graph[k][i])


#--STEP 3--
# We will proceed with 2 maps
# one as a crewmate and the other one as an impostor with the vents
# We have chosen the Floyd Warshall algorithm to find the shortest path between a pair of rooms 

INF = 1000000000  # We compute a very big number to fill in the matrix

class Graph_FloydWarshall(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[INF for column in range(vertices)]     # initializing the matrix with full of INF (we will use INF if there is no edge)
                    for row in range(vertices)] 
        # fill the digonale with 0
        for i in range(14) :
            self.graph[i][i] = 0        
            
    def floyd_warshall(self):
        # calculating all pair shortest path
        for k in range(0, self.V):
            for i in range(0, self.V):
                for j in range(0, self.V):
                    # let's take the minimum distance between the direct path and the intermediate
                    self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])
        # display
        print("start/end", end='')
        for i in range(self.V):
            print("    {:s}".format(rooms[i]), end=' ')
        print()
        for i in range(self.V):
            print("%-17s"%rooms[i], end='')
            for j in range(self.V):
                print("%-12s"% f"{self.graph[i][j]:.1f}", end='')
            print()


g_dijkstra_crewmate = Graph_FloydWarshall(14)
# Below the index of the rooms :
rooms = {0 : "Reactor" ,
        1 : "Upper E", 
        2 : "Lower E", 
        3 : "Security",
        4 : "Medbay",
        5 : "Electrical",
        6 : "Cafeteria",
        7 : "Storage",
        8 : "Unkown1",
        9 : "Unknown2",
        10 : "O2",
        11 : "Weapon",
        12 : "Navigation",
        13 : "Shield"}
# edge of the Reactor room 
g_dijkstra_crewmate.graph[0][1] = 2.5
g_dijkstra_crewmate.graph[0][3] = 2.5
g_dijkstra_crewmate.graph[0][2] = 2.5
# edge of the Upper E room 
g_dijkstra_crewmate.graph[1][0] = 2.5 
g_dijkstra_crewmate.graph[1][2] = 4 
g_dijkstra_crewmate.graph[1][3] = 2.5 
g_dijkstra_crewmate.graph[1][4] = 3 
g_dijkstra_crewmate.graph[1][6] = 4.5 
# edge of the Lower E room 
g_dijkstra_crewmate.graph[2][0] = 2.5
g_dijkstra_crewmate.graph[2][1] = 4
g_dijkstra_crewmate.graph[2][3] = 2.5
g_dijkstra_crewmate.graph[2][5] = 3.5
g_dijkstra_crewmate.graph[2][7] = 6
# edge of the Security room
g_dijkstra_crewmate.graph[3][0] = 2.5
g_dijkstra_crewmate.graph[3][1] = 2.5
g_dijkstra_crewmate.graph[3][2] = 2.5
# edge of the Medbay room
g_dijkstra_crewmate.graph[4][1] = 3 
g_dijkstra_crewmate.graph[4][6] = 1.5
# edge of the Electrical room
g_dijkstra_crewmate.graph[5][2] = 3.5
g_dijkstra_crewmate.graph[5][7] = 2.5
# edge of the Cafeteria room 
g_dijkstra_crewmate.graph[6][1] = 4.5
g_dijkstra_crewmate.graph[6][4] = 1.5
g_dijkstra_crewmate.graph[6][7] = 2
g_dijkstra_crewmate.graph[6][8] = 2
g_dijkstra_crewmate.graph[6][11] = 1
# edge of the Storage room
g_dijkstra_crewmate.graph[7][2] = 6 
g_dijkstra_crewmate.graph[7][5] = 2.5 
g_dijkstra_crewmate.graph[7][6] = 2
g_dijkstra_crewmate.graph[7][8] = 1.5 
g_dijkstra_crewmate.graph[7][9] = 2.5
# edge of the Unknown1 room 
g_dijkstra_crewmate.graph[8][6] = 2
g_dijkstra_crewmate.graph[8][7] = 1.5
# edge of the Unkown2 room
g_dijkstra_crewmate.graph[9][7] = 2.5
g_dijkstra_crewmate.graph[9][13] = 1
# edge of the O2 room
g_dijkstra_crewmate.graph[10][11] = 2
g_dijkstra_crewmate.graph[10][12] = 4
g_dijkstra_crewmate.graph[10][13] = 4
# edge of the Weapon room 
g_dijkstra_crewmate.graph[11][6] = 1 
g_dijkstra_crewmate.graph[11][10] = 2 
g_dijkstra_crewmate.graph[11][12] = 4.5
# edge of the Navigation room
g_dijkstra_crewmate.graph[12][10] = 4
g_dijkstra_crewmate.graph[12][11] = 4.5
g_dijkstra_crewmate.graph[12][13] = 4.5
# edge of the Shield room
g_dijkstra_crewmate.graph[13][9] = 1
g_dijkstra_crewmate.graph[13][10] = 4
g_dijkstra_crewmate.graph[13][12] = 4.5
import copy
### Rooms with the vents 
g_dijkstra_impostor = Graph_FloydWarshall(14)
g_dijkstra_impostor.graph = copy.deepcopy(g_dijkstra_crewmate.graph)

"modifying the edge weights because of the vents"
# {Reactor , Upper E}
g_dijkstra_impostor.graph[0][1] = 0
g_dijkstra_impostor.graph[1][0] = 0
# {Reactor , Lower }
g_dijkstra_impostor.graph[0][2] = 0
g_dijkstra_impostor.graph[2][0] = 0
# {Medbay , Security}
g_dijkstra_impostor.graph[4][3] = 0
g_dijkstra_impostor.graph[3][4] = 0
# {Medbay , Electrical}
g_dijkstra_impostor.graph[4][5] = 0
g_dijkstra_impostor.graph[5][4] = 0
# {Security , Medbay}
g_dijkstra_impostor.graph[3][5] = 0
g_dijkstra_impostor.graph[5][3] = 0
# {Cafeteria , Unknown1}
g_dijkstra_impostor.graph[8][6] = 0
g_dijkstra_impostor.graph[6][8] = 0
# {Cafeteria , O2}
g_dijkstra_impostor.graph[6][10] = 3
g_dijkstra_impostor.graph[10][6] = 3
# {Cafeteria , Shield}
g_dijkstra_impostor.graph[6][13] = 2
g_dijkstra_impostor.graph[13][6] = 2
# {Cafeteria , Navigation}
g_dijkstra_impostor.graph[6][12] = 3.5
g_dijkstra_impostor.graph[12][6] = 3.5
# {Cafeteria , Weapon}
g_dijkstra_impostor.graph[6][11] = 3.5
g_dijkstra_impostor.graph[11][6] = 3.5

# {Unknonw1 , O2}
g_dijkstra_impostor.graph[8][10] = 3
g_dijkstra_impostor.graph[10][8] = 3
# {Unknown1 , Shield}
g_dijkstra_impostor.graph[8][13] = 2
g_dijkstra_impostor.graph[13][8] = 2
# {Unknown1 , Navigation}
g_dijkstra_impostor.graph[8][12] = 3.5
g_dijkstra_impostor.graph[12][8] = 3.5
# {Unknown1 , Weapon}
g_dijkstra_impostor.graph[8][11] = 3.5
g_dijkstra_impostor.graph[11][8] = 3.5

# {Weapon , Navigation}
g_dijkstra_impostor.graph[12][11] = 0
g_dijkstra_impostor.graph[11][12] = 0
#{Navigation , Shield}
g_dijkstra_impostor.graph[12][13] = 0
g_dijkstra_impostor.graph[13][12] = 0

#--step 4--
# We take the crewmate map for exploring all vertices
# We willuse a variante of the Hamiltonian path 
# It is the same algorithm but we have removed the link between the final node and the starting node

class Graph_Hamilton():  
    
    def __init__(self, vertices):  
        self.graph = []  
        self.V = vertices  
  
    # method that verifies the adjacency and whether v is not already in the path
    def check(self, v, position, path):    
        # the adjacency
        if self.graph[ path[position-1] ][v] == 0:  
            return False
  
        # if v not already in path  
        for vertex in path:  
            if vertex == v:  
                return False
        return True
  
    def Hamilton_aux(self, path, position):  
        # if it is the final vertice
        if position == self.V:  
            return True

        # Let's have a look at the next room to visit
        # List of all rooms
        # We exclude the room 4 because it is the starting one  
        liste = [0,1,2,3,5,6,7,8,9,10,11,12,13]

        # Foreach vertice we assign its position
        for v in liste:  
            if self.check(v, position, path) == True:  
                path[position] = v  
                
                if self.Hamilton_aux(path, position+1) == True:  
                    return True
        
        return False
  
    def Hamilton(self):  
        # path is a list of V elements initialized at -1
        path = [-1] * self.V  
        # starting vertice is 4 (Medbay)
        path[0] = 4

        if self.Hamilton_aux(path,1) == False:  
            print ("Sorry, there is no such path") 
            return False
        else : 
            self.display(path)  
            return True
  
    def display(self, path):  
        print ("The route passing through each room is : ") 
        for vertex in path:  
            print ("->",rooms[vertex], end = " ") 

gh1 = Graph_Hamilton(14)
# We retake the crewmate map 
gh1.graph = copy.deepcopy(g_dijkstra_crewmate.graph)
# let's preprossessing the map by replacing the INF and non-zero values :
for i in range(14) : 
    for j in range(14) : 
        if gh1.graph[i][j] == INF : 
            gh1.graph[i][j] = 0

for i in range(14) : 
    for j in range(14) : 
        if gh1.graph[i][j] != 0 : 
            gh1.graph[i][j] = 1



if __name__=='__main__':
    
    import random as rd
    
    # for k in graph.keys() : 
    #     print(str(k)+" has seen "+ str(graph[k]))
    # print()
    #--step 2--
    # print(g1)
    # dico = g1.coloration()
    # print(dico)
    #Find_Impostors(player_0)
    #--step 3--
    for item in rooms.items() : 
        print(item)
    
    # print()
    # g_dijkstra_impostor.floyd_warshall()
    #g_dijkstra_crewmate.floyd_warshall()

    #--step3--
    gh1.Hamilton()
    