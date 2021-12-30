import sys


def create_bed(input_file, output_file):
    out = open(output_file, "a")
    with open(input_file) as input_object:
        while True:
            line = input_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith('C'):
                chrom = line_items[0]
                pos = line_items[1]
                values = "\t".join([chrom, pos, pos])
                out.write(values+"\n")


if __name__ == '__main__':
    in_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", in_file)
    print("output ", output_file)

    # output_file = 'bed_out.txt'
    # in_file = 'females_equal_to_ref_0_or_dot_P2_1000.txt'
    create_bed(in_file, output_file)

