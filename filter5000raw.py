import pandas as pd
data_path = 'C:\\Users\\hongj\\git\\fc-manufactoring\\example_3.csv'
df = pd.read_csv(data_path)

total_count = len(df)
print("Total number of data points:", total_count)

#sampling_df = df.sample(n=5000, random_state=42)

#result_path = 'C:\\Users\\hongj\\git\\fc-manufactoring\\sampled_data3.csv'
#sampling_df.to_csv(result_path, index=False)

