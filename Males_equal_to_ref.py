import sys


def female_counter(f,f_c):
    global f_counter
    f = f[:7]
    if f == '1/1/1/1':
        f_c += 1
    return f_c


def male_dot_counter(m,mdot_c):
    m = m[:7]
    if m == './././.':
        mdot_c += 1
    return mdot_c


def male_0_counter(m,m0_c):
    m = m[:7]
    if m == '0/0/0/0':
        m0_c += 1
    return m0_c


def male_0_or_dot_counter(m,m_c):

    m = m[:7]
    if m == '0/0/0/0' or m == './././.':
        m_c += 1
    return m_c


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
            elif line_items[0].startswith('N'):
                f_c = 0
                m0_c = 0
                mdot_c = 0
                m_c = 0
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
                m_c=male_0_or_dot_counter(m1,m_c)
                m_c=male_0_or_dot_counter(m3,m_c)
                m_c=male_0_or_dot_counter(m5,m_c)
                m_c=male_0_or_dot_counter(m7,m_c)
                m_c=male_0_or_dot_counter(m9,m_c)
                m0_c=male_0_counter(m1,m0_c)
                m0_c=male_0_counter(m3,m0_c)
                m0_c=male_0_counter(m5,m0_c)
                m0_c=male_0_counter(m7,m0_c)
                m0_c=male_0_counter(m9,m0_c)
                mdot_c=male_dot_counter(m1,mdot_c)
                mdot_c=male_dot_counter(m3,mdot_c)
                mdot_c=male_dot_counter(m5,mdot_c)
                mdot_c=male_dot_counter(m7,mdot_c)
                mdot_c=male_dot_counter(m9,mdot_c)
                f_c = female_counter(f1,f_c)
                f_c = female_counter(f2, f_c)
                f_c = female_counter(f4, f_c)
                f_c = female_counter(f6, f_c)
                f_c = female_counter(f8, f_c)
                if f_c == 5 and (m0_c == 5 or mdot_c == 5 or m_c == 5):
                    out.write(line)


if __name__ == '__main__':
    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", vcf_file)
    print("output ", output_file)

    # output_file = 'count_evidence.txt'
    # vcf_file = 'Female_M5.txt'
    count_evidence(vcf_file, output_file)

