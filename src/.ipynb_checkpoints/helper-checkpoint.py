def stationarity_test(filepath):
    stationary = \
         {
             'before': 
             {
              'ADF':     adfuller(before['Perc_Diff'])[0], 
              'p-value':  adfuller(before['Perc_Diff'])[1], 
              '1%':       adfuller(before['Perc_Diff'])[4]['1%'],
              '5%':       adfuller(before['Perc_Diff'])[4]['5%'],
              '10%':      adfuller(before['Perc_Diff'])[4]['10%'],
             },
              'after': 
             {
              'ADF':     adfuller(after['Perc_Diff'])[0], 
              'p-value':  adfuller(after['Perc_Diff'])[1], 
              '1%':       adfuller(after['Perc_Diff'])[4]['1%'],
              '5%':       adfuller(after['Perc_Diff'])[4]['5%'],
              '10%':      adfuller(after['Perc_Diff'])[4]['10%'],
              }
        }
    
    return stationary