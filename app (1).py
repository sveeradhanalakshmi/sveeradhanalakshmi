import pickle
import streamlit as st
import numpy as np
pickle_in=open('sales mart.pkl','rb')
clf=pickle.load(pickle_in)

def main():
    html_temp='''
    <div style="background-color:yellow;padding:13px">
    <h1 style="color:black;text-align:center;">CORONARY HEART DETECTION PREDICTION</h1>
    </div>'''

    st.markdown(html_temp,unsafe_allow_html=True)
    itwe=st.number_input('Item_Weight')
    itfa=st.number_input('Item_Fat_Content')
    ity=st.number_input('Item_Type')
    sbp=st.number_input('Item_MRP')
    ots=st.number_input('Outlet_Size')
    result=''

    if st.button('PREDICT'):
        result=prediction(itwe,itfa,ity,sbp,ots)
        st.success('YOUR ITEM_OUTLET_SALES{}'.format(result))

def prediction(itwe,itfa,ity,sbp,ots):
  s=clf.predict([[itwe,itfa,ity,sbp,ots]])
  if s==1:
     p='GOOD'
  else:
     p='BAD'
  return p

if __name__=='__main__':
    main()
