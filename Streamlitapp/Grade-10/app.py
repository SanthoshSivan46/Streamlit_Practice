import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")
import math
from PIL import Image
import source.title_1 as head
import source.frustum as fstm
import source.sd_var as sd
import source.section_formula as sec
import source.tables as tri
import source.areaquad as area
import source.areatri as areatri
import source.collinear as collin

with open('/app/ai-lab-schools/Streamlitapp/Grade-10/style/final.css') as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
imcol1, imcol2, imcol3 = st.columns((2,5,3))
with imcol1:
    st.write("")
with imcol2:
    st.image('/app/ai-lab-schools/Streamlitapp/Grade-10/image/Logo_final.png')
with imcol3:
    st.write("")
#---------Side bar-------#
with st.sidebar:
    selected = st.selectbox("",
                     ['Home',"Section Formula","Area of Quadrilateral","Area of Triangle","Collinear Check","Volume of Frustum","Trigonometry Table","Standard Deviation & varience"],key='text')
    Library = st.selectbox("",
                     ["Library Used","Streamlit","Streamlit-option-Menu","Image","Math","Pandas"],key='text1')
    Gcp_cloud = st.selectbox("",
                     ["GCP Services Used","VM Instance","Computer Engine","Cloud Storage"],key='text2')
    st.markdown("")
    def clear_text():
            st.session_state["text"] = "Home"
            st.session_state["text1"] = "Library Used"
            st.session_state["text2"] = "GCP Services Used"
    st.button("Clear/Reset", on_click=clear_text)

#--------------function calling-----------#
if __name__ == "__main__":
    try:
        if selected == "Home":
            head.title()
        if selected == "Section Formula":
            sec.Section_1() 
        if selected == "Trigonometry Table":
            tri.table_1()
        if selected == "Area of Quadrilateral" :
            area.area()
        if selected == "Area of Triangle" :
            areatri.atri()
        if selected == "Collinear Check" :
            collin.colli()
        if selected == "Volume of Frustum":
            fstm.frustum()
        if selected == "Standard Deviation & varience":
            sd.stats()
    except BaseException as error:
        st.error(error)
