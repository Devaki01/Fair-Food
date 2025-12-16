final_df["Order_Date"] = pd.to_datetime(
    final_df["Order_Date"], format="%d-%m-%Y"
)
final_df["Time_taken_min"] = (
    final_df["Time_taken(min)"]
    .astype(str)
    .str.extract(r"(\d+)")
    .astype(float)
)
# plot_df = final_df.dropna(
#     subset=["Order_Date", "Festival", "Time_taken_min"]
# )
plot_df = final_df[final_df["Festival"].isin(["Yes ", "No "])].copy()

daily_time = (
    plot_df
    .groupby(["Order_Date", "Festival"])["Time_taken_min"]
    .mean()
    .reset_index()
)

daily_pivot = daily_time.pivot(
    index="Order_Date",
    columns="Festival",
    values="Time_taken_min"
)
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

for col in daily_pivot.columns:
    plt.plot(
        daily_pivot.index,
        daily_pivot[col],
        label=f"Festival = {col}",
        linewidth=2
    )

plt.xlabel("Date")
plt.ylabel("Average Delivery Time (minutes)")
plt.title("Daily Average Delivery Time: Festival vs Non-Festival")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
