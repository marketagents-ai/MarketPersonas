### Clustering on question embeddings

This notebook demonstrates how to cluster embeddings from a sentence transformer using five different clustering methods. Each method has specific strengths and use cases:

1. **K-Means**  
   - **Why try it?**  
     - K-Means is one of the most widely used clustering algorithms due to its simplicity and speed on large datasets.  
     - It works well when your data is roughly spherical (in terms of Euclidean distance) and you have a rough idea of how many clusters you want.  
     - If you need quick, scalable clustering that’s easy to interpret, start with K-Means.

2. **Hierarchical (Agglomerative) Clustering**  
   - **Why try it?**  
     - Hierarchical clustering builds a hierarchy of clusters in a tree-like structure (a dendrogram), allowing you to see how clusters merge at different distance thresholds.  
     - If you want a flexible, interpretable method that can reveal potential sub-cluster relationships, hierarchical clustering is a great choice.

3. **DBSCAN**  
   - **Why try it?**  
     - DBSCAN (Density-Based Spatial Clustering of Applications with Noise) automatically detects clusters based on density, without requiring you to pre-specify the number of clusters.  
     - Choose DBSCAN if you suspect your data contains clusters of varying shapes/sizes or want a method that can handle noise gracefully.

4. **HDBSCAN**  
   - **Why try it?**  
     - HDBSCAN (Hierarchical DBSCAN) is an improvement over DBSCAN that can handle variable-density clusters.  
     - It starts with a hierarchical approach (like agglomerative) but merges it with DBSCAN’s density-based approach.  
     - If you want fully automated cluster discovery that can deal with complex data structures and produce better, more stable results than plain DBSCAN, HDBSCAN is often the go-to.

5. **UMAP + HDBSCAN** (Dimensionality Reduction + Clustering)  
   - **Why try it?**  
     - UMAP (Uniform Manifold Approximation and Projection) is a non-linear dimensionality reduction technique that can help reveal structure in high-dimensional data, often better than PCA or t-SNE.  
     - By reducing the dimensionality of embeddings (especially if they are large, e.g., 768 or 1024 dimensions), clustering methods like HDBSCAN can more easily discover clusters in the 2D–5D space.  
     - If your embeddings are high-dimensional and you suspect that simpler clustering in the original space might miss nuanced structure, UMAP + HDBSCAN can lead to clearer groupings and better visualizations.

---

### Usage Notes

- **Install Dependencies**:  
  \[
    \text{pip install numpy scikit-learn umap-learn hdbscan}
  \]

- **Load Embeddings**:  
  - Update the `folder_path` in the notebook to point to your `.npy` files.

- **Run Clustering**:  
  - Execute each cell in order to see how each method performs on your data.

- **Compare Results**:  
  - Check the **silhouette scores** (or other metrics) and explore cluster distributions.  
  - You can tune hyperparameters (e.g., `n_clusters` in K-Means, `eps` in DBSCAN, `min_cluster_size` in HDBSCAN) to find the best fit for your data.

