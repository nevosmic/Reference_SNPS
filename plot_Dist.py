import sys
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn
matplotlib.use('Agg')


def collect_vector_from_file(filename):
    _file = open(filename, 'r')
    distances_vector=[]
    line = _file.readline()
    line = line[1:-1]  # remove chars [ ]
    line = line.split(",")
    for x in line:
        #if x.__contains__(' '):
        #    print(x)
        #else:
            distances_vector.append(int(x))
    return distances_vector


def create_DF(distances_vector):
    # Calling DataFrame constructor on list
    df = pd.DataFrame(distances_vector, columns=['male-ploidy8'])
    print(df)
    return df


def plot(df, output_png, title):
    plot = seaborn.histplot(data=df, bins=100,binwidth=3,alpha=1)
    plt.ylim(0, 6000)
    plt.xlim(0, 6000)
    plt.xlabel('Distance values')
    plt.title(title)
    fig = plot.get_figure()
    fig.savefig(output_png)

    print("Done :)")


def Average(lst):
    return sum(lst) / len(lst)


if __name__ == '__main__':

    filename = 'dist_vector.txt'
    output_file = 'dist.png'
    #filename = sys.argv[-2]
    #output_file = sys.argv[-1]

    print("input ", filename)
    print("output ", output_file)

    distances_vector = collect_vector_from_file(filename)
    df = create_DF(distances_vector)
    print(df)
    av = Average(distances_vector)
    title = r'Distance between snps : average: {}'.format(av)
    print("Average: ", av)

    plot(df, output_file, title)
    print('Done')
