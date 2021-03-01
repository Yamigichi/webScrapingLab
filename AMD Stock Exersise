#Now using the Ticker module create an object for AMD (Advanced Micro Devices) with the ticker symbol is AMD called; name the object amd.
amd = yf.Ticker("AMD")

#Question 1 Use the key 'country' to find the country the stock belongs to, remember it as it will be a quiz question.
amd_info=amd.info
amd_info
amd_info['country']

#Question 2 Use the key 'sector' to find the sector the stock belongs to, remember it as it will be a quiz question.
amd_info['sector']

#Question 3 Find the max of the Volume column of AMD using the history function, set the period to max.
amd_share_price_data= amd.history(period="max")
amd_share_price_data.max()
