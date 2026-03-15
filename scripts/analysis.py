import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data/marketing_campaign.csv")

# Display first rows
print(data.head())

# Calculate Click Through Rate
data["CTR"] = data["clicks"] / data["impressions"]

# Calculate Conversion Rate
data["Conversion Rate"] = data["conversions"] / data["clicks"]

# Calculate ROI
data["ROI"] = (data["conversions"] * 50 - data["cost"]) / data["cost"]

print("\nCampaign Metrics:")
print(data[["channel","CTR","Conversion Rate","ROI"]])

# Visualization
plt.figure(figsize=(8,5))
sns.barplot(x="channel", y="conversions", data=data)

plt.title("Conversions by Marketing Channel")
plt.show()