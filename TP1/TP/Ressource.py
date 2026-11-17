import heapq



# pour tout (u, v) element d'un A
# un chemin : chemin([u,v]) = {flot, cout}

# un flot : flot([u,v]) = entier

V = {"A", "B", "C", "D", "E", "F"}
A = {
    ("A", "B") : [11,16],
    ("A", "C"): [8, 13],
    ("B", "D"): [12, 12],
    ("C", "B"): [1, 4],
    ("C", "E"): [11, 14],
    ("D", "C"): [4, 9],
    ("D", "F"): [15, 20],
    ("E", "D"): [7, 7],
    ("E", "F"): [4, 4],
}
G = V,A
def fordFulkerson(G, source, puits) :
    flot = {}
    V, A = G

    for (u,v) in A :
        flot[(u, v)] = 0

    G_f = G
    chemin = cheminAugmentant(G_f, source, puits)

    while chemin is not None:
        flot = augmenterFlot(flot, chemin)
        G_f = mettreAjourResiduel(G, G_f, chemin, flot)
        chemin = cheminAugmentant(G_f, source, puits)

    return flot


#
def augmenterFlot(flot, chemin):
    # capacité d'un chemin augmentant
    capacite_min = min(chemin, key= lambda x : chemin[x][1])

    for (u,v) in chemin :
        if (u,v) in flot :
            flot[u, v] += capacite_min
        else :
            flot[u, v] -= capacite_min
    return flot


def mettreAjourResiduel(G_f, chemin, flot_p) :
    V, A_f, c_f = G_f

    for (u,v) in chemin :
        c_f[(u,v)] -= flot_p[(u,v)]

        if c_f[(u,v)] == 0 :
            A_f[(u,v)] += chemin[(u,v)]

        c_f[(u,v )] = flot_p[(u,v)]
    return G_f



def cheminAugmentant(G_f, source, puits) :
    file = []

    heapq.heappush(file,source)
    parent = []
    parent[source] = source

    while file and file[0] == puits:
        V,A_f,_ = G_f
        heapq.heappop(file)
        for (u,v) in A_f :
            parent[v] = u
            heapq.heappush(file,v)

    chemin = parcoursChemin(parent, source, puits)
    return chemin


def parcoursChemin(parent, source, puits) :
    chemin = []
    v = puits
    while v != source :
        chemin.insert(0, chemin[v], v)
        v = parent[v]
    return chemin


# sommets adjacents
def voisin(G, u):
    return [v for (x,v) in G if u == x]


print(fordFulkerson(G, "A", "F"))







