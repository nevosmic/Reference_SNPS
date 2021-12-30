import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn


def collect_vector_from_file(filename):
    _file = open(filename, 'r')
    snps_vector=[]
    line = _file.readline()
    line = line[1:-1]  # remove chars [ ]
    line = line.split(",")
    for x in line:
        snps_vector.append(int(x))
    return snps_vector


def create_DF(distances_vector):
    # Calling DataFrame constructor on list
    df = pd.DataFrame(distances_vector,columns =['male-ploidy4'])
    print(df)
    return df


def plot(df, output_png, title):
    plot = seaborn.histplot(data=df, bins=100,binwidth=3,alpha=1)
    plt.ylim(0, 100)
    # plt.xlim(0, 6000)
    plt.xlabel('Number of snps per 10k')
    plt.title(title)
    fig = plot.get_figure()
    fig.savefig(output_png)

    print("Done :)")


def Average(lst):
    return sum(lst) / len(lst)


if __name__ == '__main__':
    # filename = 'snps_vector.txt'
    # output_file = 'snps_hist.png'
    filename = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", filename)
    print("output ", output_file)

    snps_vector = collect_vector_from_file(filename)
    df = create_DF(snps_vector)
    av = Average(snps_vector)
    title = r'Average snps per segment: {}'.format(av)
    print("Average: ",av)

    plot(df, output_file, title)
