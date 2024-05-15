import pandas as pd
data_path = 'C:\\Users\\hongj\\git\\fc-manufactoring\\example_2.csv'
df = pd.read_csv(data_path)
fraud_data = df[df['isFraud'] == 1].sample(n=1000, random_state=42)
non_fraud_data = df[df['isFraud'] == 0].sample(n=1000, random_state=42)

result_path = 'C:\\Users\\hongj\\git\\fc-manufactoring\\sampled_data2.csv'
result_df = pd.concat([fraud_data, non_fraud_data])
result_df.to_csv(result_path, index=False)

