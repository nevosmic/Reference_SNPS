import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def collect_AF_from_file(filename):
    AF_file = open(filename, 'r')
    AF_vector=[]
    line = AF_file.readline()
    line = line[1:-1]  # remove chars [ ]
    line = line.split(",")
    for x in line:
        AF_vector.append(float(x))
    return AF_vector


def plot_AF(AF_vector, output_png, title):
    num_bins = 5
    n, bins, patches = plt.hist(AF_vector, num_bins, facecolor='blue', alpha=0.5)
    plt.xlabel('AF values')
    plt.title(title)
    plt.savefig(output_png)
    print('DONE')


if __name__ == '__main__':
    filename = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", filename)
    print("output ", output_file)

    title = r'AF plot of ploidy 8'

    AF_vector = collect_AF_from_file(filename)
    plot_AF(AF_vector, output_file, title)
