# ldssa-capstone

This is the github repository that contains my solution of the Batch 3 Lisbon Data Science Academy Capstone Project.

Every detail of the project is explained here: https://docs.google.com/document/d/1EVEqCiUGSyXgb2d9k4zQHAMIeWnhQx5YGYKI0yWkjtQ/edit#

# Quick overview

The dataset contains roughly 3 years of data from vehicles that were stopped by the Connecticut police and whether they were searched afterwards, in an attempt to find drugs. A variety of data about the drivers was also recorded.

The main goal of the project was to create a machine learning model that not only predicts the cars that are most likely to have drugs but also ensure fairness across the population of drivers (namely in 3 of the features: their sex, ethnicity and race). E.g. women should not be unfairly more searched than men. To ensure fairness, the difference of precision between the classes of these 3 features was kept under 10%.

The first report was made before the model went into production. In there I explained my decisions and the steps that I took in order to build the machine learning model.
After the first report, the model was deployed in production, on a Heroku server, using a Flask app with 2 endpoints (one to receive the datapoints and one to update information about the received datapoints). The production run lasted a week and the production dataset had 10k datapoints. For 5k of those datapoints, we received their labels (if the car had drugs inside or not).
Finally, the second report compares the expected behavior described in the first report with the reality obtained in the production run (using the 5k labels to assess the performance of the model).

Inside each folder there's a short description of every file. 



