import streamlit as st

st.title("Fib Series")

a= st.text_input(label="Enter a Number")
button = st.button(label = "Submit")

if(button):
    try:
        if(a.isdigit()):
            a=int(a)
            if(a>0):
                st.write(int(a)," is a Even number")
            else:
                st.write(int(a)," is a Odd number")
        else:
            st.write("Enter Positive Number")
    except:
        st.write("Enter a valid number")