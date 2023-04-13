import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
from .utils import nullity_sort


def matrix(df, sort=None, figsize=(25, 10), fontsize=12, 
           color=(60, 60, 60), show_label=True, label_rotation=45):
    
    df = nullity_sort(df, sort=sort)
    height, width = df.shape

    z = df.notnull().values
    x = np.zeros((height, width, 3), dtype=np.uint32)
    x[z < 0.5] = (255, 255, 255)
    x[z > 0.5] = color

    plt.figure(figsize=figsize)
    ax = plt.subplot()
    ax.imshow(x, interpolation='none', aspect='auto')
    ax.xaxis.tick_top()
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.set_yticks([])
    ax.spines[['top', 'right', 'bottom', 'left']].set_visible(False)
    
    if show_label:
        ax.set_xticks(list(range(0, width)))
        ax.set_xticklabels(list(df.columns), rotation=label_rotation, 
                           ha='left', fontsize=fontsize)
    else:
        ax.set_xticks([])

    # Add a vertical line across the grid
    for x in [_ + 0.5 for _ in range(0, width-1)]:
        ax.axvline(x, color='white')

    return ax


def bar(df, sort=None, figsize=(25, 10), fontsize=12, 
        color='C0', show_label=True, label_rotation=45):

    df = nullity_sort(df, sort=sort)
        
    ax1 = plt.gca()

    plot_args = {'figsize': figsize, 'fontsize': fontsize, 'color': color, 'ax': ax1}
    valid_counts = len(df) - df.isnull().sum()
    (valid_counts / len(df)).plot.bar(**plot_args)

    axes = [ax1]
    ax1.set_xticklabels(ax1.get_xticklabels(), 
                        rotation=label_rotation, ha='right', fontsize=fontsize)
    ax1.set_ylim([0, 1])
    ax1.yaxis.set_major_formatter(ticker.PercentFormatter(1.0)) # Make percent format
    
    # Display total of valid data above the plot.
    ax2 = ax1.twiny()
    ax2.set_xticks(ax1.get_xticks())
    ax2.set_xlim(ax1.get_xlim())
    ax2.set_xticklabels(valid_counts.values, 
                        rotation=label_rotation, ha='left', fontsize=fontsize)
    axes.append(ax2)

    if not show_label:
        ax1.set_xticks([])
        ax1.set_yticks([])
        ax2.set_xticks([])

    for ax in axes:
        ax.spines[['top', 'right', 'bottom', 'left']].set_visible(False)
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')

    return ax1
