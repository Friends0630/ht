import streamlit as st
money=5000
while(True):
  e=1
  st.title('丁半')
  th= st.radio('偶数だと思うなら丁、奇数だと思うなら半を入力',['丁', '半'])
  while e==0:
    st.number_input(label='賭け金を入力(現在の所持金:'+str(money)+"円)",value=0)
    if money < money0:
      st.error('所持金を超える賭け金は賭けられません')
    else:
      e=0
