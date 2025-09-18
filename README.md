# PCA & Clustering di rane con KMeans

Questo progetto esplora un dataset di **rane** e applica tecniche di **clustering non supervisionato** tramite **KMeans**.  
L'obiettivo è confrontare i cluster generati dall'algoritmo con le classi reali delle rane.

---

## 📊 Dataset

- Ogni **rana** è descritta da **22 feature** quantitative.  
- Ci sono **4 classi di rane** conosciute nel dataset (Family).  
- Le feature sono state normalizzate/standardizzate prima del clustering.
- [https://archive.ics.uci.edu/dataset/406/anuran+calls+mfccs](Il dataset usato).

---

## 🎯 Obiettivo

- Applicare **KMeans** per raggruppare le rane in cluster.  
- Confrontare i cluster ottenuti con le classi reali delle rane.  
- Visualizzare i dati in **3D** usando **PCA** per ridurre le 22 feature principali a 3 componenti principali.

---

## ⚙️ Pipeline utilizzata

1. **Custom KMeans**: implementazione personalizzata per ottimizzazione dei centroidi.  
2. **PCA a 3 dimensioni**: riduzione della dimensionalità da 22 a 3 componenti principali.  
3. **Generazione grafici**: interattivi in 3D con Plotly e Streamlit.

---

## 🔍 Analisi dei cluster

- È stato usato **l’Elbow Method** per identificare il numero ottimale di cluster.  
- Il miglior risultato è stato ottenuto con **5 cluster**, nonostante ci siano 4 classi:  
  - Nel grafico 3D si vede che una porzione della popolazione di leptociatidi forma un cluster a sé.  
  - Con **6 cluster**, un cluster evidente viene diviso in due, rendendo il risultato meno interpretabile.  
- La quarta classe **Bufonidae** non crea un cluster proprio, a causa della **disparità nella dimensione della popolazione** e della **similarità con altre classi**.

---

## 🖥️ Contenuto della repository

- `app.py` → App Streamlit interattiva con toggle tra colorazione per Family o per Cluster.  
- `pca_results_5cl.pkl` → Risultati PCA + KMeans per **5 cluster**.  
- `pca_results_4cl.pkl` → Risultati PCA + KMeans per **4 cluster**.  
- `requirements.txt` → Librerie necessarie per eseguire l’app.

---

## 🌐 Visualizzazione online

I grafici sono disponibili direttamente online senza download:  
[https://kmeans-pca-visualization.streamlit.app/](https://kmeans-pca-visualization.streamlit.app/)  

È possibile osservare come cambia il clustering con **4, 5 o 6 cluster**.

