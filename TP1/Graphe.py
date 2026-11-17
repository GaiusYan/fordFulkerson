import heapq

class Graphe():
    def __init__(self, matrice_adjacence=None):
        # si la matrice d'adjacence n'est pas donnée
        # on initialise le graphe sans aucun noeud
        # On veut utiliser la représentation sous
        # forme de dictionnaire, même quand une matrice 
        # est donnée
        
        # TODO
        self.arcs = {}
        self.nb_arete= 0
        self.cout = 0
        
        if matrice_adjacence:
            for i in range(len(matrice_adjacence)):
                self.arcs[i] = {}
                for j in range(len(matrice_adjacence[i])):
                    if matrice_adjacence[i][j]:
                        self.arcs[i][j] = True
                        self.nb_arete = self.nb_arete + 1
                    
        
    
    def ajouter_noeud(self,u):
    # doit ajouter u  au graphe si celui-ci n'existe pas
    # ne fait rien si il existe déjà
        if u not in self.arcs:
            self.arcs[u] = {}

    def noeuds(self):
    # renvoie une vue des noeuds : un test d'appartenance
    # doit fonctionner en O(1) et on doit pouvoir
    # itérer sur les noeuds en faisant for ... in graphe.noeuds()
        return list(self.arcs.keys())

    def ajouter_arete(self,u,v):
    # ajoute l'arête de u à v
    # on suppose que u et v existent
        self.ajouter_noeud(u)
        self.ajouter_noeud(v)
        if v not in self.arcs[u]:
            self.nb_arete = self.nb_arete + 1
            self.arcs[u][v] = True

    def enlever_arete(self,u,v):
        if v in self.arcs[u]:
            self.nb_arete = self.nb_arete - 1
            del self.arcs[u][v]
        
    def enlever_noeud(self,u):
    # enlève le noeud u, pour garder la consistence,
    # enlève toutes les arêtes de et vers u
        self.nb_arete = self.nb_arete - len(self.arcs[u])
        for v in self.arcs:
            if u in self.arcs[v]:
                del self.arcs[v][u]
                self.nb_arete -= 1
        del self.arcs[u]

    def voisins(self,u):
    # renvoie une vue sur les voisins de u
        if u in self.arcs:
            return list(self.arcs[u].keys())
        return []

    def nb_sommets(self):
    # renvoie le nombre de sommets
        return len(self.arcs.keys())

    def nb_aretes(self):
    # renvoie le nombre d'arêtes
        return self.nb_arete

    def export_matrice(self):
    # renvoie une matrice d'adjacence pour
    # le graphe et un dictionnaire qui associe les
    # noms/identifiants aux indices correspondants 
    # de la matrice
        res = []
        dico = {}
        
        i = 0
        for u in self.noeuds():
            dico[u] = i
            i = i+1
        for u in self.noeuds():
            res.append([0 for j in range(self.nb_sommets())])
            for v in self.arcs[u]:
                res[dico[u]][dico[v]] = 1
        return res, dico
    
    def reconstuire_chemin(self, u, v, parent):
        res = []
        arrivee = v
        while arrivee != u:
            res.insert(0, arrivee)
            arrivee = parent[arrivee]
        res.insert(0, u)
        return res
               
    def plus_court_chemin(self, u, v):
        parent = {u:u}
        dist = {u:0}
        f = []
        heapq.heappush(f, u)
        while v not in parent and f:
            depart = f.pop()
            for arrivee in self.voisins(depart):
                if arrivee not in parent:
                    parent[arrivee] = depart
                    dist[arrivee] = dist[depart] +1
                    heapq.heappush(f, arrivee)
        if v not in parent:
            return None
        return self.reconstuire_chemin(u,v,parent), dist[v]
            
