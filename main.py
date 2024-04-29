import sys
import networkx as nx
from graph_parser import get_matrix
from colorama import Back
import tkinter as tk


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

        text = tk.Label(
            root, text=f"The graph is planar and it has {faces} faces", bg="GREEN", font=("TkDefaultFont", 60))
        text.pack()

    else:
        text = tk.Label(
            root, text=f"The graph is not planar", bg="RED", font=("TkDefaultFont", 60))
        text.pack()


def main():
    global root
    root = tk.Tk()
    root.title("Formula di Eulero")
    root.update_idletasks()
    root.geometry(
        f"{root.winfo_screenwidth()}x180+1+{int(root.winfo_screenheight()*0.70)}")

    check_planarity()

    root.mainloop()


if __name__ == "__main__":
    main()
