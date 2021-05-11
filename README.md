## Euclidean-distance
![Euclidean Distance Matrix](https://github.com/anij715/Mahalanobis-distance-analysis/blob/main/Euclid.PNG)
- From the above table, we can observe that, for the point D1, D2 is at the maximum distance (21.19) when both have different class values (D1.class == 4, D2.class == 2). While D5 is located the nearest, at 6.86 units from D1, both instances have the same class values (~4). Similarly, for other points, this trend is being followed by each pair. 
- Also, for distance of 12.45 units, class value is same, while for 13.71 units, class value is different, hence it has been noticed that the deciding value of distance between two instance points lies somewhere between 12.45 and 13.11.
- Therefore, we can say that, for distance less than 12.45, class values will be same, and for distance greater than 13.71, class values will be different. And, with the increase in Euclidean distance, probability of the class attributes being different also increases. 

- Except for the ‘Mitoses’ & ‘Uniformity of Cell Size’, we can differentiate the other attributes of these instances based on the Euclidean distance from the above table. Even though we have not included the class attribute while calculating the Euclidean distance, we have a relational dependence, means the other attributes also directly influences the class attribute, for e.g., nucleoli, if the value is large, there is a high chance that the class value will also be 4.
## Cosine-similarity
![Euclidean Distance Matrix](https://github.com/anij715/Mahalanobis-distance-analysis/blob/main/Cosine.PNG)
- Here, D2 & D3 have the lowest cosine similarity amongst all pairs, while D1 and D4 have the highest similarity. D2 & D3 have the same class values and D1 & D4 have the different class values. Also, while calculating the cosine similarity, we have not included the class attribute. So, from the above observations, I think we cannot determine different  instances with the help of cosine similarity.
## Mahalanobis-distance
![Euclidean Distance Matrix](https://github.com/anij715/Mahalanobis-distance-analysis/blob/main/MAHA.PNG)
- Here, D5 & D4 are the most apart based on the mahalanobis distance, and D1 & D2 are least separated amongst all pairs. Now consider D1, it has almost similar values of mahalanobis distance from D1, D3, and D4. And the only attribute which is same among these four instances is “Mitosis” with value 1. Now, for D2, the mahalanobis distance is similar from D1 & D3, but not from D4 and D5. Also, comparatively, D5 is placed far apart from each instance.

- So, it can be said that D1, D2, D3 & D4 all lie in the cartesian plane not too empty, but D5 on the other hand is very far from the cluster. From this, we cannot be certain about the class values of the D1, D2, D3, or D4, but we can say that D5 lies will have different behavior than the others.
## Conclusion
- From the above observations, I think that the Euclidean distance is the best suited for this dataset as we have seen that we can determine the class attribute of the instances based on the Euclidean distance between the two instance points. Also, we saw that some of the attribute values have weight when it comes to directly influence the class, which makes it easier to differentiate the instances with the help of Euclidean distance.

- On the other hand, while calculating cosine similarity, we did not have any certain relation through which we can differentiate the instances.

- And, after calculating the mahalabonis distance, we could tell apart D5, but not the other instances.
