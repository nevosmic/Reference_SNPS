import sys


def process_line(depth_lst):
    for fish in depth_lst:
        if int(fish) < 2:
            return False
    return True


def filter_depth(vcf_file, output_file):
    out = open(output_file, "a")
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if process_line(line_items[3:13]):
                out.write(line)


if __name__ == '__main__':

    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]
    print("input ", vcf_file)
    print("output ", output_file)

    '''
    output_file = 'NEW_PIPELINE.txt'
    vcf_file = 'males_equal_to_ref_15_intersect_depth_no_dup.vcf'
    '''
    filter_depth(vcf_file, output_file)