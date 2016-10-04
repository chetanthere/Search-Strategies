#AI Programming Assignment 1 : Graph Search
#Chetan There : 1001248919

#from sets import Set
from operator import sub


graph = {}
path = []
pathcost = 0
fq = []
cq = []
cpathcost = 0
clength = 0
givenl = 0


def create_graph():
    #Graph implementaed as linked list {vertex:[(),()..],...}
    #read file contents
    linec = 0

    al = []
    with open('C:/Users/Chetan There/Desktop/assign1.txt') as inp_file:

        for line in inp_file:
            al = []
            #print(line)
            linec = linec + 1
            words = line.split(",")
            sn = words[0]
            en = words[1]
            pc = int(words[2])

            vt = (en,pc)

            #checking whether node is already there in graph dictionary
            if graph.has_key(sn):
                al = graph[sn]
                al.append(vt)
                graph[sn] = al
            else:
                al.append(vt)
                graph[sn] = al

            vt = (sn, pc)
            al = []

            # This is for en :checking whether node is already there in graph dictionary
            if graph.has_key(en):
                al = graph[en]
                al.append(vt)
                graph[en] = al
            else:
                al.append(vt)
                graph[en] = al

    print("total lines = ", linec)

def show_graph():
    print("Here is given Graph")
    for k,v in graph.items():
        show = str(k) +" : " +str(v)
        print(show )

def initialize():
    #print("Here is given initialize")
    global path,pathcost,fq,cq

    path = []
    pathcost = 0
    fq = []
    cq = []
    return

def testgoal():
    #print("Here is given testgoal")
    global cn,en
    #print(cn,en)
    if (cn == en):
        return 1
    else:
        return 0


def update_frontier(salgo):
    #print("Here is given update_frontier")
    global cn, en, sn
    global path, pathcost, fq, cq, cpathcost, clength, givenl

    if not cn in cq:
        for tuples in graph[cn]:
            if not tuples in fq:
                ts0 = tuples[0]
                ts1 = cn
                ts2 = tuples[1]

                if(salgo == "ucs"):
                    #cpathcost = cpathcost + ts2
                    ts2 = cpathcost + ts2

                tupless = (ts0,ts1,ts2)

                if (salgo == "dfsl"):
                    ts3 = clength + 1
                    tupless = (ts0, ts1, ts2, ts3)
                    if (ts3 <= givenl):
                        fq.append(tupless)
                else:
                    fq.append(tupless)

        cq.append(cn)

        fq = [x for x in fq if x[0] not in cq]
        if (salgo == "ucs"):
            fq.sort(key=lambda x: x[2])
    return


def choose_node(salgo):
    #print("Here is given choose_node")
    global cn, en, sn
    global path, pathcost, fq, cq, cpathcost,clength
    #print(salgo)

    if( (salgo == "bfs") or (salgo == "ucs") ):
        cnt = fq[0]
        if (salgo == "ucs"):
            cpathcost = cnt[2]
        cn = cnt[0]
        fq = fq[1:]
        path.append(cnt)
    elif( (salgo == "dfs") or (salgo == "dfsl") ):
        cnt = fq.pop()
        cn = cnt[0]
        if (salgo == "dfsl"):
            clength = cnt[3]
        path.append(cnt)
    else:
        print("ERROR: Improper search strategy")
        exit(1)

    return


def cal_path():
    #print("Here is given cal_path")
    global path, pathcost

    i = 0
    pathcost = 0
    rpath = []
    path.reverse()

    tup = path[0]
    rpath.append(tup[0])
    iparent= tup[1]
    pathcost = pathcost + tup[2]
    i = i + 1

    while(i < len(path)):
        tup = path[i]
        if(tup[0] == iparent):
            rpath.append(tup[0])
            iparent = tup[1]
            pathcost = pathcost + tup[2]
        i = i + 1

    rpath.reverse()
    path = rpath
    return


def bfs_search():
    #print("Here is bfs_search")
    global cn, en, sn
    global path, pathcost, fq, cq

    initialize()
    path.append((sn,sn,0))
    cn = sn
    result = 0

    while (True):

        tgr = testgoal()
        if(tgr == 1):
            result = 1
            res = path
            break

        update_frontier("bfs")

        if len(fq) == 0:
            res = "no path"
            result = 0
            break

        choose_node("bfs")

    cal_path()

    if result == 1:
        res.reverse()

    return(res)


def dfs_search():
    #print("Here is dfs_search")
    global cn, en, sn
    global path, pathcost, fq, cq

    initialize()
    path.append((sn, sn, 0))
    cn = sn
    result = 0

    while (True):

        tgr = testgoal()
        if (tgr == 1):
            result = 1
            res = path
            break

        update_frontier("dfs")

        if len(fq) == 0:
            res = "no path"
            result = 0
            break

        choose_node("dfs")

    cal_path()

    if result == 1:
        res.reverse()

    return (res)


def ucs_search():
    #print("Here is ucs_search")
    global cn, en, sn
    global path, pathcost, fq, cq,    cpathcost


    initialize()
    path.append((sn, sn, 0))
    cpathcost = 0
    cn = sn
    result = 0

    while (True):

        tgr = testgoal()
        if (tgr == 1):
            result = 1
            res = path
            break

        update_frontier("ucs")

        if len(fq) == 0:
            res = "no path"
            result = 0
            break

        choose_node("ucs")

    cal_path()
    pathcost = cpathcost

    if result == 1:
        res.reverse()

    return (res)



def dfsl_search():
    global cn, en, sn
    global path, pathcost, fq, cq, givenl, clength

    print("enter limit")
    givenl= int(raw_input())

    initialize()
    path.append((sn, sn, 0))
    clength = 0
    cn = sn
    result = 0

    while (True):

        tgr = testgoal()
        if (tgr == 1):
            result = 1
            res = path
            break

        update_frontier("dfsl")

        if len(fq) == 0:
            res = "no path"
            result = 0
            break

        choose_node("dfsl")

    cal_path()

    if result == 1:
        res.reverse()

    return (res)



if __name__ == '__main__':
    create_graph()
    show_graph()

    print("enter start node and end node to search")
    sn = raw_input()
    en = raw_input()
    cn = sn

    res = bfs_search()
    print("bfs results")
    print("traverse through :")
    print(res)
    print("path :")
    print(path)
    print("path cost :")
    print(pathcost)


    res = dfs_search()
    print("dfs results")
    print("traverse through :")
    print(res)
    print("path :")
    print(path)
    print("path cost :")
    print(pathcost)



    res = ucs_search()
    print("ucs results")
    print("traverse through :")
    print(res)
    print("path :")
    print(path)
    print("path cost :")
    print(pathcost)



    res = dfsl_search()
    print("dfsl results")
    print("traverse through :")
    print(res)
    if res != "no path":
        print("path :")
        print(path)
        print("path cost :")
        print(pathcost)


