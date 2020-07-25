start_date='2019-07-23'
moveback_date='2019-10-15'
reference_date='2020-03-16' 
current_date='2020-07-20'

colors = ['#E67E22', '#A569BD', '#58D68D', '#D4AC0D']
dy_param_list = ['2020-03-16', '2020-04-16', '2020-05-15', '2020-06-16', '2020-07-16'] 

bayes_intervals = list(zip(dy_param_list[:-1], dy_param_list[1:], colors))

test_dim = 'Pct_Diff'