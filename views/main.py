import streamlit as st
import pandas as pd
import ydata_profiling 
from streamlit_pandas_profiling import st_profile_report
from pycaret.regression import setup, compare_models, pull, save_model
from feature_engine.imputation import MeanMedianImputer


st.set_page_config(page_title="DashML",page_icon='logo.png', layout='wide')

def sidebarView():
    with st.sidebar:
        st.image('logo.png',width=100)
        st.title('DashML')

        choice = st.radio('Navigation', ['Upload', 'Profiling', 'ML', 'Download'])
        st.info('Allows you to build an automated ML pipeline using streamlit, Pandas profiling and PyCaret')

    return choice


def upload():
    st.title('Upload your data for modelling')
    file = st.file_uploader('Upload your Dataset')

    if file:
        st.session_state.df = pd.read_csv(file, index_col=None)
        st.session_state.file = file
        st.dataframe(st.session_state.df,use_container_width=True)
    return file

def profiling():
    st.title('Automated Profile Report')

    df = st.session_state.df
    st.session_state.profile_report = df.profile_report(title='Profile Report', explorative=True, dark_mode=True)
    report = st.session_state.profile_report

    st_profile_report(report)

def ml_work(target,model):
    df = st.session_state.df
    imputer = MeanMedianImputer(imputation_method='mean')
    imputed_df = imputer.fit_transform(df)

    st.button("Run Modelling")
    setup(imputed_df, target=target)
    setup_df = pull()
    st.dataframe(setup_df)
    best_model = compare_models()
    compare_df = pull()
    save_model(best_model, 'best_model')
    st.dataframe(compare_df)

def ml_UI():
    st.session_state.type = st.select_slider('Select dataset type', ['Regression', 'Classification'])
    pass
    target = st.selectbox('Target', st.session_state.df.columns)

    if st.session_state.type == 'Regression':
        ml_work(target, 'Regression')
    else:
        pass
    


