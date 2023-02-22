# import libraries
import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import streamlit as st # deployment
import cufflinks as cf # import cufflinks for bollinger bands
import plotly.graph_objects as go # Candlestick chart
from autots import AutoTS # Time series analysis

# Import warnings + watermark
from watermark import watermark
from warnings import filterwarnings
filterwarnings("ignore")
print(watermark())
print(watermark(iversions=True, globals_=globals()))


#------------------------------------------------------------------#

# Load and Use local style.css file
def local_css(file_name):
    """
    Use a local style.css file.
    """
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# load css file
local_css("./style/style.css")


#------------------------------------------------------------------#

# Read ticker symbols from a CSV file
try:
    tickers = pd.read_csv("./Resources/tickers.csv")
except:
    logging.error('Cannot find the CSV file')

# Show tickers list
st.write(f"Below is the list of the coins available for analysis")
st.write(tickers)
#------------------------------------------------------------------#

# declare variable for current date/ end date
today = date.today()
end_date = today.strftime("%Y-%m-%d")

# declare variable for start date - past 3 years
d2 = date.today() - timedelta(days=1095)
start_date = d2.strftime("%Y-%m-%d")


# Display a selectbox for the user to choose a ticker
ticker = st.selectbox("Select a ticker from the dropdown menu",tickers)


# download yfinance data
data = yf.download(ticker, 
                      start=start_date, 
                      end=end_date, 
                      progress=False)
data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)


# Display Candlestick chart
data_check_box=st.checkbox(label=f"Display {ticker} raw dataset for the past 3 years")
if data_check_box:

    # Display full dataset
    st.write(data)

    # shape of the data
    st.write(f"Data shape (rows, columns) - ",data.shape)



# Create Candlestick attribute
figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                        open=data["Open"], 
                                        high=data["High"],
                                        low=data["Low"], 
                                        close=data["Close"])])
figure.update_layout(title = f"Candlestick Analysis for {ticker} price",
                     xaxis_rangeslider_visible=False)


# Display Candlestick chart
candlestick_check_box=st.checkbox(label=f"Display {ticker} Candlestick chart")
if candlestick_check_box:
    # Bollinger bands - trendlines plotted between two standard deviations
    st.header(f"{ticker} Candlestick chart")
    st.info("Candlestick shows the market's open, high, low, and close price for the day")
    st.plotly_chart(figure)

# Display Bollinger charts
bollinger_charts_check_box=st.checkbox(label=f"Display {ticker} charts")
if bollinger_charts_check_box:
    # Bollinger bands - trendlines plotted between two standard deviations
    st.header(f"{ticker} Bollinger bands")
    st.info("Bollinger Bands are a technical analysis tool that measures volatility of a financial instrument by plotting three lines: a simple moving average and two standard deviation lines (upper and lower bands). They are used to identify possible overbought or oversold conditions in the market, trend changes and potential buy and sell signals. The upper band is plotted as the moving average plus two standard deviations and lower band is plotted as moving average minus two standard deviations. They should be used in conjunction with other analysis methods for a complete market analysis and not as a standalone method.")
    # Reset index back to original
    data.reset_index(inplace=True)
    # Add description for visualization
    qf=cf.QuantFig(data,title=f'Bollinger Quant Figure for {ticker}',legend='top',name='GS')
    qf.add_bollinger_bands()
    fig = qf.iplot(asFigure=True)
    st.plotly_chart(fig)
    
    
# Display data for prediction "Close"
prediction_check_box=st.checkbox(label=f"Display data for prediction")
if prediction_check_box:
    # Bollinger bands - trendlines plotted between two standard deviations
    st.header(f"{ticker} prediction data")
    
    correlation=data.corr()
    st.write(correlation["Close"].sort_values(ascending=False))
    
    # Using AutoTS Time Series analysis, predict price for the next 30 days
    # model = AutoTS(forecast_length=10, frequency='infer', ensemble='simple')
    # model = model.fit(data, date_col='Date', value_col='Close', id_col=None)
    # prediction = model.predict()
    # forecast = prediction.forecast
    # st.button(st.write(forecast))
    
             


