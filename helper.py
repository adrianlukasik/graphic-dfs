import networkx as nx
import matplotlib.pyplot as plt

# Wypisuje informację dotyczącą miasta city.
def writeInformation(txt, beginInfo, endInfo, city):
	txt.set_text(f'{beginInfo} {city} {endInfo}')
	
# Zmienia kolor wierzchołkowi v grafu G na color.	
def changeColorNode(G, v, color):
	G.node[v]['draw'].set_color(f'{color}')
	
# Zmienia kolor krawędzi u,v grafu G na color.
def changeColorEdge(G, u, v, color, pos):
	G[u][v]['draw'] = nx.draw_networkx_edges(G,pos,edgelist=[(u,v)],
	alpha=1,arrows=False,width=3, edge_color=f'{color}')

# Czeka	liczbę sekund równą number.
def wait(number):
	plt.pause(number)

# Notka końcowa. 	
def endNote(txt):
	for i in range(5,0,-1):
		writeInformation(txt, f'Nasza podróż dobiegnie końca za {i}', '', '')
		wait(1)

# Zmienia kolor krawędzi prev-v oraz kolor wierzchołka v na zmienną color.
# Wypisuje informację info o mieście city.
def changeColorAndPrintInformation(txt, G, v, pre, color, info, city, pos):
	changeColorEdge(G, pre, v, color, pos)
	wait(1)
	changeColorNode(G, v, color)
	writeInformation(txt, info, '', city)

# Wypisuje informację info o powrocie do danego miasta city lub o sprawdzeniu
# wszystkich sąsiadów miasta city. Zmienia color wierzchołkowi v na color1,
# a następnie przywraca color2 po wypisaniu informacji.
def printBackInformationAndSwitchColorNode(txt, G, v, color1, color2, info, city):
	changeColorNode(G, v, color1)
	writeInformation(txt, info, '', city)
	wait(2)
	changeColorNode(G, v, color2)
