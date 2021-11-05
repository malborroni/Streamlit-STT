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

#from scipy.io import wavfile

# import file
#filename_1 = "audio/TEST.wav"
filename_1 = "audio/Audio_1.wav"
filename_2 = "audio/Audio_2.wav"
img_logo = Image.open('images/logo.png')
white_img = Image.open('images/white.PNG')
overlay_1 = Image.open('images/audio_overlay_1.png')
overlay_2 = Image.open('images/audio_overlay_2.png')
scr_table_1 = Image.open('images/script_table_1.png')
scr_table_2 = Image.open('images/script_table_2.png')
CRM_match_1 = Image.open('images/CRM_table_1.png')
CRM_match_2 = Image.open('images/CRM_table_2.png')
result_1 = Image.open('images/result_VO_1.png')
result_2 = Image.open('images/result_VO_2.png')
specto_1 = Image.open('images/spectogram_1.png')
specto_2 = Image.open('images/spectogram_2.png')

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
example = st.sidebar.selectbox("Select a file ", [' - ', 'Q-1703186_VO.mp3', 'Q-2807995_VO.mp3'])

# analyze the file
#if example == "Example 1":
if example == "Q-1703186_VO.mp3":
    filename = filename_1

    spf_1 = wave.open(filename_1, "r")
    signal_1 = spf_1.readframes(-1)
    signal_1 = np.frombuffer(signal_1, "Int16")
    fs_1 = spf_1.getframerate()
    fr_1 = spf_1.getnframes()
    #time = np.linspace(0, len(signal) / fs, num=len(signal))
    #time = np.linspace(0,fr / fs)
    #signal = signal[:len(time)]
    time_1 = np.linspace(0, fr_1 / fs_1, num = len(signal_1))
    df_1 = pd.DataFrame({'time':time_1, 'signal':signal_1})
    
#    freq_1 = spf_1.getframerate()
#    samples_1 = spf_1.getnframes()
#    frames_1 = spf_1.readframes(samples_1)

    # Convert buffer to float32 using NumPy                                                                                 
#    audio_as_np_int16_1 = np.frombuffer(frames_1, dtype=np.int16)
    
# text from audio
    r = sr.Recognizer()
    with sr.AudioFile(filename_1) as source:
        audio_data = r.record(source)
        text_audio = r.recognize_google(audio_data, language = "it-IT")
        wordList_1 = re.sub("[^\w]", " ",  text_audio).split()
   
elif example == "Q-2807995_VO.mp3":
    filename = filename_2

    spf_2 = wave.open(filename_2, "r")
    signal_2 = spf_2.readframes(-1)
    signal_2 = np.frombuffer(signal_2, "Int16")
    fs_2 = spf_2.getframerate()
    fr_2 = spf_2.getnframes()
    #time = np.linspace(0, len(signal) / fs, num=len(signal))
    #time = np.linspace(0,fr / fs)
    #signal = signal[:len(time)]
    time_2 = np.linspace(0, fr_2 / fs_2, num = len(signal_2))
    df_2 = pd.DataFrame({'time':time_2, 'signal':signal_2})
    
#    freq_2 = spf_2.getframerate()
#    samples_2 = spf_2.getnframes()
#    frames_2 = spf_2.readframes(samples_2)

    # Convert buffer to float32 using NumPy                                                                                 
#    audio_as_np_int16_2 = np.frombuffer(frames_2, dtype=np.int16)
    
# text from audio
    r = sr.Recognizer()
    with sr.AudioFile(filename_2) as source:
        audio_data = r.record(source)
        text_audio = r.recognize_google(audio_data, language = "it-IT")
        wordList_2 = re.sub("[^\w]", " ",  text_audio).split()
        
else:
    pass

######################### INTRO #########################
with header:
    st.markdown('<div style="text-align:center"><span class="JTALK_1">J</span><span class="JTALK_2">AKALA // Cognitive Solutions</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center"><p class="big-font">Vocal Order Validation</p></div>', unsafe_allow_html=True)  
    st.write('\n\n\n')
    #st.image(white_img, width = 25)



