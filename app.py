import streamlit as st
import os
import model

# title
st.title('Play Local WAV File')

# text input
text = st.text_input('Please enter text')

# file selection and playback
wav_files = ['input.wav', 'output.wav']
for file in wav_files:
    if os.path.isfile(file):
        if st.button(f'Play {file}'):
            audio_file = open(file, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
    else:
        st.write(f'{file} does not exist.')

if st.button('Create Melody') and text != '':
    model.genetate_melody(text)