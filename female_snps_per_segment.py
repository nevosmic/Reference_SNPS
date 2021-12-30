import math
import sys
import os
#segment_size = 10000
i = 0
_range = 0


def create_contigs_vector(dict_of_contigs):
    contigs_vector = []
    for contig in dict_of_contigs.keys():
        contig_list = dict_of_contigs[contig]
        for segment in contig_list:
            contigs_vector.append(segment)
    return contigs_vector


def contigs_len(contigs_list):
    contigs_len = {}
    contigs_file = open(contigs_list, 'r')
    while True:
        line = contigs_file.readline()
        if not line:
            break
        line_items = line.split(',')
        contig_items = line_items[0].split('=',2)
        contig = contig_items[2]
        line_items = line_items[1].split('=')
        len_of_contig = line_items[1][:-2]
        contigs_len[contig] = int(len_of_contig)

    return contigs_len


def process_first_line(line1_items, dict_of_contigs, segment_size, contigs_len):
    global i
    global _range
    contig_1 = line1_items[0]
    pos_1 = int(line1_items[1])
    if pos_1 <= contigs_len[contig_1]:
        # case 1 : empty segment
        while pos_1 > segment_size*i and pos_1 > segment_size+segment_size*(i):
            if contig_1 in dict_of_contigs.keys():
                dict_of_contigs[contig_1].append(0)
            else:
                dict_of_contigs[contig_1] = [0]
            i += 1  # maybe not
        # case 2 : new segment - pos not bigger then segment_size+segment_size*(i+1)
        if pos_1 > segment_size*i:
            if contig_1 in dict_of_contigs.keys():
                # num_of_segments = len(dict_of_contigs[contig])
                # dict_of_contigs[contig][num_of_segments - 1] += 1
                dict_of_contigs[contig_1].append(1)
                i += 1  # maybe not
            else:
                dict_of_contigs[contig_1] = [1]
            # i += 1 ??
        else:  # case 3 : same segment
            num_of_segments = len(dict_of_contigs[contig_1])
            #if num_of_segments >= 1:
            dict_of_contigs[contig_1][num_of_segments-1] += 1


def process_line(line1_items, line2_items, dict_of_contigs, segment_size, contigs_len):
    global i
    global _range
    contig_1 = line1_items[0]
    pos_1 = int(line1_items[1])
    contig_2 = line2_items[0]
    pos = int(line2_items[1])
    if i > _range or contig_2 != contig_1:  # reset i and range
        i = 0
        _range = math.floor(contigs_len[contig_2]/segment_size)

    if pos <= contigs_len[contig_2]:
        # case 1 : empty segment
        while pos > segment_size*i and pos > segment_size*(i+1):
            if contig_2 in dict_of_contigs.keys():
                dict_of_contigs[contig_2].append(0)
            else:
                dict_of_contigs[contig_2] = [0]
            i += 1  # maybe not
        # case 2 : new segment - pos not bigger then segment_size*(i+1)
        if pos > segment_size*i:
            if contig_2 in dict_of_contigs.keys():
                dict_of_contigs[contig_2].append(1)
            else:
                dict_of_contigs[contig_2] = [1]
            i += 1
        else:  # case 3 : same segment
            num_of_segments = len(dict_of_contigs[contig_2])
            dict_of_contigs[contig_2][num_of_segments-1] += 1


def first_range(line_items, contigs_len, segment_size):
    global _range
    contig = line_items[0]
    _range = math.floor(contigs_len[contig]/segment_size)


def calculate_snps_per_segment(vcf_file, segment_size, contigs_len):
    # dict_of_contigs = { contig1: [0, 0, 0, 0, 3, 1, 5..], contig2:...}
    dict_of_contigs = {}

    with open(vcf_file) as vcf_object:
        # find first chromosome
        while True:
            line1 = vcf_object.readline()
            if not line1:
                break
            line1_items = line1.split()
            if line1_items[0].startswith('NC'):
                break
        first_range(line1_items, contigs_len, segment_size)
        process_first_line(line1_items, dict_of_contigs, segment_size, contigs_len)

        while True:
            line2 = vcf_object.readline()
            if not line2:
                break
            line1_items = line1.split()
            line2_items = line2.split()
            if line1_items[0].startswith('NC') and line2_items[0].startswith('NC'):
                process_line(line1_items, line2_items, dict_of_contigs, segment_size, contigs_len)
            line1 = line2

    return dict_of_contigs


if __name__ == '__main__':

    # contigs_len = contigs_len('contigs_list.txt')
    # print(contigs_len)
    # vcf_file = 'CACTIG010000001.1_CACTIG010000002.1'
    # segment_size = 10000
    # calculate_snps_per_segment(vcf_file, segment_size, contigs_len)

    vcf_file = sys.argv[-5]
    output1_file = sys.argv[-4]
    output2_file = sys.argv[-3]
    contigs_list = sys.argv[-2]
    segment_size = int(sys.argv[-1])

    print('vcf_file', vcf_file)
    print('output1_file',output1_file)
    print('output2_file', output2_file)
    print('contigs_list', contigs_list)
    print('segment_size',segment_size)

    contigs_len = contigs_len(contigs_list)
    print(contigs_len)

    dict_of_contigs = calculate_snps_per_segment(vcf_file, segment_size, contigs_len)
    out = open(output1_file, "w")
    out.write(str(dict_of_contigs))

    contigs_vector = create_contigs_vector(dict_of_contigs)
    out2 = open(output2_file, "w")
    out2.write(str(contigs_vector))
    print('Done')

