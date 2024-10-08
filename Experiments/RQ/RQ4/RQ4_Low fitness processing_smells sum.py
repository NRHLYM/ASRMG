import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker


if __name__ == "__main__":
    categories = ['BSA', 'M4C', 'PC', 'SCS', 'TT']

    无低适应度处理 = [1, 2, 0.01, 4, 1]
    有低适应度处理 = [0.01, 1, 0.01, 1, 0.01]

    fontsize = 20
    bar_width = 0.2

    x = np.arange(len(categories))

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22',
              '#17becf']

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.15)
    plt.xticks(x, categories, fontsize=fontsize)
    plt.rcParams['font.sans-serif'] = ['simsun']
    plt.bar(x - 0.5 * bar_width, 无低适应度处理, width=bar_width, label='无')
    plt.bar(x + 0.5 * bar_width, 有低适应度处理, width=bar_width, label='有')
    ax.set_xlabel('微服务系统', fontsize=18)
    ax.set_ylabel('值', fontsize=fontsize)

    ax.tick_params(axis='both', labelsize=fontsize)

    ax.legend(loc="upper left", fontsize=fontsize)

    plt.savefig('RQ4_有无低适应度处理_异味数量.png', bbox_inches='tight')
    plt.savefig('Fig20_c.eps', bbox_inches='tight')

    plt.show()
