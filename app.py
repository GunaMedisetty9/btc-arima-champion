
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Bitcoin Forecaster", page_icon="₿", layout="wide")

st.title("₿ Bitcoin ARIMA Champion Forecaster")
st.markdown("**MAE: $14,944 | Production Ready Model**")

# Sidebar metrics
st.sidebar.header("🏆 Tournament Results")
st.sidebar.metric("🥇 Champion", "ARIMA(1,1,1)")
st.sidebar.metric("📊 MAE", "$14,944")
st.sidebar.metric("🔮 Horizon", "147 days")

# Load data
@st.cache_data
def load_forecast():
    return pd.read_csv("01_Bitcoin_ARIMA_Champion_Forecasts.csv")

df_forecast = load_forecast()

# Main chart
st.subheader("📈 ARIMA Champion vs Actual BTC Price")
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_forecast['Forecast_Date'], y=df_forecast['Actual_BTC_Price'],
                         mode='lines+markers', name='Actual BTC', 
                         line=dict(color='black', width=3)))
fig.add_trace(go.Scatter(x=df_forecast['Forecast_Date'], y=df_forecast['ARIMA_CHAMPION'],
                         mode='lines', name='ARIMA Champion', 
                         line=dict(color='limegreen', width=3)))
fig.update_layout(height=500, template='plotly_white', title="Champion Performance")
st.plotly_chart(fig, use_container_width=True)

# Tournament table
st.subheader("🥇 Model Tournament Leaderboard")
st.dataframe(pd.read_csv("02_Model_Tournament_Leaderboard.csv"))

# Download
st.subheader("💾 Download Forecasts")
csv = df_forecast.to_csv(index=False).encode('utf-8')
st.download_button("📥 Full 147-Day Forecasts", csv, "bitcoin_forecasts.csv", "text/csv")

st.markdown("---")
st.caption("Built by NIT Trichy | Production ML Pipeline")
