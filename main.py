import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

# text = st.text_input('あなたの趣味をおしえてください。')
# condition = st.slider('あなたの今の調子は', 0, 100, 50)
# 'あなたの趣味は：', text
# 'コンディション：', condition

# option = st.selectbox(
#     'あなたが好きな数字をおしえてください。',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、', option, 'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('image_68.jpg')
#     st.image(img, caption='Sample', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/(50, 50) + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)
# st.map(df)

# st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)
# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
