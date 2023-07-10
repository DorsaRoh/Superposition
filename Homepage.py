import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Superposition of Transverse Waves",
    page_icon="waves",
)

st.title("Superposition of Tranverse Waves")
st.subheader(" ━━━━━━━━━━━━━━━━━━━━━━")


t = np.linspace(0, 2*np.pi, 1000)  # Time array from 0 to 2π


st.subheader("Wave 1")
amplitude1 = st.number_input("Enter the amplitude of the 1st wave: ", value=0.55)
frequency1 = st.number_input("Enter the frequency of the 1st wave: ", value=0.51)
phase1 = st.number_input("Enter the phase shift of the 1st wave: ")

st.subheader("Wave 2")
amplitude2 = st.number_input("Enter the amplitude of the 2nd wave: ", value=0.21)
frequency2 = st.number_input("Enter the frequency of the 2nd wave: ", value=0.34)
phase2 = st.number_input("Enter the phase shift of the 2nd wave: ")

if phase1 == 0:
    # computing each wave's y values
    wave1 = amplitude1 * np.sin(2*np.pi*frequency1*t) # wave 1's y values
    equation = f"y = {amplitude1}sin({frequency1}x) + y = {amplitude2}sin({frequency2}x)"
else:
    wave1 = amplitude1 * np.sin(2*np.pi*frequency1*t + phase1) # wave 1's y values
    equation = f"y = {amplitude1}sin({frequency1}x + phase1) + y = {amplitude2}sin({frequency2}x + phase1)"

if phase2 == 0:
    # computing each wave's y values
    wave2 = amplitude2 * np.sin(2*np.pi*frequency2*t) # wave 2's y values
    equation = f"y = {amplitude1}sin({frequency1}x) + y = {amplitude2}sin({frequency2}x)"
else:
    wave2 = amplitude2 * np.sin(2*np.pi*frequency2*t + phase2) # wave 1's y values
    equation = f"y = {amplitude1}sin({frequency1}x + phase1) + y = {amplitude2}sin({frequency2}x + phase2)"

superposition = wave1 + wave2 # y values of resulting function (superposition)

st.markdown("#### ━━━━━━━━━━━━━━━━━━━━━━ Superposition:")
fig, ax = plt.subplots()
ax.plot(t, wave1)
ax.plot(t, wave2)
ax.plot(t, superposition)
st.pyplot(fig)