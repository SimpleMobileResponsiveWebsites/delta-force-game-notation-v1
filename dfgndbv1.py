import os

# Path to the CSV file
csv_file = "delta_force_game_log.csv"

# Check if the CSV file exists
if os.path.exists(csv_file):
    # If it exists, load the existing data
    existing_data = pd.read_csv(csv_file)
else:
    # If it doesn't exist, create an empty DataFrame with the correct columns
    existing_data = pd.DataFrame(columns=["Gun Used", "AI Kills", "Player Kills", "Delta Coins Earned", "Game Notes"])

# Store the new entry
new_data = {
    "Gun Used": [gun_used],
    "AI Kills": [ai_kills],
    "Player Kills": [player_kills],
    "Delta Coins Earned": [delta_coin_earned],
    "Game Notes": [game_notes]
}

# Convert new entry to DataFrame
new_entry = pd.DataFrame(new_data)

# Append the new entry to existing data
updated_data = pd.concat([existing_data, new_entry], ignore_index=True)

# Save the updated data back to the CSV file
updated_data.to_csv(csv_file, index=False)

# Provide download link
csv = updated_data.to_csv(index=False)
st.download_button(
    label="Download Updated Game Log",
    data=csv,
    file_name="delta_force_game_log.csv",
    mime="text/csv"
)
