import streamlit as st
money=5000
money=0
st.title('丁半')

  th= st.radio('偶数だと思うなら丁、奇数だと思うなら半を入力',['丁', '半'])
  st.number_input(label='賭け金を入力(現在の所持金:'+str(money)+"円)",value=0)
  if st.button('決定'):
    st.write('決定テスト')
