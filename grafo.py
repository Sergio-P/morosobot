import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import igraph as ig
from dbAPI import obtener_usuarios, obtener_deudas

## Grafo construido con libreria NetworkX
def construir_grafo():
	G = nx.DiGraph()

	usuarios = {}

	deudas = obtener_deudas()
	for deuda in deudas:
		if not deuda[0] in usuarios:
			G.add_node(deuda[0])
			usuarios[deuda[0]] = True
		if not deuda[1] in usuarios:
			G.add_node(deuda[1])
			usuarios[deuda[1]] = True
		G.add_edge(deuda[1], deuda[0], weight=deuda[2])

	plt.figure()
	pos = nx.circular_layout(G)
	edge_labels = nx.get_edge_attributes(G,'weight')
	nx.draw_networkx(G, pos, node_size=2400, node_color="#4598d4", font_size=10)
	nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
	plt.axis("off")
	plt.savefig("network.png")


## Draw a graph with igraph.
def buildGraph():
	## Create new directed graph.
	g = ig.Graph(directed=True)

	usuarios = {}

	deudas = obtener_deudas()
	for deuda in deudas:
		if not deuda[0] in usuarios:
			g.add_vertex(deuda[0], color = "#8BC34A")
			usuarios[deuda[0]] = True
		if not deuda[1] in usuarios:
			g.add_vertex(deuda[1], color = "#8BC34A")
			usuarios[deuda[1]] = True
		g.add_edge(deuda[1], deuda[0], weight=deuda[2])
		g.vs[g.vs.find(deuda[1]).index]['color'] = '#F44336'

	g.vs['label'] = g.vs['name']
	g.es['label'] = g.es['weight']
	visual_style = {}
	visual_style['vertex_size'] = 30
	visual_style['vertex_label_dist'] = 0
	visual_style['vertex_label_size'] = 10
	visual_style['edge_arrow_size'] = 1
	visual_style['edge_label_angle'] = 180
	visual_style['edge_label_dist'] = 0
	visual_style['edge_label_size'] = 8
	visual_style['layout'] = g.layout('circle')
	visual_style['autocurve'] = True
	visual_style['bbox'] = (300,300)
	visual_style['margin'] = 40

	#out = plot(g, 'network.png', **visual_style)
	#out.save('network.png')
	ig.plot(g, 'network.png', **visual_style)