######################## PLAY AUDIO #########################
with play:
    st.markdown('<div style="text-align:center"><p class="big-font">Play the Audio</p></div>', unsafe_allow_html=True)  
    if example == "Q-1703186_VO.mp3":
        audio_file = open(filename_1, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes)
    elif example == "Q-2807995_VO.mp3":
        audio_file = open(filename_2, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes)
    else:
        pass
        
#    audio_bytes = audio_file.read()
#    st.audio(audio_bytes)

    st.write('\n\n\n')
    #st.image(white_img, width = 25)
    but1, but2, but3, but4, but5 = st.beta_columns(5)
    if (but3.button("SPEECH")):
        st.write('\n\n\n')
        #st.image(white_img, width = 25)
        #st.write("« " + text_audio + " »")
        if example == "Q-1703186_VO.mp3":
            st.write("« " + "Egregio signor yyyyyy xxxxxx le ricordo che oggi è il ventidue due duemilaventuno e che la sto chiamando da Tunisi per conto di Iren Mercato S.p.A. con sede legale in Genova per proporle una nuova offerta di energia elettrica nel mercato libero chi lei ha accettato la chiamata provvedendo a Tunisi La informo che Lei per la conclusione del contratto di fornitura energia elettrica ha il diritto di scegliere di accettare l'offerta Iren Più Conveniente Luce Verde sul mercato libero dopo aver ricevuto la nostra proposta contrattuale in forma scritta ed averla accettata per iscritto Intende rinunciare al diritto di concludere il contratto in forma scritta mi conferma" + " »")
            st.write("« " + "Sì" + " »")
        elif example == "Q-2807995_VO.mp3":
            st.write("« " + "Mi conferma che oggi è il giorno primo luglio duemilaventi mi conferma" + " »")
            st.write("« " + "Sì" + " »")   
            st.write("« " + "Le chiedo la cortesia di confermarmi il suo nome e cognome signora" + " »")
            st.write("« " + "xxxxxx yyyyyy" + " »")
            st.write("« " + "La sua data di nascita" + " »")
            st.write("« " + "Uno uno cinquantadue" + " »")
            st.write("« " + "Dove è nata" + " »")
            st.write("« " + "Valsinni" + " »")
            st.write("« " + "Perfetto Mi conferma che l’immobile presso il quale verrà erogata la fornitura di energia elettrica e gas è da lei occupato a titolo di proprietario o inquilino?" + " »")
            st.write("« " + "E proprietaria" + " »")   
            st.write("« " + "Le ricordo che per pagare le bollette attraverso la domiciliazione bancaria è necessario che mi confermi le seguenti informazioni Mi conferma di aver autorizzato Iren Mercato a richiedere in base alla normativa bancaria SEPA l’addebito permanente Core in conto corrente bancario per il pagamento alla data di scadenza dell’obbligazione delle bollette?" + " »")
            st.write("« " + "Sì" + " »")   
        
        else:
            pass
            


######################### AUDIO #########################
with sound:
    st.write('\n\n\n')
    #st.image(white_img, width = 25)

    but1, but2, but3, but4, but5 = st.beta_columns(5)

    # chart = alt.Chart(df).mark_line().encode(x='time', y='signal', color='key:N')
    # st.altair_chart(chart)
    
    if (but3.button("CALCULATE")):
        
        if example == "Q-1703186_VO.mp3":        
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
            plt.plot(time_1, signal_1, color = '#B41E3C')
            st.pyplot(plt)

            #st.image(white_img, width = 25)
            st.write('\n\n\n')
                        
