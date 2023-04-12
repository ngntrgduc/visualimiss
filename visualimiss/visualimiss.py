import numpy as np
import matplotlib.pyplot as plt
from .utils import nullity_sort

def matrix(df, n=0, sort=None, sort_axis='rows', figsize=(25, 10), fontsize=12, 
           color=(60, 60, 60), label_rotation=45, show_col_names=True):
    
    df = nullity_sort(df, sort=sort, axis=sort_axis)
    height, width = df.shape

    # z is the color-mask array, x is a (height x width x 3) matrix.
    # Apply the z color-mask to set the RGB of each pixel.
    z = df.notnull().values
    x = np.zeros((height, width, 3), dtype=np.uint32)
    x[z < 0.5] = (255, 255, 255)
    x[z > 0.5] = color

    plt.figure(figsize=figsize)
    ax = plt.subplot()
    ax.imshow(x, interpolation='none', aspect='auto')

    # Remove default visual elements
    ax.grid(visible=False)
    ax.xaxis.tick_top()
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.set_yticks([])
    ax.spines[['top', 'right', 'bottom', 'left']].set_visible(False)
    
    # Set up and rotate the column ticks.
    if show_col_names:
        ax.set_xticks(list(range(0, width)))
        ax.set_xticklabels(list(df.columns), rotation=label_rotation, 
                           ha='left', fontsize=fontsize)
    else:
        ax.set_xticks([])

    

    # Add a vertical line across the grid
    for x in [_ + 0.5 for _ in range(0, width-1)]:
        ax.axvline(x, color='white')

    return ax
