import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file to check the initial few rows and structure
data_path = 'C:\\Users\\hongj\\git\\fc-manufactoring\\example_1.csv'
data = pd.read_csv(data_path, delimiter=';')

# Display the first few rows of the dataframe
print(data.head())

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Data categorization
normal_data = data[data['anomaly'] == 0]
anomaly_data = data[data['anomaly'] == 1]

# Define the features to plot
features = ['Accelerometer1RMS', 'Accelerometer2RMS', 'Current', 'Pressure', 'Temperature', 'Thermocouple', 'Voltage', 'Volume Flow RateRMS']

# Creating histograms for each feature
fig, axes = plt.subplots(nrows=len(features), ncols=2, figsize=(15, 30), constrained_layout=True)
fig.suptitle('Comparison of Normal and Anomaly Data Distributions', fontsize=16)

for i, feature in enumerate(features):
    # Histograms
    sns.histplot(normal_data[feature], bins=30, kde=False, ax=axes[i][0], color='blue', label='Normal')
    sns.histplot(anomaly_data[feature], bins=30, kde=False, ax=axes[i][1], color='red', label='Anomaly')
    
    axes[i][0].set_title(f'Normal: {feature}')
    axes[i][1].set_title(f'Anomaly: {feature}')
    axes[i][0].legend()
    axes[i][1].legend()

plt.show()

# Creating box plots for each feature
fig, axes = plt.subplots(nrows=len(features), ncols=1, figsize=(10, 20), constrained_layout=True)
fig.suptitle('Box Plot of Features by Data Type', fontsize=16)

for i, feature in enumerate(features):
    sns.boxplot(x='anomaly', y=feature, data=data, ax=axes[i], palette='Set3')
    axes[i].set_title(f'Box Plot of {feature}')
    axes[i].set_xticklabels(['Normal', 'Anomaly'])

plt.show()




