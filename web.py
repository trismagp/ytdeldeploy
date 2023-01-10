import os
from pytube import YouTube
from datetime import datetime
import streamlit as st

def rename_file(out_file, file_ext):
    now = datetime.now()
    current_time = now.strftime("%Y%d%m_%H%M%S")
    base, ext = os.path.splitext(out_file)
    new_file = base + current_time + '.' + file_ext
    os.rename(out_file, new_file)

def download_360p_mp4_videos(url: str, file_format: str,outpath: str = "./"):
    yt = YouTube(url)
    if file_format == "music":
        out_file = yt.streams.filter(only_audio=True).first().download()
        rename_file(out_file, "mp3")
    else:
        out_file = yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download()
        rename_file(out_file, "mp4")
    return yt.title

st.title('My youyou downloader')
st.subheader('this is my music and video downloader')
st.selectbox('Which file format?',('music', 'video'), key="file_format")
st.text_input(label='YT url',placeholder='input youtube url here...', key="url")
st.text_input(label='output path',value= 'C:\\Users\\Public\\Downloads',placeholder='output path here...', key="output")



if st.button('Download'):
    url = st.session_state['url']
    output = st.session_state['output']
    file_format = st.session_state['file_format'].strip()
    title = download_360p_mp4_videos(url,file_format,output)

    
    
    

