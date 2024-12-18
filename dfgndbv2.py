import os
import pandas as pd
import streamlit as st

# Path to the CSV file
csv_file = "delta_force_game_log.csv"

# Check if the CSV file exists
if os.path.exists(csv_file):
    # If it exists, load the existing data
    existing_data = pd.read_csv(csv_file)
else:
    # If it doesn't exist, create an empty DataFrame with the correct columns
    existing_data = pd.DataFrame(columns=["Gun Used", "AI Kills", "Player Kills", "Delta Coins Earned", "Game Notes"])

# Sidebar to input new data
st.sidebar.title("Input New Game Log Entry")
gun_used = st.sidebar.text_input("Gun Used")
ai_kills = st.sidebar.number_input("AI Kills", min_value=0)
player_kills = st.sidebar.number_input("Player Kills", min_value=0)
delta_coin_earned = st.sidebar.number_input("Delta Coins Earned", min_value=0)
game_notes = st.sidebar.text_area("Game Notes")

# When the user submits the form
if st.sidebar.button("Add Game Log Entry"):
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

    # Provide a download button for the updated CSV
    csv = updated_data.to_csv(index=False)
    st.download_button(
        label="Download Updated Game Log",
        data=csv,
        file_name="delta_force_game_log.csv",
        mime="text/csv"
    )

    # Show the updated DataFrame
    st.subheader("Updated Game Log")
    st.dataframe(updated_data)
else:
    # Show the existing DataFrame if no new entry is added
    st.subheader("Existing Game Log")
    st.dataframe(existing_data)
