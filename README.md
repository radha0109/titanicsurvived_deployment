# titanicsurvived_deployment
# Analysis of Titanic Disaster Dataset by Applying EDA and Machine Learning Techniques.

# 1.	INTRODUCTION

The most infamous disaster which occurred over a century ago on April 15, 1912, that is well known as sinking of “The Titanic”. The collision with the iceberg ripped off many parts of the Titanic. Machine Learning algorithms are applied to make a prediction which passengers survived at the time of sinking of the Titanic. Features like ticket, fare, age, sex, class will be used to make the predictions. The objective is to perform EDA to mine various information in the dataset available and to know the effect of each field on survival of passengers by applying analytics between every field of dataset with “Survival” field.

# 2.	TOOLS & LIBRARIES

Python,  Jupyter Notebook, Pandas, Numpy, Seaborn, Sklearn, Matplotlib, Plotly & Cufflinks.

# 3.	DATA DESCRIPTION

The datasets contains following columns.

•	Passenger ID: Passenger ID numbers.

•	Survival: Outcome of Survival (0 = No; 1 = Yes)

•	Class: Passengers Class (1 = 1st; 2 = 2nd; 3 = 3rd)

•	Name: Name of the passengers.

•	Sex: Sex of the passengers.

•	Age: Age of the passengers.

•	SibSp: Number of Siblings/ Spouses Aboard

•	Parch: Number of Parents/ Children Aboard

•	Ticket: Ticket Number of the passengers.

•	Fare: Passenger Fare (British Pound).

•	Cabin: Does the location of the cabin influence chances of survival?

•	Embarked: Embarked implies where the traveler mounted from.
Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

# 4.	DATA CLEANING

Before applying any type of data analytics on the dataset, the data is first clean. There are some missing values in the dataset which needs to be handled. 

•	Analysis of the Cabin.

•	Deleting “Cabin” column as it has lots of missing values.

•	Analysis of missing person

•	Replacing the missing values “Embarked” column with the highest accuracy frequency. 

# 5.	EXPLORATORY DATA ANALYSIS (EDA)

We are going to perform Exploratory Data Analysis for our problem in the first stage. In Exploratory Data Analysis dataset is explored to figure out the features which would influence the survival rate. The data is deeply analyzed by finding a relationship between each attribute and survival.

•	Total Survived Passengers by Pclass.

•	Passenger’s composition by Sex.

•	Survival percentage of minors.

•	Passengers who travelled with at least one Siblings/Spouse.

•	Passengers who travelled with at least one Parents/Children.


# 6.	MACHINE LEARNING ALGORITHM

•	Logistic Regression(Lasso)

•	Logistic Regression(Ridge)

•	Gradients Boosting Classifier

•	Random Forest Classifier

I deployed this project on HEROKU.
Link: (https://dashboard.heroku.com/apps/titanic-survivedpred02)
