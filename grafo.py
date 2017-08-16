import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
from dbAPI import obtener_usuarios, obtener_deudas


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
