import streamlit as st
import random

st.title("Rock Paper Scissors Game")

options = ["Rock", "Paper", "Scissors"]
user_choice = st.selectbox("Choose your option", options)

if st.button("Play"):
    computer_choice = random.choice(options)
    st.write(f"You chose: {user_choice}")
    st.write(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        st.write("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        st.write("You win!")
    else:
        st.write("You lose!")
