import streamlit as st
from streamlit_option_menu import option_menu
import math
import datetime
from datetime import date
import calendar
from PIL import Image
import source.title_1 as head
# with open('style/final.css') as f:
#         st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
def average():
    head.title()
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Average </p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((4,3,3,6))
    with col1:
        st.markdown("")
        st.write("# Enter the Series ")
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["Clear_Avg"] = ""
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_num=st.text_input("",placeholder="Eg:00,00,00",key="Clear_Avg")  
        vAR_list=[]
    #----- Average -------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                try:
                    if vAR_input_num != '':
                        vAR_input_data = vAR_input_num.split(",")
                        for i in vAR_input_data:
                            vAR_num=float(i)
                            vAR_list.append(vAR_num)
                        def Average(vAR_list):
                            vAR_avg= sum(vAR_list) / len(vAR_list)
                            vAR_avg=round(vAR_avg,4)
                            st.success(vAR_avg)
                        Average(vAR_list)
                    else:
                        st.error("Error")
                    with col1:
                        st.write("# Average ")
                except BaseException as error:
                    st.error("Enter the Valid data")
