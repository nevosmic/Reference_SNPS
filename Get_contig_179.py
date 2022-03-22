import sys


def filter_vcf(vcf_file, output_file):
    out = open(output_file, "a")
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith('##') or line_items[0].startswith('#'):
                out.write(line)
            elif line_items[0].startswith('C'):
                chrom = line_items[0]
                pos = line_items[1]
                QUAL = line_items[5]
                if chrom == 'CACTIG010000179.1':
                    if 61200000 < int(pos) < 61265000:
                        out.write(line)


if __name__ == '__main__':
    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", vcf_file)
    print("output ", output_file)

    filter_vcf(vcf_file, output_file)