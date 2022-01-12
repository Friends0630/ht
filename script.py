import streamlit as st
money=5000
def main():
  st.title('丁半')
  th= st.radio('偶数だと思うなら丁、奇数だと思うなら半を入力',['丁', '半'])
if __name__ == '__main__':
    main()
