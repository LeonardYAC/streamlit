import streamlit as st
import pandas as pd

data = {
  'Series_1':[1,4,16,64,256,240,200],
  'Series_2':[10,30,40,100,250,700,800]
}

df = pd.DataFrame(data)

st.title('The ultimate graphing app')
st.subheader('Automate with streamlit')
st.write('''graphing stuff. 
Enjoy it.
''')

st.write(df)
st.line_chart(df)
st.area_chart(df)