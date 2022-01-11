import sys


def filter_snps(vcf_file,output):
    type=''
    PASS=''
    file = open(output, "a")
    with open(vcf_file) as vcf_object:
        line_1 = vcf_object.readline()
        while True:
            line_2 = vcf_object.readline()
            if not line_2:
                break
            row_items_1 = line_1.split()
            print('row_items_1:', row_items_1)
            chrom = row_items_1[0]
            non, a, b = line_1.split(chrom)
            a_s = a.split()
            b_s = b.split()
            pos_a = a_s[0]
            pos_b = b_s[0]
            type_prev = type
            PASS_prev = PASS

            if pos_a != pos_b:
                INFO_b = b_s[6].split(';')
                type = INFO_b[-3] # 38
                PASS = 'NO PASS PREV COMPLEX'
            else:  # same pos check prev
                if PASS_prev is 'NO PASS PREV COMPLEX':  # prev complex
                    line = f'{line_1}\t{PASS_prev}\t{type_prev}'
                    file.write(line)
                elif b_s[-3].startswith('./././.'):  # check males snp of b
                    PASS = 'PASS'
                    file.write(f'{line_1}\t{PASS}\t{type})

            row_items_2 = line_2.split()
            print('row_items_2:' ,row_items_2)
            """
            chrom_a =
            pos_a =
            chrom_b =
            pos_b =
            if row_items_1[0].startswith('NC') and row_items_2[0].startswith('NC'):
                process_lines(row_items_1, row_items_2, chromosomes)
            line_1 = line_2"""


if __name__ == '__main__':
    vcf_file = 'Males_equal_to_ref_p4_unfiltered_intersect_WAO.vcf'
    output_file = 'intersect_filter.txt'


    filter_snps(vcf_file)
