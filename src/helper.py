import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
from matplotlib import rcParams
plt.style.use('ggplot')
import pandas as pd
from data_frame import *
from static import *
import numpy as np
import calmap
from scipy import stats
from parameters import *

def stationarity_test(filepath:str, col:str, reference_date, current_date, moveback_date):
    data = data_frame(filepath, reference_date, current_date, moveback_date).before_after
    before, after = data.before, data.after
    result_before, result_after=adfuller(before[col]), adfuller(after[col])
    stationary = \
         {
             'before': 
             {
              'ADF':      result_before[0], 
              'p-value':  result_before[1], 
              '1%':       result_before[4]['1%'],
              '5%':       result_before[4]['5%'],
              '10%':      result_before[4]['10%'],
             },
              'after': 
             {
              'ADF':      result_after[0], 
              'p-value':  result_after[1], 
              '1%':       result_after[4]['1%'],
              '5%':       result_after[4]['5%'],
              '10%':      result_after[4]['10%'],
              }
        }
    
    return stationary

vcdf = np.vectorize(lambda value, array: (array<value).sum()/len(array), excluded = ['array'])


def confidence_interval(mean, se, pct:str):
    lower, upper = mean - two_sided_confidence_level[pct]*se, \
        mean + two_sided_confidence_level[pct]*se

    return {'lower':lower, 'upper':upper}

def plot_hlines(ax, ys: list, x: list, colors: list, linestyles: list):
    for y, color, linestyle in zip(ys, colors, linestyles):
        ax.hlines(y, x[0], x[1], colors=color, linestyles=linestyle)

def plot_vlines(ax, xs: list, y: list, colors: list, linestyles: list, linewidths:list):
    for x, color, linestyle, linewidth in zip(xs, colors, linestyles, linewidths):
        ax.vlines(x, y[0], y[1], colors=color, linestyles=linestyle, linewidths=linewidth)


def plot_with_fill(ax, x, y, label,color):
    lines = ax.plot(x, y, label=label, lw=2, color=color)
    ax.fill_between(x, 0, y, alpha=0.2, color=lines[0].get_c())

def set_axis_sizes(ax, size=18):
    ax.tick_params(axis='x', labelsize=size)
    ax.tick_params(axis='y', labelsize=size)

def put_text(ax, X:list, Y:list, text:list, font_spec:list, align: list):
    for x, y, text_item, font_item, align_item in zip(X, Y, text, font_spec, align):
        ax.text(x, y, text_item, fontdict=font_item, horizontalalignment=align_item)

def create_heatmap(ax, fig, series, year=2020, cmap='YlGn'):
    cax = calmap.yearplot(series, year=2020, ax=ax, cmap=cmap)
    fig.colorbar(cax.get_children()[1], ax=cax, orientation='horizontal')
    set_axis_sizes(ax)


def statistics(filepaths):
    '''
     Compute sample mean, sample std, and std. error for a sample
        input: a filepath (str)
        output: a dictionary of statistics 
    '''
    before_after_dict = dict()
    prop = dict()

    for filepath in filepaths:
        data = data_frame(filepath, reference_date, current_date, moveback_date).before_after
        before, after = data.before, data.after

        before_after_dict[refer[filepath]] = {'before': before['Pct_Diff'],'after': after['Pct_Diff']}
        prop[refer[filepath]] = \
            {
                'before': 
                {
                'mean': round(before['Pct_Diff'].mean(),3), 
                'std':  round(before['Pct_Diff'].std(), 3), 
                'se':   round(before['Pct_Diff'].sem(), 3)
                },
                'after': 
                {
                'mean': round(after['Pct_Diff'].mean(), 3), 
                'std':  round(after['Pct_Diff'].std(), 3), 
                'se':   round(after['Pct_Diff'].sem(), 3)
                }
            }

    return prop

def t_test(filepaths):
    hyp_test = dict()
    for filepath in filepaths:
        data = data_frame(filepath, reference_date, current_date, moveback_date).before_after
        before, after = data.before['Pct_Diff'], data.after['Pct_Diff']
        stat, p_val = stats.ttest_ind(before, after, axis=0, equal_var=False, nan_policy='omit')
        hyp_test[refer[filepath]] = {'t_stat': stat, 'p_val': p_val}

    return hyp_test

def draw_heatmap(filepaths, fig, axs):
    for filepath, ax in zip(filepaths, axs): 
        test = data_frame(filepath, reference_date, current_date, moveback_date).df
        series = test['Close']
        create_heatmap(ax, fig, series)
        ax.set_title(f'{refer[filepath]} Stock Closing Price($) in 2020', fontdict=font, size=30)
        set_axis_sizes(ax, 30)

def bayesian_count(filepaths):
    bayesian_count={}
    for filepath in filepaths:
        data = data_frame(filepath, reference_date, current_date, moveback_date).before_after
        before, after = data.before, data.after
        before_count = before[before[test_dim]>0][test_dim].count() / before[test_dim].count()
        after_count = after[after[test_dim]>0][test_dim].count() / after[test_dim].count()
        bayesian_count[refer[filepath]] = \
                                        {
                                        'before': {'positive': before_count, 'negative': 1-before_count, 'count': before['Pct_Diff'].count()},
                                        'after' : {'positive': after_count, 'negative': 1-after_count, 'count': after['Pct_Diff'].count()}
                                        }

    return bayesian_count