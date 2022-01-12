import streamlit as st
money=5000
def main():
  st.title('丁半')
  th= st.radio('偶数だと思うなら丁、奇数だと思うなら半を入力',['丁', '半'])
    money0 = st.slider(label='賭け金を入力(現在の所持金:'+str(money)+"円)",
                    min_value=0,
                    max_value=money,
                    value=0,
                    )
if __name__ == '__main__':
    main()
