## Week 10 Assignment - Recommendation System
Maria Clarin - 2501990331 - L3AC

## Description
I have successfully made a recommendation system using netflix movies dataset from Kaggle. </br>
Source: https://www.kaggle.com/datasets/rishitjavia/netflix-movie-rating-dataset?resource=download</br>
Directory : </br>
* netflixRecommenderSystem.ipynb : the code file for the recommendation system 
* Netflix_Dataset_Movie.csv : the movie dataset from kaggle
* Netflix_Dataset_Rating.csv : the rating dataset from kaggle (I cannot upload this file nor can I push it due to the size boundary of the file limited by GitHub, but it is the same dataset from the Kaggle link)

## Important Notes !
Do note that I have tried and explored other datasets to create a recommendation system in the folder "Experiment". </br>
</br>
Inside the folder, I tried using my own group's dataset, however, because our group didnt have a proper user rating dataset yet, so I made up some fake dataset just to play around to 
understand the concept of the recommendation system better. Because of the incomplete dataset for the user rating (because its not real data), the recommendation system works, however for the calculations, there are a lot of NaN values or very round values such as 1.0 and 0.0 that you can see in the output. After understanding it better, I found that it is because there is not enough unique raters for the calculation to be maximized and be accurate. But the system still worked ! >_<
</br>
</br>
Also inside the folder, there is another folder named "Exploring" where I tried using another, more complex dataset from BX books archive. </br>
Source : http://www.informatik.uni-freiburg.de/~cziegler/BX/</br>
However, the full system still has some errors due to some mathematical calculation that went wrong with the values of the data in the dataset. I still am unable to figure out the specific root cause of it, however, I do know that the problem is within the dataset and how the data is presented. Therefore, this project/file, I'm still exploring.
