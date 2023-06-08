import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="select the number of forecasted days")

option = st.selectbox("Select data to view",
                      ("temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-20"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d,t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature(c)"})
st.plotly_chart(figure)