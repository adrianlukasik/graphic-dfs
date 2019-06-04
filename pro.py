from helper import *
	
# Wykonuje algorytm dfs na grafie G, wierzchołku startowym v i słowniku
# cities, w którym znajdują się nazwy miast.	
def dfs(txt, G, cities, v, pos):
	
	# Funkcja pomocnicza funkcji dfs, wykorzystuje rekurencję.
	# Posiada parametry graf G, aktualny wierzchołek v, poprzedni
	# wierzchołek pre, tablica visited przechowująca informację
	# o odwiedzonych wierzchołkach.
	def dfsNode(G, v, pre, visited):
		visited[v] = True
		
		if (pre != v):
			markTrailBetweenCitiesAndPrintReport(txt, G, v, pre, cities.get(v), pos)
		else:
			markStartingPoint(G, v)
			
		for u in G.neighbors(v):
			if visited[u] == False:
				dfsNode(G, u, v, visited)
				showReturnToCity(txt, G, v, cities.get(v))
			else:
				executeInstructionsRelatedToVisitedCity(txt, G, v, pre, u, cities.get(u), pos)
			
		showVerifyNeighbours(txt, G, v, cities.get(v))
	
	visited = [False] * (len(cities))
	beginNote(txt, cities.get(v))
	dfsNode(G, v, v, visited)
	endNote(txt)
	
plt.ion()

H=nx.DiGraph()

H.add_edges_from([(0,1), (1,0), (0,2), (2,0), (1,2), (2,1), (2,3), (3,2),
(2,4), (4,2), (3,4), (4,3), (3,5), (5,3), (4,5), (5,4), (4,6), (6,4),
(4,7), (7,4), (5,6), (6,5), (5,8), (8,5), (6,7), (7,6), (6,8), (8,6),
(6,9), (9,6), (6,10), (10,6), (7,9), (9,7), (9,10), (10,9), (10,11), (11,10)])

cities = {0:"Lisboa", 1:"Cadiz", 2:"Madrid", 3:"Barcelona", 4:"Pamplona",
5:"Marseille", 6:"Paris", 7:"Brest", 8:"Zurich", 9:"Dieppe",
10:"Bruxelles", 11:"Amsterdam"}

fig = plt.figure(1,figsize=(16,8))
ax = fig.add_axes((0,0,1,1))

pos = nx.drawing.layout.planar_layout(H)

txt=fig.text(.55,.9,'Ahoj przygodo!',fontsize=15)

for n in H:
    H.node[n]['draw'] = nx.draw_networkx_nodes(H,pos,nodelist=[n], node_size=200,alpha=0.5,node_color='k')
for u,v in H.edges():
    H[u][v]['draw']=nx.draw_networkx_edges(H,pos,edgelist=[(u,v)],alpha=1,arrows=False,width=3, edge_color = 'k')
    
posL={}
for n,p in pos.items():
	posL[n] = (p[0],p[1]+0.03)
	
labdraw = nx.draw_networkx_labels(H,posL,cities)
wait(2)
plt.show()
wait(1)
dfs(txt, H, cities, 0, pos)
	
