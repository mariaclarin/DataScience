# Data Science Assigment Week 8
Maria Clarin - 2501990331 - L3AC
## Directory
* exercise1.csv : csv file for the data presented in exercise 1
* exercise1.csv : the code implementing kmeans algorithm for exercise 1
* HorrorSVMCookies.csv : the dataset file of my group's fp
* kmeans.ipynb : the code implementing kmeans algorithm for my group's dataset
* hierarchical.ipynb : the code implementing hierarchical algorithm for my group's dataset
* meanshift.ipynb : the code implementing meanshift algorithm for my group's dataset

## Conclusion
For this assignment, I have completed **Exercise 1** with Kmeans Clustering Algorithm </br>
Aside from that, I have also tried out several clustering algorithms using my group's dataset. </br>
1. **K-Means Algorithm** </br>
* I divided the data into 3 clusters and used kmeans algorithm to track the centroids of the clusters. 
2. **Hierarchical Algorithm** </br>
* I used hieararchical algorithm to cluster the data using a dendogram and present it. The number of clusters solely depends on where you determine to cut the dendogram based on the y axis value. Therefore it is very flexible
3. **Meanshift Algorithm** </br>
* The algorithm iteratively assigns each data point towards the closest cluster centroid and direction to the closest cluster centroid is determined by where most of the points nearby are at. It outputs 16 estimated clusters. </br>
</br>
Note : There might be some outliers present in our dataset, possibly presented in plots of each algorithm, however the amount is very little compared to the total amount of data that we have. (1248 rows)

## Datasets Resource:
* https://www.goodreads.com/shelf/show/horror

