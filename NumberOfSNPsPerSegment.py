import sys
import os
segment_size = 10000
snps_counter = 0


def process_lines(line1_items, line2_items, chromosomes, seg_increase):
    global segment_size
    chrom1 = line1_items[0]
    chrom2 = line2_items[0]
    pos2 = int(line2_items[1])

    if pos2 <= segment_size:  # same segment
        if chrom1 == chrom2:  # same chrom
            num_of_segments = len(chromosomes[chrom2])
            if num_of_segments >= 1:
                chromosomes[chrom2][num_of_segments-1] += 1
        else: # new chrom
            chromosomes[chrom2] = [1]
    else:  # new segment
        while pos2 > segment_size:
            segment_size += int(seg_increase)
        if chrom1 == chrom2:
            # num_of_segments = len(chromosomes[chrom2])
            # if num_of_segments >= 1:
            #     chromosomes[chrom2][num_of_segments-1] += 1
            chromosomes[chrom2].append(1)
        else:
            chromosomes[chrom2] = [1]


def insert_first(line1_items, chromosomes, seg_increase):
    global segment_size
    chrom1 = line1_items[0]
    pos1 = int(line1_items[1])
    if pos1 < segment_size:
        chromosomes[chrom1] = [1]
    else:  # new segment
        while pos1 > segment_size:
            segment_size += int(seg_increase)
        chromosomes[chrom1] = [1]


def calculate_snps_per_segment(vcf_file, seg_increase):
    # chromosomes = { chr1: [6, 11, 80], chr2:...}
    chromosomes = {}

    with open(vcf_file) as vcf_object:
        # find first chromosome
        while True:
            line1 = vcf_object.readline()
            if not line1:
                break
            line1_items = line1.split()
            if line1_items[0].startswith('N'):
                break
        insert_first(line1_items, chromosomes, seg_increase)

        while True:
            line2 = vcf_object.readline()
            if not line2:
                break
            line1_items = line1.split()
            line2_items = line2.split()
            if line1_items[0].startswith('N') and line2_items[0].startswith('N'):
                process_lines(line1_items, line2_items, chromosomes, seg_increase)
            line1 = line2

    print(chromosomes)
    return chromosomes


if __name__ == '__main__':
    # output_file = 'snps_per_segment.txt'
    # seg_increase = 10000
    # vcf_file = "vcf_example.vcf"

    seg_increase = sys.argv[-3]
    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]
    print('seg_increase',seg_increase)
    print('vcf_file',vcf_file)
    print('output_file',output_file)

    if os.stat(vcf_file).st_size != 0:
        chromosomes = calculate_snps_per_segment(vcf_file, seg_increase)
        out = open(output_file, "w")
        out.write(str(chromosomes))

