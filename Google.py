from googlesearch import search
import streamlit as st


# PAGE CONFIG
st.set_page_config(layout="wide",
                   page_title="Google",
                   page_icon="content/google.ico",
                   initial_sidebar_state="collapsed")

src,o=st.tabs(["Search","other"])

#------------------ side bar parameters
lg=st.sidebar.selectbox("Search Language",["fr","en"])
nbr=st.sidebar.slider("Result Number",2,80,value=10)


# --- Functions
def google_search(query):
    cols=[]
    for k in search(query, lang=lg, num_results=nbr,advanced=True):
        if "http" in k.url:
            cols+=[src.columns([1,8])]
            cols[-1][0].link_button("GO",url=k.url)
            cols[-1][1].title(k.title)
            src.text(k.description)
            src.divider()



#---------------------- main page : search
para=src.columns([10,100])
choice=para[1].text_input("Google search")

launch=para[0].button("Search",on_click=google_search, args=(choice,),type="primary")

        
