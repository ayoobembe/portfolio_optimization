# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:20:14 2015

@author: danielayomikun
"""

import os
import pandas as pd
import numpy as np
from pandas import DataFrame as df
from pandas import Series
import time
import matplotlib.pyplot as plt


aapl_df = pd.read_csv('../Desktop/CQF/2_Risk_and_Return/Project/aapl.csv')
txi_df = pd.read_csv('../Desktop/CQF/2_Risk_and_Return/Project/txi.csv')


aapl_closing_full = Series(aapl_df['Close'])
aapl_closing = aapl_closing_full[2000:]
aapl_closing.index = np.arange(6622)

txi_closing_full = Series(txi_df['Close'])
txi_closing = txi_closing_full[1500:]
txi_closing.index = aapl_closing.index


txi_closing.plot()
aapl_closing.plot()
plt.show()

plt.scatter(txi_closing,aapl_closing )
plt.show()

#Calculating returns
aapl_returns = aapl_closing.pct_change()
txi_returns = txi_closing.pct_change()

txi_returns.plot()
aapl_returns.plot()
plt.show()

plt.scatter(txi_returns,aapl_returns )
plt.show()