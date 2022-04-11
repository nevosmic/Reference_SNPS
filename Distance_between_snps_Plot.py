import sys
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn
matplotlib.use('Agg')


class SnpsForPlot:

    def __init__(self):
        self.chromosomes_dict = {}
        self.distances_vector = []

    def process_lines(self, row_items_1, row_items_2):
        chrom1 = row_items_1[0]
        pos_1 = int(row_items_1[1])
        chrom2 = row_items_2[0]
        pos_2 = int(row_items_2[1])
        if chrom1 == chrom2:
            dist = pos_2 - pos_1
            if chrom1 in self.chromosomes_dict:
                self.chromosomes_dict[chrom1].append(dist)
            else:
                self.chromosomes_dict[chrom1] = [dist]

    def count_dist_between_snps(self, vcf_file):
        with open(vcf_file) as vcf_object:
            line_1 = vcf_object.readline()
            while True:
                line_2 = vcf_object.readline()
                if not line_2:
                    break
                row_items_1 = line_1.split()
                row_items_2 = line_2.split()
                if row_items_1[0].startswith('N') and row_items_2[0].startswith('N'):
                    '''Fill chromosomes dict'''
                    self.process_lines(row_items_1, row_items_2)
                line_1 = line_2

    def collect_distances(self):

        for key in self.chromosomes_dict.keys():
            for dist in self.chromosomes_dict[key]:
                self.distances_vector.append(dist)
        print(self.distances_vector)

    def create_DF(self, columns_name):
        # Calling DataFrame constructor on list
        df = pd.DataFrame(self.distances_vector, columns=[columns_name])
        return df

    def plot(self, df, output_png, title):
        plot = seaborn.histplot(data=df, bins=100, binwidth=3, alpha=1)
        plt.ylim(0, 6000)
        plt.xlim(0, 6000)
        plt.xlabel('Distance values')
        plt.title(title)
        fig = plot.get_figure()
        fig.savefig(output_png)

        print("Done :)")

    def Average(self, ):
        return sum(self.distances_vector) / len(self.distances_vector)


if __name__ == '__main__':
    vcf_file = 'Male_ref_snps.vcf.txt'
    output_png = 'Dist_plot.png'
   # vcf_file = sys.argv[-2]
   # output_png = sys.argv[-1]

    print("input ", vcf_file)
    print("output ", output_png)

    snps_for_plot = SnpsForPlot()
    snps_for_plot.count_dist_between_snps(vcf_file)
    snps_for_plot.collect_distances()
    snps_for_plot.distances_vector
    df = snps_for_plot.create_DF('Male reference - ploidy 2')
    av = snps_for_plot.Average()
    title = r'Distance between snps : average: {}'.format(av)
    snps_for_plot.plot(df, output_png, title)
