import sys


def process_depth(depth_lst):
    for fish in depth_lst:
        if int(fish) < 2:
            return False
    return True


def get_list(vcf_file):
    snips_list = []
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            snips_list.append(line[:-1])

    return snips_list


def remove_duplicates(vcf_file, output_file, snips_list):
    out = open(output_file, "a")
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith('C') or line_items[0].startswith('NW'):
                chrom = line_items[0]
                pos = line_items[1]
                snip = f'{chrom}_{pos}'

                if process_depth(line_items[3:13]):
                    if snip in snips_list:
                        parse_line = line.split(chrom)
                        depth_line = f'{chrom}{parse_line[1][:-1]}'
                        vcf_line = f'{chrom}{parse_line[2]}'
                        new_line = vcf_line[:-1] + '\t' + depth_line + '\n'
                        out.write(new_line)


if __name__ == '__main__':

    snip_file = sys.argv[-3]
    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]
    print("list ", snip_file)
    print("input ", vcf_file)
    print("output ", output_file)

    '''
    output_file = 'NEW_PIPELINE_2.txt'
    vcf_file = 'NEW_PIPELINE.txt'
    snip_file = 'list_snips.txt'
    '''
    snips_list = get_list(snip_file)
    remove_duplicates(vcf_file, output_file, snips_list)