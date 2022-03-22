import sys


def male_counter(m,m_c):
    snip_line = m.split(',')[0]
    m = snip_line.split(':')[0]
    if m == '1/1':
        m_c += 1
    return m_c


def female_counter(f, f_c):
    snip_line = f.split(',')[0]
    f = snip_line.split(':')[0]
    if f != '1/1':
        f_c += 1
    return f_c


def count_evidence(vcf_file, output_file):
    out = open(output_file, "a")
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith('##') or line_items[0].startswith('#'):
                out.write(line)
            elif line_items[0].startswith('C') or line_items[0].startswith('NW'):
                m_c = 0
                f_c = 0
                m1 = line_items[9]
                m3 = line_items[10]
                m5 = line_items[11]
                m7 = line_items[12]
                m9 = line_items[13]
                f1 = line_items[14]
                f2 = line_items[15]
                f4 = line_items[16]
                f6 = line_items[17]
                f8 = line_items[18]
                f1_1 = line_items[19]
                f2_1 = line_items[20]
                f4_1 = line_items[21]
                f6_1 = line_items[22]
                f8_1 = line_items[23]
                m_c = male_counter(m1,m_c)
                m_c = male_counter(m3,m_c)
                m_c = male_counter(m5,m_c)
                m_c = male_counter(m7,m_c)
                m_c = male_counter(m9,m_c)
                f_c = female_counter(f1, f_c)
                f_c = female_counter(f2, f_c)
                f_c = female_counter(f4, f_c)
                f_c = female_counter(f6, f_c)
                f_c = female_counter(f8, f_c)
                f_c = female_counter(f1_1, f_c)
                f_c = female_counter(f2_1, f_c)
                f_c = female_counter(f4_1, f_c)
                f_c = female_counter(f6_1, f_c)
                f_c = female_counter(f8_1, f_c)

                if m_c == 5 and f_c == 10:
                    out.write(line)


if __name__ == '__main__':

    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", vcf_file)
    print("output ", output_file)
    '''
    output_file = 'NEW_PIPELINE.txt'
    vcf_file = 'Female_all_fish_15'
    '''

    count_evidence(vcf_file, output_file)

