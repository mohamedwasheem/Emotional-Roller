# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 08:44:57 2023

@author: User
"""

import streamlit as st
import pandas as pd

# Initialize user_ratings if it doesn't exist in session_state
if "user_ratings" not in st.session_state:
    st.session_state.user_ratings = []

# Ask for user's name
# name = st.text_input("Enter your name:")
name = "Afrah"

# Read in CSV with motivational messages
messages_df = pd.read_csv("motivational_messages.csv")

# Print message with name + motivational message
if st.button("Islamically Motivate Me"):
    # Randomly select a message from the DataFrame
    selected_motiv = messages_df.sample().iloc[0]["Motivation"]
    
    # Print the message with the user's name
    # st.write(f"Hi {name}! Here's a motivational message for you:")
    # st.write(selected_motiv)
    st.write(f"Dearest {name},")
    st.write(f"{selected_motiv}")

# Print message with name + motivational message
if st.button("Motivate Me"):
# if st.button("Roast Me"):
    # Randomly select a message from the DataFrame
    selected_roast = messages_df.sample().iloc[0]["Demotivation"]
    
    # Print the message with the user's name
    # st.write(f"Hi {name}! Brace Yourself for a Roast:")
    st.write(f"Dearest {name},")
    st.write(f"{selected_roast}")

# Ask the user to rate their experience
# rating = st.radio("Rate your experience", options=[1, 2, 3, 4, 5])
# if st.button("Rate Your Experience"):

    
#     user_rating = {"User": name, "Rating": rating}
#     st.session_state.user_ratings.append(user_rating)

#     # Display the thank you message
#     st.write(f"Thank you, {name}! You rated your experience as {user_rating['Rating']} out of 5.")

# # Display the logged user ratings
# st.subheader("Realtime Supporters Ratings")
# try:
#     df = pd.DataFrame(st.session_state.user_ratings)
#     df.columns = ["SUPPORTERS","RATING"]
#     st.write(df)
# except:
#     st.subheader("YOU ARE THE FIRST SCAPE GOAT")
    
