#Create two NumPy arrays: one representing the number of likes on your last 7 Instagram posts, and another for the number of comments.
#Use arithmetic operators to calculate the average engagement (likes + comments) per post and print the result.

import numpy as np

#Likes
likes = np.array([100,120,150,60,405,600,700])

#Comments
comments = np.array([50,30,15,64,60,75,35])

#Calculate Total
engagement = likes + comments
print("Engagement Total: ",engagement)

#Average engagement

average_engagement = engagement.mean()
print("Average Engagement: ",average_engagement)


