import sys


def find_depth(depth_file, query):
    depth = ""
    with open(depth_file) as depth_object:
        while True:
            line = depth_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith("NC"):
                chrom = line_items[0]
                pos = line_items[1]
                key = f'{chrom}_{pos}'
                if query == key:
                    F1 = line_items[2]
                    F2 = line_items[3]
                    F4 = line_items[4]
                    F6 = line_items[5]
                    F8 = line_items[6]
                    M1 = line_items[7]
                    M3 = line_items[8]
                    M5 = line_items[9]
                    M7 = line_items[10]
                    M9 = line_items[11]
                    depth = f" depth     F1:{F1}     F2:{F2}     F4:{F4}     F6:{F6}     F8:{F8}     M1:{M1}     M3:{M3}     M5:{M5}     M7:{M7}     M9:{M9}"
                    break
    return depth


def add_depth_2_vcf(vcf_file, depth_file, output_file):
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
                query = f'{chrom}_{pos}'
                depth = find_depth(depth_file, query)
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
    # depth_file = 'depth_EXAMPLE.depth'

    add_depth_2_vcf(vcf_file, depth_file, output_file)

