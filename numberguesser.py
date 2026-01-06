import streamlit as st
import random

if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.message = ""

with st.form("guess_form"):
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100)
    submitted = st.form_submit_button("Submit Guess")

if submitted:
    st.session_state.attempts += 1
    if guess < st.session_state.secret_number:
        st.session_state.message = "Too low! Try again."
    elif guess > st.session_state.secret_number:
        st.session_state.message = "Too high! Try again."
    else:
        st.session_state.message = f"Congratulations! You guessed it in {st.session_state.attempts} tries!"
        st.session_state.secret_number = None # End game


st.write(st.session_state.message)
