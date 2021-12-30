import sys
from collections import defaultdict

import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
from test_plotSNPs import parse_chromosomes


def bar_plot(ax, data, group_stretch=0.8, bar_stretch=0.95,
             legend=True, x_labels=True, label_fontsize=8,
             colors=None, barlabel_offset=1,
             bar_labeler=lambda k, i: ""):
    """
    Draws a bar plot with multiple bars per data point.
    :param dict data: The data we want to plot, where keys are the names of each
      bar group, and items is a list of bar values for the corresponding group.
    :param float group_stretch: 1 means groups occupy the most (largest groups
      touch side to side if they have equal number of bars).
    :param float bar_stretch: If 1, bars within a group will touch side to side.
    :param bool x_labels: If true, x-axis will contain labels with the group
      names given at data, centered at the bar group.
    :param int label_fontsize: Font size for the label on top of each bar.
    :param float barlabel_offset: Distance, in y-values, between the top of the
      bar and its label.
    :param function bar_labeler: If not None, must be a function with signature
      ``f(group_name, i, scalar)->str``, where each scalar is the entry found at
      data[group_name][i]. When given, returns a label to put on the top of each
      bar. Otherwise no labels on top of bars.
    """
    sorted_data = list(sorted(data.items(), key=lambda elt: elt[0]))
    sorted_k, sorted_v = zip(*sorted_data)
    max_n_bars = max(len(v) for v in data.values())
    group_centers = np.cumsum([max_n_bars
                               for _ in sorted_data]) - (max_n_bars / 2)
    bar_offset = (1 - bar_stretch) / 2
    bars = defaultdict(list)
    #
    if colors is None:
        colors = {g_name: [f"C{i}" for _ in values]
                  for i, (g_name, values) in enumerate(data.items())}
    #
    for g_i, ((g_name, vals), g_center) in enumerate(zip(sorted_data,
                                                         group_centers)):
        n_bars = len(vals)
        group_beg = g_center - (n_bars / 2) + (bar_stretch / 2)
        for val_i, val in enumerate(vals):
            bar = ax.bar(group_beg + val_i + bar_offset,
                         height=val, width=bar_stretch,
                         color=colors[g_name][val_i])[0]
            bars[g_name].append(bar)
            if bar_labeler is not None:
                x_pos = bar.get_x() + (bar.get_width() / 2.0)
                y_pos = val + barlabel_offset
                barlbl = bar_labeler(g_name, val_i)
                ax.text(x_pos, y_pos, barlbl, ha="center", va="bottom",
                        fontsize=label_fontsize)
    if legend:
        ax.legend([bars[k][0] for k in sorted_k], sorted_k)
    #
    ax.set_xticks(group_centers)
    if x_labels:
        ax.set_xticklabels(sorted_k)
    else:
        ax.set_xticklabels()
    return bars, group_centers


if __name__ == '__main__':
    # filename = sys.argv[-2]
    # output_file = sys.argv[-1]
    #
    # print("input ", filename)
    # print("output ", output_file)

    fig, ax = plt.subplots()
    #data = {'NC_048323.1': [23, 12, 13, 11, 15, 6, 15, 21, 27, 27, 25, 35, 12, 40, 1, 5, 9, 4, 22, 39, 53, 45, 50, 49, 67, 61, 36, 43, 38, 33, 31, 46, 31, 35, 29, 17, 29, 29, 22, 42, 18, 19, 36, 49, 43, 27, 34, 41, 35, 51, 34, 47, 22, 11, 74, 31, 14, 5, 15, 10, 2],'NC_048324.1': [2, 15, 12, 23, 37, 28, 22, 29, 2, 8, 15, 4, 10, 21, 33, 2, 24, 25, 19, 3, 7, 31, 51, 21, 61, 70, 29, 4, 17, 63, 30, 2, 4, 26, 4, 6, 20, 36, 40, 15, 23, 94, 66, 38, 44, 69, 53, 22, 50, 66, 100, 94, 44, 58, 55, 57, 52, 54, 74, 37, 6, 17, 39, 48, 55, 59, 53, 61, 79, 72, 63, 55, 41, 65, 10]}

    data = parse_chromosomes('keys_vals_5_5.txt')
    bar_plot(ax, data, group_stretch=0.8, bar_stretch=0.95, legend=True, label_fontsize=8, barlabel_offset=0.05,
             bar_labeler=lambda k, i: "")

    fig.show()
