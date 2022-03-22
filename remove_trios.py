import sys


def remove_trios(vcf_file, trios_list, output_file):
    out = open(output_file, "a")
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith('C'):
                chrom = line_items[0]
                pos = line_items[1]
                check = f'{chrom}_{pos}'
                if check not in trios_list:
                    out.write(line)


def get_trios(vcf_file):
    trio_list = []
    """ get trios """
    with open(vcf_file) as vcf_object:
        line_1 = vcf_object.readline()
        line_2 = vcf_object.readline()
        while True:
            line_3 = vcf_object.readline()
            if not line_3:
                break
            line_1_items = line_1.split()
            line_2_items = line_2.split()
            line_3_items = line_3.split()
            # variables:
            chrom_1 = line_1_items[0]
            pos_1 = int(line_1_items[1])
            chrom_2 = line_2_items[0]
            pos_2 = int(line_2_items[1])
            chrom_3 = line_3_items[0]
            pos_3 = int(line_3_items[1])
            if chrom_1 == chrom_2 == chrom_3:
                if pos_1 == pos_2 and pos_2+1 == pos_3:  # trio
                    trio_list.append(f'{chrom_1}_{pos_1}')
                    trio_list.append(f'{chrom_2}_{pos_2}')
                    trio_list.append(f'{chrom_3}_{pos_3}')

            line_1 = line_2
            line_2 = line_3

    return trio_list


if __name__ == '__main__':
    '''
    vcf_file = 'males_equal_to_ref_15_intersect_depth_no_dup.vcf'
    output_file = 'NEW_PIPELINE.txt'
    '''
    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]
    print("input ", vcf_file)
    print("output ", output_file)

    trios_list = get_trios(vcf_file)
    print(trios_list)
    print(len(trios_list))
    remove_trios(vcf_file, trios_list, output_file)