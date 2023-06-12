import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import os
import base64

# Title
st.title('Upload and Visualize WAV File')

# Text input
text = st.text_input('Please enter text')

# File upload
uploaded_file = st.file_uploader("Please upload a WAV file", type="wav")
if uploaded_file is not None:
    # Temporarily save the file
    with open('temp.wav', 'wb') as f:
        f.write(uploaded_file.getbuffer())
    
    # Read the file
    rate, data = read('temp.wav')
    
    # Play the file (provide a link)
    audio_file = open('temp.wav', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/wav')
    
    # Visualize the waveform
    fig, ax = plt.subplots()
    time = np.arange(0, len(data)) / rate
    ax.plot(time, data)
    ax.set(xlabel='Time [s]', ylabel='Amplitude')
    st.pyplot(fig)
    
    # Delete the temporary file
    os.remove('temp.wav')
