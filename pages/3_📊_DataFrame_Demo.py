import pandas as pd
import streamlit as st

st.title("DataFrame Demo")

sample_df = pd.DataFrame(
    {
        "City": ["New York", "Los Angeles", "Chicago", "Boston"],
        "Population": [8.4, 3.9, 2.7, 0.7],
        "Avg Temp (C)": [12, 19, 9, 10],
    }
)

st.write("Here is a sample dataframe rendered in the app.")
st.dataframe(sample_df)

st.bar_chart(sample_df.set_index("City")["Population"])
