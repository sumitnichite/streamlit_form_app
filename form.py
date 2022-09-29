import streamlit as st


st.title('Form')

# with st.form('form1', clear_on_submit = True):

name = st.text_input('enter your name')


email = st.text_input('enter your email ')

about_me = st.text_area('About me')

select_gender = st.radio('Select Gender:' , ('Male','Female') )

uploaded_file = st.file_uploader("Choose a file")
submit = st.button('Submit')


if submit and name and email and about_me and select_gender and uploaded_file :
    st.write('name:',name)
    st.write('email: ',email)
    st.write('About me:', about_me)
    st.write('Select Gender:', select_gender)

    st.write('choose a file:',uploaded_file )





