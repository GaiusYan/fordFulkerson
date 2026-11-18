from Graphe import *






# pour tout (u, v) element d'un A
# Mon graphe sera représenter de cette manière
#  =
#  graphe = {
#     'S': {'A': (10, 2), 'B': (5, 5)},
#     'A': {'B': (15, 1), 'T': (10, 3)},
#     'B': {'T': (10, 2)},
#     'T': {}
# }
#

# un flot : flot([u,v]) = entier

V = {"A", "B", "C", "D", "E", "F"}

# Cette fonction est OK
def fordFulkerson(G, source, puits) :
    flot = {}
    A = {(u,v) for (u,v) in G.keys()}

    # for (u,v) in A :
    #     flot[(u, v)] = 0
    #
    # G_f = G
    # chemin = cheminAugmentant(G_f, source, puits)
    #
    # while chemin is not None:
    #     flot = augmenterFlot(flot, chemin)
    #     G_f = mettreAjourResiduel(G_f, chemin, flot)
    #     chemin = cheminAugmentant(G_f, source, puits)

    return flot


#
def augmenterFlot(flot, chemin):
    # capacité d'un chemin augmentant
    chemin,_ = chemin

    # Reconstruire le chemin
    chemin = [(chemin[i], chemin[i + 1]) for i in range(len(chemin) - 1)]

    capacite_min = min([graphe[(u,v)][1] for (u,v) in graphe if (u,v) in chemin])

    #flot_min = min(chemin, key=lambda x: graphe[x][1])

    for (u,v) in chemin :
        if (u,v) in flot :
            flot[u, v] += capacite_min
        else :
            flot[u, v] -= capacite_min
    return flot


def mettreAjourResiduel(G_f, chemin, flot_p) :

    #c_f = tuple(G_f[(u, v)][1] for (u, v) in G_f)
    c_f = {(u, v): G_f[(u, v)][1] for (u, v) in G_f}
    A_f = {(u,v) for (u,v) in G_f}

    chemin, _ = chemin
    chemin = [(chemin[i], chemin[i + 1]) for i in range(len(chemin) - 1)]

    for (u,v) in chemin :
        c_f[(u,v)] -= flot_p[(u,v)]

        if c_f[(u,v)] == 0 :
            # A_f =A_f \ {(u, v)}
            A_f.pop()

        if c_f[(v,u)] == 0 :
            # A_f = A_f Union {(u,v)}
            A_f[(u,v)] = c_f[(u,v)]

        c_f[(u,v)] = flot_p[(u,v)]
    return G_f


def cheminAugmentant(G_f, source, puits) :
    return plus_court_chemin(G_f, source, puits)


def plus_court_chemin(G, u, v):
    parent = {u:u}
    dist = {u:0}
    f = []
    # heapq.heappush(f, u)
    # while v not in parent and f:
    #     depart = f.pop()
    #     for arrivee in voisin(G,depart):
    #         if arrivee not in parent:
    #             parent[arrivee] = depart
    #             dist[arrivee] = dist[depart] + 1
    #             heapq.heappush(f, arrivee)
    # if v not in parent:
    #     return None
    return reconstuire_chemin(u,v,parent), dist[v]


def reconstuire_chemin(u, v, parent):
    res = []
    arrivee = v
    while arrivee != u:
        res.insert(0, arrivee)
        arrivee = parent[arrivee]
    res.insert(0, u)
    return res



# sommets adjacents
def voisin(G, u):
    return [v for (x,v) in G if u == x]


graphe = {
    ('A', 'B'): (11, 16),
    ('A', 'C'): (8, 13),
    ('B', 'D'): (12, 12),
    ('C', 'B'): (1, 4),
    ('C', 'E'): (11, 14),
    ('D', 'C'): (4, 9),
    ('D', 'F'): (15, 20),
    ('E', 'D'): (7, 7),
    ('E', 'F'): (4, 4),
}

print(fordFulkerson(graphe, 'A', 'F'))







