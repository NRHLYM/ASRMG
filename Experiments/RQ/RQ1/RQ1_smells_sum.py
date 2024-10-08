import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":

    categories = ['BSA', 'M4C', 'PC', 'SCS', 'TT']

    前异味数量 = [8, 86, 4, 38, 26]
    后异味数量 = [0, 1, 0, 1, 0]

    fontsize = 20

    bar_width = 0.2


    x = np.arange(len(categories))

    colors = ['#e5b5a4', '#559da5', '#acc38c']

    plt.figure(dpi=600)

    plt.subplots_adjust(bottom=0.15)

    plt.rcParams['font.sans-serif'] = ['simsun']
    plt.bar(x - 0.5 * bar_width, 前异味数量, width=bar_width, label='重构前')
    plt.bar(x + 0.5 * bar_width, 后异味数量, width=bar_width, label='重构后')

    # 添加标签和标题
    plt.xlabel('微服务系统', fontsize=fontsize)
    plt.ylabel('异味数量', fontsize=fontsize)

    plt.xticks(x, categories, fontsize=fontsize)
    plt.yticks(fontsize=fontsize)

    plt.legend(loc="upper right", fontsize=fontsize)

    plt.savefig('Fig12_b.eps', bbox_inches='tight')
    plt.savefig('RQ1_重构前后异味数量.png', bbox_inches='tight')

    plt.show()
