import streamlit as st
import pandas as pd
a = pd.read_csv('성_연령별_실업률_20241120175237.csv')
a1=a.T
st.dataframe(a1)
import matplotlib.pyplot as plt
a1=a1.drop(index=['성별','연령계층별'])
a1.columns=['실업률']
import matplotlib.pyplot as plt
fig= plt.fiugre()
plt.plot(a1.index, a1.values)
st.pyplot(plt)
