# %%
#import os
import cv2
import PIL.Image
import numpy as np
#import pandas as pd
import streamlit as st
from csv import writer
from dotenv import load_dotenv
#from FollowUp import FollowUp as fu
import google.generativeai as genai
#from SendMessage import SendMessage as sm

#%% Setup
load_dotenv()
PATH_IMAGE = r'sample_pics/name_card_2.png'
PATH_IMAGE2 = r'sample_pics/name_card_3.png'

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
#%% Camera inputs
# Front side
img_file_buffer = st.camera_input("Take Front Side")

if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data,np.uint8),cv2.IMREAD_COLOR)

    cv2.imwrite(PATH_IMAGE,cv2_img)
    img = PIL.Image.open(PATH_IMAGE)

# Back side
if img_file_buffer is not None:
    img_file_buffer2 = st.camera_input("Take Back Side")
    
    if img_file_buffer2 is not None:
        bytes_data = img_file_buffer2.getvalue()
        cv2_img2 = cv2.imdecode(np.frombuffer(bytes_data,np.uint8),cv2.IMREAD_COLOR)

        cv2.imwrite(PATH_IMAGE2,cv2_img2)
        img2 = PIL.Image.open(PATH_IMAGE2)

#%% streamlit if button
    if img_file_buffer2 is not None:
        if st.button('Start Scanning'):
            with st.spinner():
                pass
                #%% Generate content with Gemini
                try:
                    name = model.generate_content(["Give me only the name from the card.", img,img2])
                    name = name.text
                    print(name)
                except:
                    print('Name Not Found')
                    name = 'NULL'

                if name == 'NULL':
                    try:
                        name = model.generate_content(["Guess the name from the email address and give me only the name.", img,img2])
                        name = name.text
                        print(name)
                    except:
                        print('Name Not Found')
                        name = 'NULL'
                st.header('Name',divider='rainbow')
                st.subheader(name)

                try: 
                    email = model.generate_content(["Based on the trend that email address usually include '@' and any combination of ['.com','.org','.edu','.my']. Give the email address in this card.", img,img2])
                    # email = model.generate_content(["Give me only the email address from the card. Based on the trend that email address usually include '@'r", img,img2])
                    email = email.text
                    print(email)
                except:
                    print('Email Not Found')
                    email = 'NULL'

                st.header('Email',divider='rainbow')
                st.subheader(email)

                try: 
                    phone_no = model.generate_content(["Give me only the mobile number from the card.", img,img2])
                    phone_no = phone_no.text
                    print(phone_no)

                except:
                    print('Phone Number Not Found')
                    phone_no = str(123456789)

                st.header('Phone Number',divider='rainbow')
                st.subheader(phone_no)
                
                try: 
                    pos = model.generate_content(["Give me only the position of the job from the card.", img,img2])
                    pos = pos.text
                    print(pos)

                except:
                    print('pos Not Found')
                    pos = 'NULL'

                st.header('Position',divider='rainbow')
                st.subheader(pos)
                
                try: 
                    com_name = model.generate_content(["Give me only the name of the company from the card.", img,img2])
                    com_name = com_name.text
                    print(com_name)

                except:
                    print('Company Name Not Found')
                    com_name = 'NULL'

                st.header('Company Name',divider='rainbow')
                st.subheader(com_name)
                
                try: 
                    com_vertical = model.generate_content(["Deduce the indutry vertical of the company from the card. return only a single word", img,img2])
                    com_vertical = com_vertical.text
                    print(com_vertical)

                except:
                    com_vertical = 'NULL'

                try: 
                    prio = model.generate_content([f"What is the priority of this person for leads conversion given that they are a {pos} from {com_name}. Return only a single word either [High, Medium, Low]", img,img2])
                    prio = prio.text
                    print(prio)

                except:
                    prio = 'NULL'
                    
                try: 
                    justi = model.generate_content([f"Given that the person is {pos} from {com_name}, provide justification as to why the leads conversion priority level would be {prio}. Answer in a single sentence", img,img2])
                    justi = justi.text
                    justi = justi.replace(",","")
                    print(justi)

                except:
                    justi = 'NULL'
            st.toast("All done!")    
        #%% Generate email based on profile

            #email_gen = model.generate_content([fu.email_prompt(pos=pos, com_name=com_name, com_vertical=com_vertical,name=name, course_dict=fu.course_dict)])

            #sm.send_email(email, "Automated Message by AI Nusantara Booth", email_gen.text)

            #sm.send_email(email, "Automated Message by AI Nusantara Booth", email_gen.text)
        #%% write data into csv and append
            with open('leads.csv', 'a', newline="") as fd:
                writer_object = writer(fd)
                writer_object.writerow([name, email, phone_no, pos, com_name, prio, justi])
                fd.close()