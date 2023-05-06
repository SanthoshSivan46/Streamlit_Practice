#Program to calculate BMI
import streamlit as vAR_st
def BMI():
    #vAR_st.markdown("<h1 style='text-align: center; color: black; font-size:29px;'>Application to calculate BMI</h1>", unsafe_allow_html=True)
    col1,col2,col5,col6= vAR_st.columns((0.5,2,2,0.7))
    
    with col2:
        vAR_st.write('')
        vAR_st.write('')
        vAR_st.subheader('Select your category')
    
    with col5:
        category = vAR_st.selectbox('',('Adult','Child'))
    
    with col2:
        vAR_st.write('')
        vAR_st.subheader('Select the height format')
    
    with col5:
        status = vAR_st.selectbox('',('cms','meters','feet'),key='clear6')
    
    col1,col2,col3=vAR_st.columns((0.5,3.6,0.6))
    col3,col4,col5,col6= vAR_st.columns((5,2,2,5))
    col6,col7,col8=vAR_st.columns((0.1,2,0.1))
    with col4:
        vAR_st.write("")
        vAR_K=vAR_st.button('Submit')

    with col2:
        weight = vAR_st.slider("Select your weight(in kgs)",0,200,key='clear2')
    
    if status=='cms':
        with col2:
            height = vAR_st.slider("Select your height",0,240,key='clear3')
            if vAR_K:
                try:
                    bmi = weight/((height/100)**2)
                    bmi=round(bmi,2)
                    vAR_st.success("Your BMI Index is {}".format(bmi))
                    if category=="Adult":
                        if(bmi < 16):
                            with col2:
                                vAR_st.error("You are Extremely Underweight")
                        elif(bmi >= 16 and bmi < 18.5):
                            with col2:
                                vAR_st.warning("You are Underweight")
                        elif(bmi >= 18.5 and bmi < 25):
                            with col2:
                                vAR_st.success("Healthy")
                        elif(bmi >= 25 and bmi < 30):
                            with col2:
                                vAR_st.warning("Overweight")
                        elif(bmi >= 30):
                            with col2:
                                vAR_st.error("Extremely Overweight")
                    else:
                        if(bmi < 13):
                            with col2:
                                vAR_st.error("You are Extremely Underweight")
                        elif(bmi >= 13 and bmi < 16):
                            with col2:
                                vAR_st.warning("You are Underweight")
                        elif(bmi >= 16 and bmi < 18):
                            with col2:
                                vAR_st.success("Healthy")
                        elif(bmi > 18 and bmi <= 21):
                            with col2:
                                vAR_st.warning("Overweight")
                        elif(bmi >= 22):
                            with col2:
                                vAR_st.error("Extremely Overweight")
                except ZeroDivisionError:
                    with col2:
                        vAR_st.info("Height or Weight cannot be zero")
    
    elif status=="meters":
        with col2:
            height = vAR_st.slider("Select your height",0.0,10.0,key='clear4')
            if vAR_K:
                try:
                    bmi = weight/(height**2)
                    bmi=round(bmi,2)
                    vAR_st.success("Your BMI Index is {}".format(bmi))
                    if category=="Adult":
                        if(bmi < 16):
                            with col2:
                                vAR_st.error("You are Extremely Underweight")
                        elif(bmi >= 16 and bmi < 18.5):
                            with col2:
                                vAR_st.warning("You are Underweight")
                        elif(bmi >= 18.5 and bmi < 25):
                            with col2:
                                vAR_st.success("Healthy")
                        elif(bmi >= 25 and bmi < 30):
                            with col2:
                                vAR_st.warning("Overweight")
                        elif(bmi >= 30):
                            with col2:
                                vAR_st.error("Extremely Overweight")
                    else:
                        if(bmi < 13):
                            with col2:
                                vAR_st.error("You are Extremely Underweight")
                        elif(bmi >= 13 and bmi < 16):
                            with col2:
                                vAR_st.warning("You are Underweight")
                        elif(bmi >= 16 and bmi < 18):
                            with col2:
                                vAR_st.success("Healthy")
                        elif(bmi > 18 and bmi <= 21):
                            with col2:
                                vAR_st.warning("Overweight")
                        elif(bmi >= 22):
                            with col2:
                                vAR_st.error("Extremely Overweight")
                except ZeroDivisionError:
                    with col2:
                        vAR_st.info("Height or Weight cannot be zero")



    
    else:
        with col2:
            height= vAR_st.slider("Select your height",0.0,10.0,key='clear5')
            if vAR_K:
                try:
                    bmi = weight/((height/3.28)**2)
                    bmi=round(bmi,2)
                    vAR_st.success("Your BMI Index is {}".format(bmi))
                    if category=="Adult":
                        if(bmi < 16):
                            with col2:
                                vAR_st.error("You are Extremely Underweight")
                        elif(bmi >= 16 and bmi < 18.5):
                            with col2:
                                vAR_st.warning("You are Underweight")
                        elif(bmi >= 18.5 and bmi < 25):
                            with col2:
                                vAR_st.success("Healthy")
                        elif(bmi >= 25 and bmi < 30):
                            with col2:
                                vAR_st.warning("Overweight")
                        elif(bmi >= 30):
                            with col2:
                                vAR_st.error("Extremely Overweight")
                    else:
                        if(bmi < 13):
                            with col2:
                                vAR_st.error("You are Extremely Underweight")
                        elif(bmi >= 13 and bmi < 16):
                            with col2:
                                vAR_st.warning("You are Underweight")
                        elif(bmi >= 16 and bmi < 18):
                            with col2:
                                vAR_st.success("Healthy")
                        elif(bmi > 18 and bmi <= 21):
                            with col2:
                                vAR_st.warning("Overweight")
                        elif(bmi >= 22):
                            with col2:
                                vAR_st.error("Extremely Overweight")
                except ZeroDivisionError:
                    with col2:
                        vAR_st.info("Height or Weight cannot be zero")
                                
               
    
    
    def clear_text():
        vAR_st.session_state["clear"]=""
        vAR_st.session_state['clear2']=0
        vAR_st.session_state['clear3']=0
        vAR_st.session_state['clear4']=0.0
        vAR_st.session_state['clear5']=0.0
        vAR_st.session_state['clear6']='cms'

    
    
    
    
    

    #col3,col4,col5,col6= vAR_st.columns((5,2,2,5))
    
    #with col4:
        #vAR_st.write("")
        #if(vAR_st.button('Submit')):
            # print the BMI INDEX
            #with col2:
             #   bmi=round(bmi,2)
              #  vAR_st.subheader("Your BMI Index is {}".format(bmi))
            
        
    with col5:
        vAR_st.write("")
        vAR_st.button("clear",on_click=clear_text)

