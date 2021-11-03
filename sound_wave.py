#import os 

# import library
import streamlit as st
from PIL import Image
import wave
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import altair as alt

import speech_recognition as sr
import re

from annotated_text import annotated_text

# import file
#filename_1 = "audio/TEST.wav"
filename_1 = "audio/Audio_1.wav"
filename_2 = "audio/Audio_2.wav"
img_logo = Image.open('images/logo.png')
white_img = Image.open('images/white.PNG')
overlay_1 = Image.open('images/grafico_audio_1_overlay.png')
scr_table_1 = Image.open('images/tabella_script_1_v2.png')

######################### STREAMLIT #########################
header = st.beta_container()
play = st.beta_container()
sound = st.beta_container()
kpi = st.beta_container()

st.markdown("""
<style>
.JTALK_1 {font-size:40px !important; font-family: arial black;color: #B41E3C}
.JTALK_2 {font-size:40px !important; font-family: arial black;color: #002060}
.big-font {font-size:30px !important; font-family: arial black;color: #002060}
.medium-font {font-size:20px !important; font-family: arial black;color: #002060}
.small-font {font-size:15px !important; font-family: arial;color: #000000}
</style>
""", unsafe_allow_html=True)

# side bar
st.sidebar.image(img_logo, width = 180)
#example = st.sidebar.selectbox("Select a file ", ['Example 1'])
example = st.sidebar.selectbox("Select a file ", ['Q-1703186_VO.mp3', 'Q-2807995_VO.mp3'])

# analyze the file
#if example == "Example 1":
if example == "Q-1703186_VO.mp3":
    filename = filename_1

    spf = wave.open(filename, "r")
    signal = spf.readframes(-1)
    signal = np.frombuffer(signal, "Int16")
    fs = spf.getframerate()
    fr = spf.getnframes()
    #time = np.linspace(0, len(signal) / fs, num=len(signal))
    #time = np.linspace(0,fr / fs)
    #signal = signal[:len(time)]
    time = np.linspace(0, fr / fs, num = len(signal))
    df = pd.DataFrame({'time':time, 'signal':signal})
    
# text from audio
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text_audio = r.recognize_google(audio_data, language = "it-IT")
        wordList = re.sub("[^\w]", " ",  text_audio).split()
   
elif example == "Q-2807995_CCA.mp3":
    filename = filename_2

    spf = wave.open(filename, "r")
    signal = spf.readframes(-1)
    signal = np.frombuffer(signal, "Int16")
    fs = spf.getframerate()
    fr = spf.getnframes()
    #time = np.linspace(0, len(signal) / fs, num=len(signal))
    #time = np.linspace(0,fr / fs)
    #signal = signal[:len(time)]
    time = np.linspace(0, fr / fs, num = len(signal))
    df = pd.DataFrame({'time':time, 'signal':signal})
    
# text from audio
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text_audio = r.recognize_google(audio_data, language = "it-IT")
        wordList = re.sub("[^\w]", " ",  text_audio).split()

######################### INTRO #########################
with header:
    st.markdown('<div style="text-align:center"><span class="JTALK_1">J</span><span class="JTALK_2">AKALA // Customer Operation</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center"><p class="big-font">Process Mining of an IVR</p></div>', unsafe_allow_html=True)  
    st.write('\n\n\n')
    #st.image(white_img, width = 25)



######################## PLAY AUDIO #########################
with play:
    st.markdown('<div style="text-align:center"><p class="big-font">Play the Audio</p></div>', unsafe_allow_html=True)  
    audio_file = open(filename, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes)

    st.write('\n\n\n')
    #st.image(white_img, width = 25)
    but1, but2, but3, but4, but5 = st.beta_columns(5)
    if (but3.button("SPEECH")):
        st.write('\n\n\n')
        #st.image(white_img, width = 25)
        #st.write("« " + text_audio + " »")
        st.write("« " + "Egregio signor Guglielmo Alberto Barletta le ricordo che oggi è il ventidue duemilaventuno e che la sto chiamando da Tunisi per conto di Iren Mercato S.p.A. con sede legale in Genova per proporle una nuova offerta di energia elettrica nel mercato libero chi lei ha accettato la chiamata provvedendo a Tunisi La informo che Lei per la conclusione del contratto di fornitura energia elettrica ha il diritto di scegliere di accettare l'offerta Più Conveniente Luce Verde sul mercato libero dopo aver ricevuto la nostra proposta contrattuale in forma scritta ed averla accettata per iscritto Intende rinunciare al diritto di concludere il contratto in forma scritta mi conferma" + " »")
        st.write("« " + "Sì" + " »")
            


######################### AUDIO #########################
with sound:
    st.write('\n\n\n')
    #st.image(white_img, width = 25)

    but1, but2, but3, but4, but5 = st.beta_columns(5)

    # chart = alt.Chart(df).mark_line().encode(x='time', y='signal', color='key:N')
    # st.altair_chart(chart)
    
    if (but3.button("CALCULATE")):
        st.write('\n\n\n')
        st.write('\n\n\n')
        #st.image(white_img, width = 25)

        plt.figure(figsize=(35,10))
        plt.title("Signal Wave \n", fontsize = 35)
        plt.xlabel('\n Time (s)', fontsize = 30)
        plt.ylabel('Amplitude \n', fontsize = 30)
        plt.xticks(fontsize = 25)
        plt.yticks(fontsize = 25)
        #plt.plot(time, signal, color = '#143C73')
        plt.plot(time, signal, color = '#B41E3C')
        st.pyplot(plt)

        #st.image(white_img, width = 25)
        st.write('\n\n\n')
        st.write('\n\n\n')

        st.markdown('<div style="text-align:center"><p class="medium-font">Registered KPIs</p></div>', unsafe_allow_html=True)  
        
        st.image(overlay_1, width = 720)
        
        st.image(scr_table_1, width = 740)
        
        kpi1_col, kpi2_col = st.beta_columns(2)
        
        # First column
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font">General Overview:</p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Total length: </b></p></div>', unsafe_allow_html=True)
        kpi1_col.write("&emsp;" + str(round(time[-1],1)) + ' sec.')
        kpi1_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Number of words: </b></p></div>', unsafe_allow_html=True)
        kpi1_col.write("&emsp;" + str(len(wordList)))
        kpi1_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Number of sentences: </b></p></div>', unsafe_allow_html=True)
        kpi1_col.write("&emsp;4")

        # Second column
        kpi2_col.markdown('<div style="text-align:left"><p class="medium-font">Conversation details:</p></div>', unsafe_allow_html=True)
        kpi2_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Greeting: </b></p></div>', unsafe_allow_html=True)
        kpi2_col.write('&emsp;2 sec.')
        kpi2_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Formal introduction: </b></p></div>', unsafe_allow_html=True)
        kpi2_col.write('&emsp;16 sec.')
        kpi2_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Next steps definition: </b></p></div>', unsafe_allow_html=True)
        kpi2_col.write('&emsp;15 sec.')
        kpi2_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Operator renunciation question: </b></p></div>', unsafe_allow_html=True)
        kpi2_col.write('&emsp;6 sec.')
        kpi2_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Customer renunciation answer: </b></p></div>', unsafe_allow_html=True)
        kpi2_col.write('&emsp;1 sec.')


    st.write('\n\n\n')
    st.write('\n\n\n')
    #st.image(white_img, width = 25)

