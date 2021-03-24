import numpy as np
import pandas as pd
import math 
import matplotlib.pyplot as plt


def calculate_EMA(N, data, current_day):
    alpha = 2/(N+1)
    p = data[current_day:current_day+(N-1)]
    sum_top = 0
    sum_bottom = 0
    for i in range(len(p)):
        sum_top += p[i] * ((1-alpha) ** i)
        sum_bottom += (1-alpha) ** i
    EMA = sum_top / sum_bottom  
    return EMA

def calculate_MACD_element(data, current_day):
    EMA12 = calculate_EMA(12, data, current_day)
    EMA26 = calculate_EMA(26, data, current_day)
    macd = EMA12 - EMA26
    return macd

def calculate_MACD(data):
    MACD = []
    for i in range(len(data)-26, -1, -1):
        x = calculate_MACD_element(data, i)
        MACD.append(x)
    return MACD

def calculate_signal_element(data, current_day):
    ema9 = calculate_EMA(9, data, current_day)
    return ema9

def calculate_signal(data):
    SIGNAL = []
    for i in range(len(data)-8):
        x = calculate_signal_element(data, i)
        SIGNAL.append(x)
    return SIGNAL

def plot_data(start_day, end_day, MACD, SIGNAL, data):
    x = np.arange(0,len(data))
    fig, (ax, ax2) = plt.subplots(2, figsize=(20,10), gridspec_kw={'height_ratios': [3, 1]})
    ax.set_ylabel('Price')
    ax2.set_ylabel('Indicator')

    period = math.floor((end_day - start_day)/10)

    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    
    for idx, val in data.iterrows():
        ax.plot([x[idx], x[idx]], [val['Min.'], val['Max.']], color='red')

    ax.xaxis.grid(color='black', linestyle='dashed', which='both', alpha=0.1)
    ax2.plot(x, MACD, color='orange', label='macd')
    ax2.plot(x, SIGNAL, color='navy', label='signal')
    ax2.legend()
    ax2.yaxis.tick_right()
    plt.xlim(start_day, end_day)
    plt.subplots_adjust(wspace=0, hspace=0)

    ax2.set_xticks(x[::period])
    ax2.set_xticklabels(data.Data.dt.date[::period], rotation=90)
    ax.set_xticks([])
    ax.set_xlim(start_day, end_day)
    ax.set_title('MACD analysis\n', loc='left', fontsize=20)
    ax2.set_xlim(start_day, end_day)
    plt.show()
