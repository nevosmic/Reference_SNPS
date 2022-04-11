import sys


def process_lines(row_items_1, row_items_2, chromosomes):
    chrom1 = row_items_1[0]
    pos_1 = int(row_items_1[1])
    chrom2 = row_items_2[0]
    pos_2 = int(row_items_2[1])
    if chrom1 == chrom2:
        dist = pos_2 - pos_1
        if chrom1 in chromosomes:
            chromosomes[chrom1].append(dist)
        else:
            chromosomes[chrom1] = [dist]


def count_dist_between_snps(vcf_file):
    chromosomes = {}
    with open(vcf_file) as vcf_object:
        line_1 = vcf_object.readline()
        while True:
            line_2 = vcf_object.readline()
            if not line_2:
                break
            row_items_1 = line_1.split()
            row_items_2 = line_2.split()
            if row_items_1[0].startswith('N') and row_items_2[0].startswith('N'):
                process_lines(row_items_1, row_items_2, chromosomes)
            line_1 = line_2
    print(chromosomes)
    return chromosomes


def collect_distances(chromosomes):
    distances_vector = []
    for key in chromosomes.keys():
        for dist in chromosomes[key]:
            distances_vector.append(dist)
    return distances_vector


if __name__ == '__main__':

    #vcf_file = 'example.txt'
    #output_file = 'dist.txt'

    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]

    chromosomes = count_dist_between_snps(vcf_file)

    out = open(output_file, 'a')
    out.write('hello')
    out.write(str(collect_distances(chromosomes)))
    print('Done')
