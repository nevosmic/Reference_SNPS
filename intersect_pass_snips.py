
def filter_snps(vcf_file, output):
    file = open(output, "a")
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith('##') or line_items[0].startswith('#'):
                file.write(line)
            elif line_items[-2] == 'PASS':
                file.write(line)


def remove_fake_snips(input_file, list_, final_file):
    file = open(final_file, "a")
    with open(input_file) as input_object:
        while True:
            line = input_object.readline()
            if not line:
                break
            line_items = line.split()
            # variables:
            pos_a = line_items[1]
            if pos_a in list_:
                file.write(line)


if __name__ == '__main__':
    '''vcf_file = 'intersect_filter_second.vcf'
    output_file = 'intersect_pass_snips.vcf'
    vcf_file = 'intersect_filter_p2.vcf'
    output_file = 'intersect_pass_snips_p2.vcf

    filter_snps(vcf_file, output_file)
    input_file = 'Males_equal_to_ref_p4_unfiltered_intersect_WAO_with_depth.txt'
    '''
    input_file = 'Males_equal_ref_p2_depth_intersect_with_filter.vcf'
    list_ = []
    list_file = open('210_snips.txt', "r")
    for line in list_file.readlines():
        if line == '496604':
            list_.append(line)
        else:
            list_.append(line[:-1])
    print(list_)
    print(len(list_))
    final_file = 'final_pass_snip_p2.txt'
    remove_fake_snips(input_file, list_, final_file)