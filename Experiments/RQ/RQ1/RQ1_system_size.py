import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":


    categories = ['BSA', 'M4C', 'PC', 'SCS', 'TT']
    系统前大小 = [5, 11, 4, 11, 37]
    系统后大小 = [8, 22, 4, 15, 36]

    fontsize = 20

    bar_width = 0.2


    x = np.arange(len(categories))


    colors = ['#e5b5a4', '#559da5', '#acc38c']

    plt.figure(dpi=600)


    plt.subplots_adjust(bottom=0.15)

    plt.rcParams['font.sans-serif'] = ['simsun']

    plt.bar(x - 0.5 * bar_width, 系统前大小, width=bar_width, label='重构前')
    plt.bar(x + 0.5 * bar_width, 系统后大小, width=bar_width, label='重构后')

    plt.xlabel('微服务系统', fontsize=fontsize)
    plt.ylabel('大小', fontsize=fontsize)



    plt.xticks(x, categories, fontsize=fontsize)
    plt.yticks(fontsize=fontsize)

    plt.legend(loc="upper left", fontsize=fontsize)

    plt.savefig('Fig12_a.eps', bbox_inches='tight')
    plt.savefig('RQ1_重构前后规模.png', bbox_inches='tight')

    plt.show()
