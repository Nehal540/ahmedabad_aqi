import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Designstorm 10X", layout="wide")
st.title("🚀 Designstorm 10X Status")

# Create connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Read the data (using your specific link)
url = "https://docs.google.com/spreadsheets/d/1FLvc6FoVIQlO5-7rY88NWhmuaaU4jK-Bw8L6TzeW-nk/edit#gid=2091390401"
df = conn.read(spreadsheet=url, ttl=0)

# Simple Sidebar Filter
member = st.sidebar.selectbox("Select Team Member", df['Team Member'].unique())

# Display Data
st.subheader(f"Current Progress for {member}")
st.dataframe(df[df['Team Member'] == member])
