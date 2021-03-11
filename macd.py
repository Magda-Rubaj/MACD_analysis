import numpy as np
import pandas as pd
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

def plot_data(start_day, end_day, data):
    MACD = calculate_MACD(data)
    SIGNAL = calculate_signal(MACD)
    plt.figure(figsize=(20, 10))
    plt.plot(data)
    plt.plot(MACD[8:len(MACD)])
    plt.plot(SIGNAL)
    plt.xlim(start_day, end_day)
    plt.show()