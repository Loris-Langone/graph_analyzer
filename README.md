# Verificatore di Planarità dei Grafi

## Introduzione

Questo script Python analizza un grafo fornito in un file XGML per determinare se è planare o meno. Utilizza la libreria `networkx` per le operazioni sui grafi e un parser di grafi personalizzato per analizzare il file.

## Utilizzo

Per utilizzare questo script, segui questi passaggi:

1. Assicurati di avere Python installato sul tuo sistema.
2. Installa le librerie richieste eseguendo:
    ```
    pip install networkx colorama
    ```
3. Verifica che il file XGML contenente il grafo sia formattato correttamente.
4. Esegui lo script dalla riga di comando usando il seguente comando:
    ```bash
    python main.py "nomefile.xgml"
    ```

## Esecuzione dello Script

Lo script esegue i seguenti passaggi:

1. Analizza gli argomenti della riga di comando

2. Controlla se è stato fornito un numero corretto di argomenti dalla riga di comando. Se non è così, viene stampato un messaggio di errore che indica il modo corretto di utilizzare lo script.

3. Recupera il nome del file fornito come argomento dalla riga di comando.

4. Utilizza il parser del grafo per estrarre una matrice di adiacenza dal file XGML specificato.

5. Utilizza la libreria `networkx` per creare un grafo a partire dalla matrice di adiacenza.

6. Verifica se il grafo è planare utilizzando la funzione `check_planarity` di `networkx`.

7. Se il grafo è planare, calcola il numero di facce nel grafo e stampa un messaggio verde che indica che il grafo è planare e il numero di facce.

8. Se il grafo non è planare, stampa un messaggio rosso che indica che il grafo non è planare.

## Nota

- Assicurati che il file XGML sia formattato correttamente e contenga informazioni valide sul grafo.
- Il corretto funzionamento dello script dipende dalla corretta formattazione e struttura del file XGML di input.

Segui queste istruzioni per eseguire correttamente lo script e interpretare i suoi risultati. Fammi sapere se hai altre domande!
