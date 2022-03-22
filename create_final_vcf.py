import sys


def get_list(vcf_file):
    snips_list = []
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            chrom = line_items[0]
            pos = line_items[1]
            snip = f'{chrom}_{pos}'
            snips_list.append(snip)

    return snips_list


def remove_duplicates(vcf_file, output_file, snips_list):

    out = open(output_file, "a")
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith('##') or line_items[0].startswith('#'):
                out.write(line)
            if line_items[0].startswith('C') or line_items[0].startswith('NW'):
                chrom = line_items[0]
                pos = line_items[1]
                snip = f'{chrom}_{pos}'
                if snip in snips_list:
                    out.write(line)


if __name__ == '__main__':

    snip_file = sys.argv[-3]
    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]
    print("list ", snip_file)
    print("input ", vcf_file)
    print("output ", output_file)
    '''
    snip_file = 'NEW_PIPELINE_SNIPS'
    vcf_file = 'NEW_PIPELINE.txt'
    output_file = 'NEW_PIPELINE_2.txt'
    '''

    snips_list = get_list(snip_file)
    print(snips_list)
    print(len(snips_list))
    remove_duplicates(vcf_file, output_file, snips_list)