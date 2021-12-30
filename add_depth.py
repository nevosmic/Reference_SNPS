import sys


def parse_depth_dict(depth_file):
    depth_dict = {}
    with open(depth_file) as depth_object:
        while True:
            line = depth_object.readline()
            if not line:
                break
            line_items = line.split(",")
            for item in line_items:
                item = item[2:-1]
                if item.startswith("N"):
                    chrom,rest = item.split(":",1)
                    chrom = chrom[:-1]
                    key = rest[2:]
                    depth_dict[chrom]=key
    return depth_dict


def add_depth_2_vcf(vcf_file, depth_dict, output_file):
    out = open(output_file, "a")
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith('#'):
                out.write(line)
            elif line_items[0].startswith('NC'):
                chrom = line_items[0]
                pos = line_items[1]
                key = f'{chrom}_{pos}'
                depth = " "
                if key in depth_dict.keys():
                    depth = depth_dict[key]
                final_line = f'{line[:-1]} {depth}\n'
                out.write(final_line)


if __name__ == '__main__':
    depth_file = sys.argv[-3]
    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("depth_file ", depth_file)
    print("input ", vcf_file)
    print("output ", output_file)

    # output_file = 'out.vcf'
    # vcf_file = 'vcf_example.vcf'
    # depth_file = 'depth_dict'
    depth_dict = parse_depth_dict(depth_file)
    print(depth_dict)
    add_depth_2_vcf(vcf_file, depth_dict, output_file)

