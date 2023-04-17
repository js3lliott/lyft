# Predicting Lyft Driver Lifetime Value

The goal of this project is to predict the lifetime value (LTV) of a driver for Lyft and identify the main factors affecting a driver's LTV. We also aim to explore whether there are specific segments of drivers that generate more value for Lyft than the average driver and provide actionable recommendations for the business based on our findings.

## Project Approach

1. **Exploratory Data Analysis**: We'll perform in-depth EDA to understand the data better and identify any data quality issues
2. **Feature Engineering**: We will create features about rides and drivers included in the dataset that are relevant to our analysis.
3. **Projected LIfetime of a Driver**: We will estimate the average projected lifetime of a driver, which refers to the amount of time a driver typically continues driving with Lyft once they are onboarded.
4. **Clustering**: We will cluster drivers into categories using KMeans clustering to identify main factors affecting a driver's lifetime value.
5. **Actionable Recommendations**: We will provide actionable recommendations for the business based on our findings.

## Results & Recommendations

After exploring the data, we found that the average lifetime of a driver with Lyft is approximately **55 days**. We also performed KMeans clustering and identified four clusters of drivers based on their lifetime value, ride count, ride duration, and ride distance.

- `Cluster 0 = Bad drivers`: This cluster contains drivers with low lifetime value, low total ride count, low total ride duration and distance. They may have issues with customer service, low demand for their services, or low fares.
- `Cluster 2 = Fair drivers`: This cluster has drivers with a moderate lifetime value, ride count, ride duration, and ride distance. They may not have high demand for their services, but they also don't have many major issues impacting their ratings.
- `Cluster 1 = Good drivers`: The drivers in this cluster have higher lifetime values than the previous clusters, as well as higher ride count, duration, and distance. They most likely have consistent demand for their services and a good reputation, which could lead to higher earnings.
- `Cluster 3 = Excellent drivers`: This cluster has drivers with the highest lifetime value, ride count, distance, and duration. These drivers are likely the most in demand and have a great reputation for providing top-notch service, leading to high earnings.

Based on these findings, we recommend the following actionable steps for Lyft:

- Focus on retaining good and excellent drivers: The business should focus on retaining the drivers who belong to the good and excellent clusters as they bring in more revenue and have more frequent rides compared to other driving clusters.

- Target improvement of fair drivers: The business should target to improve the performance of fair drivers, to convert them into good or excellent drivers.

- Identify and address issues faced by bad drivers: The business should identify and address the issues faced by the bad drivers, such as low earnings, low frequency, and low ride duration, to improve their performance.

- Personalized incentives and training: The business can offer personalized incentives and training to drivers based on their performance clusters to further improve their performance.

- Use cluster results for dynamic pricing: The cluster results can be used for dynamic pricing, where prices can be adjusted based on the supply and demand of drivers in a particular area.

- Monitor performance regularly: The business should regularly monitor the performance of drivers and reassess them based on the clustering results to ensure that they are being properly targeted with the appropriate incentives and support.

By implementing these recommendations, Lyft can improve its driver retention, increase revenue, and enhance the overall experience for its passengers.

## Data Description

We have three CSV files to work with that contain the following data:

- `driver_ids.csv`: Unique identifier for a driver and the date on which they were onboarded.
- `ride_ids.csv`: Unique identifier for a driver and ride, ride distance in meters, ride duration in seconds, and prime time applied on the ride.
- `ride_timestamps.csv`: Unique identifier for a driver and ride, ride distance in meters, ride duration in seconds, and prime time applied on the ride.