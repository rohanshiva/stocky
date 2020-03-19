from alpha_vantage.timeseries import TimeSeries

import arrow
import streamlit as st


st.title("Stocky - i don't know why i built this")



def stocky(key, ticker, date, b, today):
    ts = TimeSeries(key)
    stock_data, meta = ts.get_daily(symbol=ticker, outputsize='full')
    previous_price = (stock_data[date])['4. close']
    previous_price = float(previous_price)
    stocks = b/previous_price

    current_price = (stock_data[today])['4. close']
    current_price = float(current_price)
    profit = current_price*stocks
    return profit

key = 'DA7HVED5F6XYRPTV'


ticker = st.text_input('Enter the stock symbol')

date = st.text_input('Enter data in YYYY-MM-DD format')
budget = st.text_input("How much money did you plan on investing? (just enter the number)")
b = float(budget)
today = arrow.now().format('YYYY-MM-DD')
profit = 0.0
if st.button('Stocky'):
    with st.spinner('chill... i am calculating'):
        try:
            profit = stocky(key, ticker, date, b, today)
            if((profit)<b):
                st.write(profit)
                st.balloons()
                st.success("good shit, if you invested you would have lost $" + str(b-profit))
            else:
                st.write(profit)
                st.error("rip, you could have made, $"  + str(profit-b) + ", you lost money retard")
        except:
            st.warning("invalid date or stock symbol!! try again") 

        
