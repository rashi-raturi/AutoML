import streamlit as st
from views import main

# Initialising df session state for storing  
if 'file' not in st.session_state:
    st.session_state.file = ''
if 'df' not in st.session_state:
    st.session_state.df = ''
if 'profile_report' not in st.session_state:
    st.session_state.profile_report = ''
if 'type' not in st.session_state:
    st.session_state.type = ''


choice = main.sidebarView()
    
if choice == 'Upload':
    main.upload()

if choice == 'Profiling':
    main.profiling()

if choice == 'ML':
    main.ml_UI()

if choice == 'Download':
    pass
