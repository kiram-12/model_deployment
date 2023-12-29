import os 
import cv2
import streamlit as st
import PIL
from PIL import Image
import json



st.set_page_config(page_title="My Webpage",page_icon=":purple_heart:",layout="wide", initial_sidebar_state="collapsed" )
#wide to display more content horizontally
st.subheader(" WELCOME TO OUR FIRST PROJECT ")
st.title("QUALITY DETECTION :heavy_check_mark: ")


#def load_lottiefile(filepath: str):
 #   with open(filepath,"r") as f:
  #      return json.load(f)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style.css")
#lottie_coding=load_lottiefile(r"C:\Users\dell\Desktop\website\lottie.json")
with st.container():
    st.write("----")
    left_column,right_column=st.columns(2)

    with left_column:
        st.header("The Purpose of our website")
        st.write("##") #espace
        st.write(
         """
---
Headline:
Revolutionizing Bottle Quality Assurance with AI

Overview:
Welcome to our innovative project dedicated to enhancing the quality assurance process in the industrial world. Leveraging the power of Artificial Intelligence, we have developed a cutting-edge system designed to detect and ensure the highest quality standards for bottles.

Problem Statement:
Traditional methods of quality assurance are often time-consuming, prone to errors, and may not keep pace with the demands of modern industry. Manual inspections can be inefficient, leading to potential quality issues and production bottlenecks.

Solution:
Our project introduces a state-of-the-art AI system that automates the bottle quality detection process. By employing advanced computer vision techniques and machine learning algorithms, we enable real-time, accurate assessments, significantly improving efficiency and reducing the likelihood of defects.

Key Features:
- Real-time quality assessment
- Increased accuracy and reliability
- Streamlined quality control processes
- Enhanced production efficiency
- Minimized manual inspection errors

Benefits:
- Improved product quality
- Reduced production downtime
- Enhanced overall efficiency
- Cost-effective quality control
""")
    centered_text = "<h2 style='text-align: center;'>Explore the future of bottle quality assurance with our AI-powered solution. Join us in revolutionizing the industry standards and ensuring excellence in every bottle produced.</h1>"
    st.markdown(centered_text, unsafe_allow_html=True)

with right_column:
        st.image("téléchargement.jpeg",width=600)
        
       
with st.container():
    st.write("---")
    st.header("OUR DATA")
    st.write("##")
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image("3.jpg",width=180)

    with text_column:
        st.subheader("DATA COLLECTION AND AUGMENTATION:")
        st.write(
            """
 In our pursuit of excellence in bottle quality detection, meticulous attention to data is at the core of our methodology. Our journey began with the manual capture of diverse datasets, where each bottle's unique characteristics were meticulously recorded. This painstaking process laid the foundation for a robust dataset that mirrors the real-world variability encountered in industrial settings.

To enhance the diversity and richness of our dataset, we employed advanced data augmentation techniques. Notably, we harnessed the power of CycleGAN, a state-of-the-art generative adversarial network (GAN), to transform and augment our images. This innovative approach allowed us to artificially expand our dataset, introducing variations in lighting conditions, orientations, and textures. The result is a model trained on a comprehensive dataset that excels in recognizing the intricacies of bottle quality under diverse circumstances.

Our commitment to data quality and diversity reflects our dedication to developing a robust and adaptive AI system, poised to revolutionize bottle quality assurance in the industrial landscape.            """

        )
with st.container():
    st.write("---")
    st.write("##")
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image("output.jpg")

    with text_column:
        st.subheader("Data Annotation and Model Training:")
        st.write(
            """
At the heart of our bottle quality detection project lies a meticulous process of data annotation and model training. To empower our artificial intelligence system with the ability to discern and classify bottle quality attributes, we turned to the Computer Vision Annotation Tool (CVAT). This powerful tool allowed us to efficiently label and annotate our dataset, providing the model with valuable insights into the specific features that define quality in the context of industrial bottles.

Our commitment to precision extended to the choice of our model architecture, and we opted for YOLOv8, a cutting-edge real-time object detection system. Leveraging the capabilities of YOLOv8, we embarked on a comprehensive training process, exposing the model to our annotated dataset. This iterative training regimen enabled our AI system to learn and adapt, ultimately mastering the intricacies of bottle quality detection.

The synergy between precise data annotation using CVAT and the advanced capabilities of YOLOv8 has culminated in a robust model ready to revolutionize bottle quality assurance, delivering unparalleled accuracy and efficiency in industrial settings.


            """
    
        )
st.write("[Learn more about Yollov8>>](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb)")
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    contact_form="""
    <form action="https://formsubmit.co/ikramnmili12@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false" >
     <input type="name" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email"  required>
     <textarea name="message" placeholder="Tap Your message here" required></textarea>
     <button type="submit"> Send </button>
    </form>
"""
left_column,right_column=st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()

with st.sidebar:
    st.header("TEST OUR MODEL")     # Adding header to sidebar
    # Adding file uploader to sidebar for selecting images
    source_img = st.sidebar.file_uploader("Choose an image", type=("jpg", "jpeg", "png", 'bmp', 'webp'))




    



  