#            plt.figure(figsize=(35,10))
#            plt.title("Spectogram \n", fontsize = 35)
#            plt.xlabel('\n Time (s)', fontsize = 30)
#            plt.ylabel('Frequency \n', fontsize = 30)
#            plt.xticks(fontsize = 25)
#            plt.yticks(fontsize = 25)
#            plt.specgram(audio_as_np_int16_1, Fs=freq_1)
#            plt.show()
#            st.pyplot(plt)

            plt.figure(figsize=(35,10))
            plt.axis('off')
            plt.imshow(specto_1) 
            st.pyplot(plt)  # display it

            
            st.write('\n\n\n')
            st.write('\n\n\n')
            
        elif example == "Q-2807995_VO.mp3":
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
            plt.plot(time_2, signal_2, color = '#B41E3C')
            st.pyplot(plt)

            #st.image(white_img, width = 25)
            st.write('\n\n\n')
            
 #           plt.figure(figsize=(35,10))
 #           plt.title("Spectogram \n", fontsize = 35)
 #           plt.xlabel('\n Time (s)', fontsize = 30)
 #           plt.ylabel('Frequency \n', fontsize = 30)
 #           plt.xticks(fontsize = 25)
 #           plt.yticks(fontsize = 25)
 #           plt.specgram(audio_as_np_int16_2, Fs=freq_2)
 #           st.pyplot(plt)             
    
            plt.figure(figsize=(35,10))
            plt.axis('off')
            plt.imshow(specto_2) 
            st.pyplot(plt)  # display it

            
            st.write('\n\n\n')
            st.write('\n\n\n')
            
        else:
            pass


        st.markdown('<div style="text-align:center"><p class="medium-font">Script Components Extraction</p></div>', unsafe_allow_html=True)  
        
        if example == "Q-1703186_VO.mp3":
            #st.image(overlay_1, width = 720)  
            #st.image(scr_table_1, width = 740)
            
            plt.figure(figsize=(35,10))
            plt.axis('off')
            plt.imshow(overlay_1) 
            st.pyplot(plt)  # display it
            
            plt.figure(figsize=(35,10))
            plt.axis('off')
            plt.imshow(scr_table_1) 
            st.pyplot(plt)  # display it
            
            st.write('\n\n\n')
            #st.write('\n\n\n')            

        elif example == "Q-2807995_VO.mp3":
            #st.image(overlay_2, width = 720)  
            #st.image(scr_table_2, width = 740)   
            
            plt.figure(figsize=(35,10))
            plt.axis('off')
            plt.imshow(overlay_2) 
            st.pyplot(plt)  # display it
            
            plt.figure(figsize=(35,10))
            plt.axis('off')
            plt.imshow(scr_table_2) 
            st.pyplot(plt)  # display it    
            
            st.write('\n\n\n')
            #st.write('\n\n\n')
            
        else:
            pass
       
    
        st.markdown('<div style="text-align:center"><p class="medium-font">CRM Info Matching</p></div>', unsafe_allow_html=True)  
        
        if example == "Q-1703186_VO.mp3":
            #st.image(overlay_1, width = 720)  
            #st.image(scr_table_1, width = 740)
            
            plt.figure(figsize=(35,10))
            plt.axis('off')
            plt.imshow(CRM_match_1) 
            st.pyplot(plt)  # display it
            
            st.write('\n\n\n')
            #st.write('\n\n\n')            

        elif example == "Q-2807995_VO.mp3":
            #st.image(overlay_2, width = 720)  
            #st.image(scr_table_2, width = 740)   
            
            plt.figure(figsize=(35,10))
            plt.axis('off')
            plt.imshow(CRM_match_2) 
            st.pyplot(plt)  # display it   
            
            st.write('\n\n\n')
            #st.write('\n\n\n')
            
        else:
            pass
            
            
 #       st.markdown('<div style="text-align:center"><p class="medium-font">Registered KPIs</p></div>', unsafe_allow_html=True) 

#        kpi1_col, kpi2_col = st.beta_columns(2)
        
        # First column
