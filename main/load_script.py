from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt
import json

model = SentenceTransformer("all-MiniLM-L6-v2")
file_path = './claims_data.json'


with open(file_path, 'r') as file:
    data = json.load(file)
    claim_numbers = [claim['ClaimNumber'] for claim in data]
    claim_descriptions = [claim['Description'] for claim in data]



sentence_embeddings = model.encode(claim_descriptions, convert_to_numpy=True)
pca = PCA(n_components=2) 
pca_embeddings = pca.fit_transform(sentence_embeddings)

def dbscan_plot_chart():
    print(pca_embeddings)

    dbscan = DBSCAN(eps=0.25, min_samples=3)  # Adjust these parameters based on your data
    clusters = dbscan.fit_predict(pca_embeddings)
    print(dbscan)
    print(clusters)


    unique_clusters = np.unique(clusters)
    largest_cluster = max(unique_clusters, key=list(clusters).count)
    print(unique_clusters)
    print(largest_cluster)

    # Colors for plotting
    colors = ['grey' if x == -1 else 'green' if x == largest_cluster else 'blue' for x in clusters]


    plt.figure(figsize=(12, 8))
    for i, color in enumerate(colors):
        x, y = pca_embeddings[i]
        plt.scatter(x, y, color=color)
        if clusters[i] == -1:
            plt.text(x + 0.01, y + 0.01, claim_numbers[i][:50] + '...', fontsize=9, color='red')  # Outliers in red text
        else:
            plt.text(x + 0.01, y + 0.01, claim_numbers[i][:50] + '...', fontsize=9, color='black')  # Others in black text

    plt.title('2D Visualization of Sentence Embeddings with Cluster Highlights')
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    plt.grid(True)
    plt.savefig('output_images/DBSsentence_embeddings_plot4.png') 

dbscan_plot_chart()
