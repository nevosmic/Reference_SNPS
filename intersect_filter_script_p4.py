

def get_type(b_s):
    INFO_b = b_s[6].split(';')
    type = INFO_b[-3]  # 38
    return type


def single(b_s_1, line_1, file):
    type = get_type(b_s_1)
    if b_s_1[-3].startswith('./././.'):  # b-males have no snp
        if 'complex' in type:
            PASS = 'NO PASS COMPLEX'
            file.write(f'{line_1[:-1]}\t{PASS}\t{type}\n')
        else:
            PASS = 'PASS'
            file.write(f'{line_1[:-1]}\t{PASS}\t{type}\n')
    else:
        PASS = 'NO PASS male snp'
        file.write(f'{line_1[:-1]}\t{PASS}\t{type}\n')


def filter_snps(wao_file, vcf_file, output):
    file = open(output, "a")
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith('##') or line_items[0].startswith('#'):
                file.write(line)
            else:
                break
    with open(wao_file) as wao_object:
        line_1 = wao_object.readline()
        while True:
            line_2 = wao_object.readline()
            if not line_2:
                single(b_s_1, line_1, file)
                break
            line_1_items = line_1.split()
            line_2_items = line_2.split()
            if int(line_1_items[-1]) >= 1:  # pass null rows
                if int(line_2_items[-1]) == 0:
                    PASS = 'NULL'
                    file.write(f'{line_2[:-1]}\t{PASS}\t{PASS}\n')
                    if not prev_couple:
                        single(b_s_1, line_1, file)
                    line_1 = wao_object.readline()
                    if not line_1:
                        break
                    prev_couple = False
                else:
                    # variables:
                    chrom_1 = line_1_items[0]
                    chrom_2 = line_2_items[0]
                    non, a_1, b_1 = line_1.split(chrom_1)
                    non, a_2, b_2 = line_2.split(chrom_2)
                    a_s_1 = a_1.split()
                    b_s_1 = b_1.split()
                    a_s_2 = a_2.split()
                    b_s_2 = b_2.split()
                    pos_a_1 = a_s_1[0]
                    pos_b_1 = b_s_1[0]
                    pos_a_2 = a_s_2[0]
                    pos_b_2 = b_s_2[0]
                    if pos_a_1 == pos_a_2:  # repetition
                        if pos_a_1 == pos_b_1:
                            PASS_1 = 'NO PASS next complex'
                            couple = True
                            type_1 = get_type(b_s_1)
                            line_ = f'{line_1[:-1]}\t{PASS_1}\t{type_1}\n'
                            file.write(line_)
                        elif pos_a_2 == pos_b_2:
                            PASS_2 = 'NO PASS prev complex'
                            couple = True
                            type_2 = get_type(b_s_2)
                            line_ = f'{line_2[:-1]}\t{PASS_2}\t{type_2}\n'
                            file.write(line_)
                    elif pos_a_1 != pos_a_2 and prev_couple:  # line_1 is a part of a couple
                        couple = False
                        pass  # maybe
                    # single:
                    else:
                        couple = False
                        single(b_s_1, line_1, file)
                    # swap
                    line_1 = line_2
                    prev_couple = couple
            else: # pass line 1
                PASS = 'NULL'
                file.write(f'{line_1[:-1]}\t{PASS}\t{PASS}\n')
                line_1 = line_2
                prev_couple = False


if __name__ == '__main__':
    wao_file = 'Males_equal_to_ref_p4_unfiltered_intersect_WAO.vcf'
    vcf_file = 'Males_equal_to_ref_p4_unfiltered.vcf'
    output_file = 'intersect_filter_second.vcf'

    filter_snps(wao_file, vcf_file, output_file)
