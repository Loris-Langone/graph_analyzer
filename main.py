import sys
import networkx as nx
from graph_parser import get_matrix
from colorama import Back


def get_argv():
    # Controlla se ci sono abbastanza argomenti
    if len(sys.argv) != 2:
        print("[ERROR] Script Usage: python main.py \"filename\"")
        return

    # Recupera gli argomenti
    filename = sys.argv[1]

    return filename


def check_planarity():
    filename = get_argv()
    adj_matrix = get_matrix(filename)

    graph = nx.from_numpy_array(adj_matrix)

    is_planar, _ = nx.check_planarity(graph)

    if is_planar:
        nodes = len(nx.nodes(graph))
        edges = len(nx.edges(graph))

        faces = edges - nodes + 2

        print(Back.GREEN + f"The graph is planar and it has {faces} faces")

    else:
        print(Back.RED + "The graph is not planar")


def main():
    check_planarity()


if __name__ == "__main__":
    main()
