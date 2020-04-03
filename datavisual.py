import random
import numpy as np
import matplotlib.pyplot as plt


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return len(lst3)


def conta1(A, n):
    count = 0
    for i in range(n):
        for j in range(n):
            if A[i][j] == 1:
                count += 1
    return count


if __name__ == '__main__':
''' 
    x1 = [ 100,73.9, 54.1, 43.4, 38.7, 30.7, 25.1, 24.1, 22.6, 20.9, 19.9]
    x2 = [ 100, 10.06, 6.21, 4.68, 3.56, 2.89, 2.69, 2.42,  2.24, 2.12, 1.99]
    x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    plt.plot(x,x1, label="Mobile",marker = "o", color = 'red')

    plt.plot(x,x2,label="Desktop", marker = "o", color = 'blue')
    plt.legend(loc='upper right')
    plt.ylabel("Coverage (%)")
    plt.xlabel("Arrest probability")
    for i, j in zip(x, x1):
        corr=0.5
        #corr = -0.05  # adds a little correction to put annotation in marker's centrum
        if i!=0:
            plt.annotate(str(j), xy=(i -0.0125 , j + corr))
    for i, j in zip(x, x2):
        corr=2
        #corr = -0.05  # adds a little correction to put annotation in marker's centrum
        plt.annotate(str(j), xy=(i -0.00625 , j + corr))
    plt.show()

    mob_cache=[ 7.39,5.41,4.34, 3.87,3.07,2.51,2.41,2.38, 2.26,2.09, 1.99]
    desk_cache=[10.06,6.21,4.68, 3.56,2.89,2.69,2.42,2.46, 2.24,2.12, 1.99]
    prob=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    res=[642104.0, 677880.2,713470.4, 749663.2, 785357.3,821089.5, 857113.6, 892423.2, 928506.9, 964130.9, 1000000]
    #plt.plot(res, 0.1)
    #plt.show()
    men_means, men_std = (20, 35, 30, 35, 27), (2, 3, 4, 1, 2)
    women_means, women_std = (25, 32, 34, 20, 25), (3, 5, 2, 3, 3)

    ind = np.arange(len(res))  # the x locations for the groups
    width = 0.5  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width / 2+0.25, res, width, yerr=prob,
                    color='darkturquoise', label='Coverage')
    #rects2 = ax.bar(ind + width / 2, women_means, width, yerr=women_std,
                    #color='IndianRed', label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Coverage')
    ax.set_title('Density by probability of link')
    ax.set_xticks(ind)
    ax.set_xticklabels(("0",'0.1', '0.2', '0.3', '0.4', '0.5', '0.6', "0.7", "0.8", "0.9", "1"))
    ax.legend()


    def autolabel(rects, xpos='left'):
        """
        Attach a text label above each bar in *rects*, displaying its height.

        *xpos* indicates which side to place the text w.r.t. the center of
        the bar. It can be one of the following {'center', 'right', 'left'}.
        """

        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
                    '{}'.format(height), ha=ha[xpos], va='bottom')


    autolabel(rects1, "left")
    #autolabel(rects2, "right")

    plt.show()
'''
