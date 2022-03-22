import sys


def find_snps(vcf_file, output_file):
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
                out.write(snip + "\n")


if __name__ == '__main__':

    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]
    print("input ", vcf_file)
    print("output ", output_file)

    find_snps(vcf_file, output_file)