#        if example == "Q-1703186_VO.mp3":
#            kpi1_col.markdown('<div style="text-align:left"><p class="medium-font">General Overview:</p></div>', unsafe_allow_html=True)
#            kpi1_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Total length: </b></p></div>', unsafe_allow_html=True)
#            kpi1_col.write("&emsp;" + str(round(time_1[-1],1)) + ' sec.')
#            kpi1_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Number of words: </b></p></div>', unsafe_allow_html=True)
#            kpi1_col.write("&emsp;" + str(len(wordList_1)))
#            kpi1_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Number of sentences: </b></p></div>', unsafe_allow_html=True)
#            kpi1_col.write("&emsp;4")
#        elif example == "Q-2807995_VO.mp3":
#            kpi1_col.markdown('<div style="text-align:left"><p class="medium-font">General Overview:</p></div>', unsafe_allow_html=True)
#            kpi1_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Total length: </b></p></div>', unsafe_allow_html=True)
#            kpi1_col.write("&emsp;" + str(round(time_2[-1],1)) + ' sec.')
#            kpi1_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Number of words: </b></p></div>', unsafe_allow_html=True)
#            kpi1_col.write("&emsp;" + str(len(wordList_2)))
#            kpi1_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Number of sentences: </b></p></div>', unsafe_allow_html=True)
#            kpi1_col.write("&emsp;13")

#        else:
#            pass

            

        # Second column
#        if example == "Q-1703186_VO.mp3":
#            kpi2_col.markdown('<div style="text-align:left"><p class="medium-font">Conversation details:</p></div>', unsafe_allow_html=True)
#            kpi2_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Opening: </b></p></div>', unsafe_allow_html=True)
#            kpi2_col.write('&emsp;35 sec.')
#            kpi2_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Vocal Order: </b></p></div>', unsafe_allow_html=True)
#            kpi2_col.write('&emsp;5 sec.')
#            kpi2_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Customer answer(s): </b></p></div>', unsafe_allow_html=True)
#            kpi2_col.write('&emsp;1 sec.')
 
#        elif example == "Q-2807995_VO.mp3":
#            kpi2_col.markdown('<div style="text-align:left"><p class="medium-font">Conversation details:</p></div>', unsafe_allow_html=True)
#            kpi2_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Date confirmation: </b></p></div>', unsafe_allow_html=True)
#            kpi2_col.write('&emsp;3 sec.')
#            kpi2_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Generalità: </b></p></div>', unsafe_allow_html=True)
#            kpi2_col.write('&emsp;7 sec.')
#            kpi2_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Conferma titolo: </b></p></div>', unsafe_allow_html=True)
#            kpi2_col.write('&emsp;7/8 sec.')
#            kpi2_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Header Domiciliazione: </b></p></div>', unsafe_allow_html=True)
#            kpi2_col.write('&emsp;7 sec.')
#            kpi2_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Conferma Autorizzazione SEPA: </b></p></div>', unsafe_allow_html=True)
#            kpi2_col.write('&emsp;10 sec.')
#            kpi2_col.markdown('<div style="text-align:left"><p class="small-font">&#8226; <b> Customer answer(s): </b></p></div>', unsafe_allow_html=True)
#            kpi2_col.write('&emsp;8 sec.')
            
#        else:
#            pass

    st.write('\n\n\n')
    but1, but2, but3, but4, but5 = st.beta_columns(5)
            
    if (but3.button("RESULT")):
        
        if example == "Q-1703186_VO.mp3":
            
            plt.figure(figsize=(35,10))
            plt.axis('off')
            plt.imshow(result_1) 
            st.pyplot(plt)  # display it
            
            st.write('\n\n\n')
            #st.write('\n\n\n')            

        elif example == "Q-2807995_VO.mp3":   
            
            plt.figure(figsize=(35,10))
            plt.axis('off')
            plt.imshow(result_2) 
            st.pyplot(plt)  # display it   
            
            st.write('\n\n\n')
            #st.write('\n\n\n')
            
        else:
            pass
            
    st.write('\n\n\n')
    st.write('\n\n\n')
    #st.image(white_img, width = 25)

