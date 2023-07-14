# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 08:44:57 2023

@author: User
"""
def load_me():
    import multiprocessing
    import psutil
    import time
    
    def cpu_load():
        while True:
            pass
    
    def load_cpu(target_percent):
        num_cpus = psutil.cpu_count(logical=False)
        procs = []
    
        for _ in range(num_cpus):
            p = multiprocessing.Process(target=cpu_load)
            p.start()
            procs.append(p)
    
        while True:
            time_load = 300
            cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    
            if all(cpu >= target_percent for cpu in cpu_percent):
                rain(emoji = "🤒",font_size = 64,falling_speed = 2, 
                        animation_length = 1)
                
                with st.empty():

                    for i in range(0,time_load):
                        time.sleep(1)
                        st.subheader(f"CPU LOADED!! :{i+1}/{time_load}")
                        # print(f"CPU: {cpu_percent}- {i}/{time_load}")
                    break
                
        rain(emoji = "🤖",font_size = 64,falling_speed = 3, 
                animation_length = 1)
        
        with st.empty():        
            st.subheader("CPU RELAXING")
        for p in procs:
            p.terminate()
    
    target = 50
    # print(psutil.cpu_percent(interval=1, percpu=True))
    load_cpu(target)
    
def load_me_test():
    import multiprocessing
    import psutil
    import time


    while True:
        print("reached Target")            
        time_load = 10
        print("Wait for {time_load}secs")
        rain(emoji = "🤒",font_size = 64,falling_speed = 2, 
                animation_length = 1)
        with st.empty():        
            for i in range(0,time_load):
                time.sleep(1)
                print(f"CPU:{i+1}/{time_load}")
                st.subheader(f"CPU LOADED!! :{i+1}/{time_load}")
    
            break
    rain(emoji = "🤖",font_size = 64,falling_speed = 3, 
            animation_length = 1)
    with st.empty():        
        st.subheader("CPU RELAXING")
      
import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_extras.let_it_rain import rain


df_db = pd.read_csv('Reviews.csv')
view_flag = False
# Initialize user_ratings if it doesn't exist in session_state
# if "user_ratings" not in st.session_state:
st.session_state.user_ratings = []

# Ask for user's name
name = st.text_input("Enter your name:")

# Read in CSV with motivational messages
messages_df = pd.read_csv("motivational_messages.csv")

# Print message with name + motivational message
if st.button("Motivate Me"):
    # Randomly select a message from the DataFrame
    selected_motiv = messages_df.sample().iloc[0]["Motivation"]
    
    # Print the message with the user's name
    st.write(f"Hi {name}! Here's a motivational message for you:")
    st.write(selected_motiv)
    rain(emoji = "💝",font_size = 64,falling_speed = 5, 
            animation_length = 1)
    

# Print message with name + motivational message
if st.button("Roast Me"):
    # Randomly select a message from the DataFrame
    selected_roast = messages_df.sample().iloc[0]["Demotivation"]
    
    # Print the message with the user's name
    st.write(f"Hi {name}! Brace Yourself for a Roast:")
    st.write(f"{selected_roast}")
    rain(emoji = "😈",font_size = 64,falling_speed = 3, 
            animation_length = 1)
    

# Ask the user to rate their experience
rating = st.radio("Rate your experience", options=[1, 2, 3, 4, 5])
if st.button("Rate Your Experience"):

    
    user_rating = {"User": name, "Rating": rating}
    st.session_state.user_ratings.append(user_rating)

    # Display the thank you message
    st.write(f"Thank you, {name}! You rated your experience as {user_rating['Rating']} out of 5.")
    st.snow()

# Display the logged user ratings

    try:
        df = pd.DataFrame(st.session_state.user_ratings)
        df.columns = ["SUPPORTERS","RATING"]
        df_view = pd.concat([df,df_db],axis=0)
        df_view.reset_index(inplace=True,drop=True)
        if len(df_view) > 5:               
            df_view = df_view.iloc[:5]
        df_view.to_csv('Reviews.csv',index=False)
        view_flag = True
    
    except:
        st.subheader("Rate Me ?")

st.subheader("Recent 5 User Ratings")
if view_flag==True:    
    st.write(df_view)
else:
    st.write(df_db)

if st.button("LOAD MEE"):
    ### CPU LOADINGSS
    # load_me_test()
    load_me()
