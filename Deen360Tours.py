import streamlit as st
from PIL import Image
img = Image.open("pix.jpg")
st.image(img, caption = 'nature is LIFE @ Deen360Tour', width = 300)

import time
import datetime
from datetime import datetime, date, time

head ='<p style = "font-family:Algerian; color:Maroon; font-size:30px;">WELCOME TO DEEN360 TOURS</p>'
st.markdown(head, unsafe_allow_html =True)

subheader = '<p style = "font-family: Courier; color: Blue; font-size:12px;">How you spend your time does not determine how much time you have got. RELAX!!!</p>'
st.markdown(subheader, unsafe_allow_html =True)


user = st.sidebar.text_input('Type Tourist Name')

booking = st.sidebar.radio('Hi '+user.title() +' would you like to tour with us?', (' ','Yes','No'))
if booking =='No':
    st.error("Maybe Another Time")
elif booking == ' ':
    st.error("Kindly select an option")
elif booking == 'Yes':
    st.success("Proceed to book a tour")
          
    st.write('\nKindly choose a tour class: \n')
    
    #Layout
    col1, col2 = st.columns(2)  
    with col1:
        tour_class= st.selectbox('Available classes of tour', ['---select a class---','Dubai in Tokyo', 'Paris in Milan', 'Vegas in Ontario', 'Zanzibar in Abuja'])
        if tour_class =='Dubai in Tokyo':
    
            st.write('mountain experience, city tour, local market tour, bar covered and third class accommodation')
            st.write('$200 per day')
            image = Image.open('pix2.jpg')
            st.image(image, caption='Dubai in Tokyo', width = 600)
            st.write("When do you wish to resume your tour?")
            starting_date = st.date_input("choose date")
    
       
            n = st.number_input('How many days will you like to tour with us?', step =1)
            if n>=1:
                st.write('Amount= $ ',  n*200)
        
                status = st.radio("choose payment method: ", ('MasterCard', 'Bank Transfer', 'Paystack', 'Cash'))
                if(status == 'MasterCard'):
                    st.error('unavailable')
                elif(status == 'Bank Transfer'):
                    st.error('unavailable')
                elif(status == 'Paystack'):
                    st.error('unavailable')
                else:
                    st.success('Payment accepted')
                    if st.button('Generate ID'):
                        st.text('CONGRATULATIONS!!! your tour ID is xxx')
            
       
            else:
                st.error('Kindly choose a figure')
        
    
           
        if tour_class =='Paris in Milan':
    
            st.write('mountain experience, city tour, local market tour, fishing tour, swimming in red spring, bar, clubbing covered and second class accommodation')
            st.write('$300 per day')
            image = Image.open('pix3.jpg')
            st.image(image, caption='Paris in Milan', width = 600)
            st.write("When do you wish to resume your tour?")
            starting_date = st.date_input("choose date")
            n = st.number_input('How many days will you like to tour with us?', step =1)
            if n>=1:
                st.write('Amount= $ ',  n*300)
        
                status = st.radio("choose payment method: ", ('MasterCard', 'Bank Transfer', 'Paystack', 'Cash'))
                if(status == 'MasterCard'):
                    st.error('unavailable')
                elif(status == 'Bank Transfer'):
                    st.error('unavailable')
                elif(status == 'Paystack'):
                    st.error('unavailable')
                else:
                    st.success('Payment accepted')
                    if st.button('Generate ID'):
                        st.text('CONGRATULATIONS!!! your tour ID is xxx')
       
            else:
                st.error('Kindly choose a figure')

        elif tour_class =='Vegas in Ontario':
    
            st.write('mountain experience, city tour, local market tour, fishing tour, swimming in red spring, bar, clubbing, gym, sports covered and first class accommodation')
            st.write('$400 per day')
            image = Image.open('pix1.jpg')
            st.image(image, caption='Vegas in Ontario', width = 600)
            st.write("When do you wish to resume your tour?")
            starting_date = st.date_input("choose date")
            n = st.number_input('How many days will you like to tour with us?', step =1)
            if n>=1:
                st.write('Amount= $ ',  n*400)
        
                status = st.radio("choose payment method: ", ('MasterCard', 'Bank Transfer', 'Paystack', 'Cash'))
                if(status == 'MasterCard'):
                    st.error('unavailable')
                elif(status == 'Bank Transfer'):
                    st.error('unavailable')
                elif(status == 'Paystack'):
                    st.error('unavailable')
                else:
                    st.success('Payment accepted')
                    if st.button('Generate ID'):
                        st.text('CONGRATULATIONS!!! your tour ID is xxx')
       
            else:
                st.error('Kindly choose a figure')
        
        elif tour_class =='Zanzibar in Abuja':
    
            st.write('mountain experience, city tour, local market tour, fishing tour, swimming in red spring, bar, clubbing, gym, sports, golf tour covered and first class accommodation')
            st.write('$500 per day')
            image = Image.open('pix4.jpg')
            st.image(image, caption='Zanzibar in Abuja', width = 600)
    
    
            st.write("When do you wish to resume your tour?")
            starting_date = st.date_input("choose date")
            n = st.number_input('How many days will you like to tour with us?', step =1)
            if n>=1:
                st.write('Amount= $ ',  n*500)
        
                status = st.radio("choose payment method: ", ('MasterCard', 'Bank Transfer', 'Paystack', 'Cash'))
                if(status == 'MasterCard'):
                    st.error('unavailable')
                elif(status == 'Bank Transfer'):
                    st.error('unavailable')
                elif(status == 'Paystack'):
                    st.error('unavailable')
                else:
                    st.success('Payment accepted')
                    if st.button('Generate ID'):
                        st.text('CONGRATULATIONS!!! your tour ID is xxx')
       
            else:
                st.error('Kindly choose a figure')
        
    



        
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 60px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(20),
        color="red",
        text_align="left",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(1)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "Contact a Tour Guide: 0814651xxxxx, adamu.tour@deen360tours.com ",
    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()




    
    
                      

    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
