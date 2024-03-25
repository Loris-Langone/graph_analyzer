import sys

def main():
    # Controlla se ci sono abbastanza argomenti
    if len(sys.argv) != 2:
        print("[ERROR] Script Usage: python nome_script.py nome_file")
        return

    # Recupera gli argomenti
    nome_file = sys.argv[1]

    # Fai qualcosa con gli argomenti
    print("Nome file:", nome_file)

if __name__ == "__main__":
    main()
