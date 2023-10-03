# **Unsupervised Learning and Cryptocurrency Clustering**

## **Overview of Project**
In this project, a clustering problem is explored via dimensional reduction
using Principal Component Analysis (PCA), an unsupervised learning K-means model
used to fit the data, and hvplot and Plotly plots of the clustering results. The
context for the project is cryptocurrencies including their coin names,
algorithms, and even total coin supply and coins mined. The goal is to develop a
grouping system in order to better understand how an investment portfolio could
be constructed based on the groupings of the cryptocurrencies.

The main analysis file is *[crypto_clustering.ipynb](https://github.com/cdpeters/crypto-clustering-unsupervised-ML-sklearn/blob/main/crypto_clustering.ipynb)*
containing all of the preprocessing, PCA, K-means, and plotting.

### **Deliverable 1**
In this stage, the data is preprocessed using pandas. The preprocessing steps
consisted of:
* Setting a column as the index
* Filtering out coins that aren't currently being traded
* Dropping rows that have any null values in them
* Keeping only rows with coins mined greater than 0
* Creating a separate DataFrame to hold only the coin names
* Dropping columns that are no longer needed (after filtering)
* Creating a DataFrame with dummy values for categorical variables
* Scaling the data

### **Deliverable 2**
Deliverable 2 is only concerned with performing the PCA analysis and creating
the DataFrame with the three PCA components for each coin.

### **Deliverable 3**
Deliverable 3 brings the K-means implementation for this problem. First an elbow
curve is constructed to determine the best choice of number of clusters. The
curve shows that ***k = 4*** is the appropriate choice. Next, the actual K-means model
is fit to the data and the labels of the resulting clusters are extracted. A new
`clustered_df` DataFrame is constructed with the data, the PCA components and
resulting class labels.

### **Deliverable 4**
Lastly, plotting is performed to show the clustering by class. This section also
includes a sortable hvplot table and a scatter plot showing the coin numbers for
each cryptocurrency for each class.
