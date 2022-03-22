import sys


def female_counter(f,f_c):
    snip_line = f.split(',')[0]
    snip = snip_line.split(':')[0]
    if snip == '1/1' or snip == '0/1' or snip == '1/0':
        f_c += 1
    return f_c


def males_counter(m,m_c):
    snip_line = m.split(',')[0]
    snip = snip_line.split(':')[0]
    if snip == './.':
        m_c += 1
    return m_c


def find_snps(vcf_file, output_file):
    out = open(output_file, "a")
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith('##') or line_items[0].startswith('#'):
                out.write(line)
            elif line_items[0].startswith('N'):
                females_snp = 0
                males_no_snp = 0
                f1 = line_items[9]
                f2 = line_items[10]
                f4 = line_items[11]
                f6 = line_items[12]
                f8 = line_items[13]
                m1_mq1 = line_items[14]
                m3_mq1 = line_items[15]
                m5_mq1 = line_items[16]
                m7_mq1 = line_items[17]
                m9_mq1 = line_items[18]
                m1 = line_items[19]
                m3 = line_items[20]
                m5 = line_items[21]
                m7 = line_items[22]
                m9 = line_items[23]

                males_no_snp = males_counter(m1,males_no_snp)
                males_no_snp = males_counter(m3,males_no_snp)
                males_no_snp = males_counter(m5,males_no_snp)
                males_no_snp = males_counter(m7,males_no_snp)
                males_no_snp = males_counter(m9,males_no_snp)
                males_no_snp = males_counter(m1_mq1,males_no_snp)
                males_no_snp = males_counter(m3_mq1,males_no_snp)
                males_no_snp = males_counter(m5_mq1,males_no_snp)
                males_no_snp = males_counter(m7_mq1,males_no_snp)
                males_no_snp = males_counter(m9_mq1,males_no_snp)

                females_snp = female_counter(f1, females_snp)
                females_snp = female_counter(f2, females_snp)
                females_snp = female_counter(f4, females_snp)
                females_snp = female_counter(f6, females_snp)
                females_snp = female_counter(f8, females_snp)

                if females_snp == 5 and males_no_snp == 10:
                    out.write(line)


if __name__ == '__main__':

    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]
    print("input ", vcf_file)
    print("output ", output_file)
    '''output_file = 'NEW_PIPELINE.txt'
    vcf_file = 'example_all_fish_15.txt'''

    find_snps(vcf_file, output_file)