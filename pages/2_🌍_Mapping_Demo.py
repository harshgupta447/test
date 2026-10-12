import pandas as pd
import streamlit as st

st.title("Mapping Demo")

map_data = pd.DataFrame(
    {
        "lat": [40.7128, 40.7306, 40.7411],
        "lon": [-74.0060, -73.9352, -73.9981],
    }
)

st.write("This map shows a few New York City locations.")
st.map(map_data)
