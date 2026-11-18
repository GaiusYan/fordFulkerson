import heapq
V = {'A', 'B', 'C', 'D', 'E', 'F'}


A = {
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'B'),
    ('C', 'E'),
    ('D', 'C'),
    ('D', 'F'),
    ('E', 'D'),
    ('E', 'F'),
}



c = {
    ('A', 'B'): 16,
    ('A', 'C'): 13,
    ('B', 'D'): 12,
    ('C', 'B'): 4,
    ('C', 'E'): 14,
    ('D', 'C'):  9,
    ('D', 'F'): 20,
    ('E', 'D'):  7,
    ('E', 'F'):  4,
}

flot = {
    ('A', 'B'): 11,
    ('A', 'C'): 8,
    ('B', 'D'): 12,
    ('C', 'B'): 1,
    ('C', 'E'): 11,
    ('D', 'C'): 4,
    ('D', 'F'): 15,
    ('E', 'D'): 7,
    ('E', 'F'): 4,
}


G = V, A, c


""" 
    On considère 
        * G = Le réseau initial
        * G_f = Le réseau résiduel actuel
        

"""

def FordFulkerson(G, source, puits):
    V, A, c = G
    flot = {}
    A_f = set(A)
    c_f = c.copy()

    for (u,v) in A:
        flot[(u,v)] = 0

    G_f = (V, A_f, c_f)
    chemin = cheminAugmentant(G_f, source, puits)

    while chemin is not None:

        # capacite_min = capaciteMinimumChemin(G_f, chemin)
        # flot = flotChemin(chemin, capacite_min)
        flot = augmenterFlot(flot, chemin)
        G_f = mettreAjourResiduel(G_f, chemin)
        chemin = cheminAugmentant(G_f, source, puits)

    return flot

def capaciteMinimumChemin(G_f,chemin) :
    _, _, c_f = G_f

    return min([c_f[u,v] for (u,v) in chemin])

def flotChemin(chemin, capacite_min) :
    flot_p = {}
    for (u,v) in chemin:
        flot[(u,v)] = capacite_min
    return flot_p


def cheminAugmentant(G_f, source, puits):
    return plus_court_chemin(G_f, source, puits)

def mettreAjourResiduel(G_f, chemin):
    V, A_f, c_f = G_f
    for (u,v) in chemin :
        c_f[(u,v)] = c_f[(u, v)] - flot[(u,v)]

        # Arcs saturés
        if c_f[(u,v)] == 0:
            A_f[(u,v)].remove((u,v))
            del c_f[(u,v)]

        # On ajoute un arc inversé pour les chemin dont la valeur de capacité n'est pas min
        if (v,u) not in c_f :
            c_f[(v,u)] = 0

        c_f[(v,u)] = flot[(u,v)]
        A_f.add((v,u))

    G_f = (V, A_f, c_f)
    return G_f

def augmenterFlot(flot, chemin):
    capacite_min = min(c[(u,v)] for (u,v) in chemin)

    for (u,v) in chemin:
        if (u,v) in flot:
            flot[(u,v)] += capacite_min
        else :
            flot[(u,v)] -= capacite_min
    return flot



def voisin(G, u):
    return [v for (x,v) in G if u == x]

def plus_court_chemin(G, u, v):
    parent = {u:u}
    dist = {u:0}
    f = []
    heapq.heappush(f, u)
    while v not in parent and f:
        depart = f.pop()
        for arrivee in voisin(G,depart):
            if arrivee not in parent:
                parent[arrivee] = depart
                dist[arrivee] = dist[depart] + 1
                heapq.heappush(f, arrivee)
    if v not in parent:
        return None
    return reconstuire_chemin(u,v,parent), dist[v]


def reconstuire_chemin(u, v, parent):
    chemin = []
    while v != u:
        u = parent[v]
        chemin.insert(0, (u, v))
        v = u

    return chemin