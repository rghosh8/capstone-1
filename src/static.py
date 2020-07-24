font = {
        'family':'serif',
        'color': 'black',
        'weight':'normal',
        'size':24,
        }

vline_prop = {
        'color':'#C0392B',
        'linestyle':'dashed',
        'linewidth':4,
}

test_data_prop = {
        'plot_title': 'Daily Closing Stock Price ($) for Monitoring Companies',
}

two_sided_confidence_level = {
        '99%': 2.576,
        '98%': 2.326,
        '95%': 1.96,
        '90%': 1.645,
}

filepaths = ['../data/SPLK.csv', '../data/DDOG.csv', '../data/DT.csv', '../data/NEWR.csv']
APM_Companies = ['Splunk', 'Datadog', 'Dynatrace', 'New Relic']
colors = ['#E67E22', '#A569BD', '#58D68D', '#D4AC0D']
refer = dict(zip(filepaths, APM_Companies))

before_prop = {'color': 'b', 'label': 'before/on March 16, 2020'}
after_prop = {'color': 'r', 'label': 'after March 16, 2020'}
