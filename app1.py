import streamlit as st

# Title of the app
st.title("Delta Force Operations - Game Log")

# Create a form to input game data
with st.form("game_data"):
    st.subheader("Game Session Information")
    
    # Player's information input fields
    gun_used = st.text_input("Gun Used", help="Enter the name of the gun used during the session.")
    ai_kills = st.number_input("AI Kills", min_value=0, step=1, help="Enter the number of AI kills.")
    player_kills = st.number_input("Player Kills", min_value=0, step=1, help="Enter the number of player kills.")
    delta_coin_earned = st.number_input("Delta Coins Earned", min_value=0, step=1, help="Enter the amount of Delta Coin earned.")
    
    # Game session notes
    game_notes = st.text_area("Game Notes", help="Any notes you want to add about the game session.")
    
    # Submit button to save data
    submit_button = st.form_submit_button(label="Save Game Session")

# Handling the form submission
if submit_button:
    st.write("### Game Session Summary:")
    st.write(f"**Gun Used:** {gun_used}")
    st.write(f"**AI Kills:** {ai_kills}")
    st.write(f"**Player Kills:** {player_kills}")
    st.write(f"**Delta Coins Earned:** {delta_coin_earned}")
    st.write(f"**Game Notes:** {game_notes}")

    # Optionally, you can save this data to a file, a database, or display a success message.
    st.success("Game session logged successfully!")

# Optionally, you can add a button to download a CSV or JSON file of the logs
import pandas as pd

# Store all entries in a list for exporting
if submit_button:
    data = {
        "Gun Used": [gun_used],
        "AI Kills": [ai_kills],
        "Player Kills": [player_kills],
        "Delta Coins Earned": [delta_coin_earned],
        "Game Notes": [game_notes]
    }
    
    # Save the data to a CSV file
    df = pd.DataFrame(data)
    csv = df.to_csv(index=False)

    st.download_button(
        label="Download Game Log",
        data=csv,
        file_name="delta_force_game_log.csv",
        mime="text/csv"
    )
