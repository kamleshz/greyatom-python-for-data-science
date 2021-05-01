# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file

#Creating a new variable to store the value counts
loan_status =data.Loan_Status.value_counts()

#Plotting bar plot
loan_status.plot(kind='bar')
plt.xticks(rotation=360)
plt.title("Loan_status")
plt.legend()
plt.show()


# Step 2
#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar',stacked=False)
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
plt.show()



#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True)

#Changing the x-axis label
plt.xlabel("Education Status")
#Changing the y-axis label
plt.ylabel("Loan Status")
#Rotating the ticks of X-axis
plt.xticks(rotation=45)

# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education']=='Graduate']

#Subsetting the dataframe based on 'Education' column
not_graduate = data[data['Education']=='Not Graduate']

#Plotting density plot for 'Graduate'
graduate.plot(kind='density', label='Graduate',color='blue')

#Plotting density plot for 'Graduate'
not_graduate.plot(kind='density', label='Not Graduate',color='red')

#For automatic legend display
plt.legend()

# Step 5
#Setting up the subplots
fig,(ax_1,ax_2,ax_3)=plt.subplots(1,3, figsize=(12,8))

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'],marker='*',s=50)

#Setting the subplot axis title
plt.title("ApplicantIncome")

#Plotting scatter plot
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'],color='Orange',edgecolor='red',marker='>',s=50)

#Setting the subplot axis title
plt.title("Coapplicant Income")

#Creating a new column 'TotalIncome'
data['TotalIncome'] = data['ApplicantIncome']+data['CoapplicantIncome']

#Plotting scatter plot
ax_3.scatter(data['TotalIncome'],data['LoanAmount'],color='green',edgecolor='pink',s=50)


#Setting the subplot axis title
plt.title("Total Income")


