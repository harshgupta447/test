import numpy as np
import pandas as pd
import streamlit as st

st.title("Plotting Demo")

x = np.arange(0, 10)
y = np.random.default_rng(42).normal(0, 1, size=10).cumsum()

df = pd.DataFrame({"x": x, "y": y})

st.write("This is a simple plotting page built with Streamlit.")
st.line_chart(df.set_index("x"))
