# Crypto Next-day Price Predictor

The Crypto Next-day Price Predictor app is a Streamlit-based web interface that lets users view crypto coins historical pricing data for the last 3 years and compare different machine learning models to predict **tomorrow's** future '**Closing**' price for the top 10 cryptocurrency coins by market cap. 

The app is powered by Python and uses popular libraries such as `pandas`, `streamlit`, `yfinance` for historical data gathering, and `plotly` to handle data and provide rich visualizations.




## Libraries

```@python
pandas   : 1.3.5
streamlit: 1.18.1
plotly   : 5.11.0
yfinance : 0.2.3
```


## Implementation

To run the Crypto Pricing Predictor, you will need to have Python 3 installed on your machine, along with the required dependencies listed in the `requirements.txt` file. You can install the dependencies by running the following command:



Create new environment:
- `conda create -n [new_name] python=3.9`
- `conda activate [new_name]`
- `pip install pandas streamlit plotly yfinance scikit-learn`

**OR**

- `pip install -r requirements.txt`
- `git clone` the repo to your local drive
- `cd` into the folder in Terminal
- Run `streamlit run home.py`
- If no other streamlit app is running, you should see the app running on `http://localhost:8501/`













<sub>**Note:** This is a project app using an opensource data provider `yfinance` and is not intended to be used live and to make live predictions</sub>