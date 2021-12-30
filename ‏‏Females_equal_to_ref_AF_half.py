import sys


def male_counter(m,m_c):
    global m_counter
    m = m[:7]
    if m == '1/1/1/1':
        m_c += 1
    return m_c


def female_dot_counter(f,fdot_c):# no evidence
    global f_dot
    f = f[:7]
    if f == './././.':
        fdot_c += 1
    return fdot_c


def female_0_counter(f,f0_c):
    global f_0
    f = f[:7]
    if f == '0/0/0/0':
        f0_c += 1
    return f0_c


def process_Info(Info):
    AF = ""
    AN_line = Info[39]
    title, AN = AN_line.split('=')
    AC_line = Info[40]
    title, AC = AC_line.split('=')
    if AC.__contains__(','):
        if len(AC.split(',')) == 2:
            AC_1, AC_2 = AC.split(',')
            AF = "{},{}".format(float(AC_1) / float(AN), float(AC_2) / float(AN))
        elif len(AC.split(',')) == 3:
            AC_1, AC_2, AC_3 = AC.split(',')
            AF = "{},{},{}".format(float(AC_1) / float(AN), float(AC_2) / float(AN), float(AC_3) / float(AN))
        elif len(AC.split(',')) == 4:
            AC_1, AC_2, AC_3, AC_4 = AC.split(',')
            AF = "{},{},{},{}".format(float(AC_1) / float(AN), float(AC_2) / float(AN), float(AC_3) / float(AN), float(AC_4) / float(AN))
    else:
        AF = "{}".format(float(AC) / float(AN))
    return AF


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
            elif line_items[0].startswith('C'):
                chrom = line_items[0]
                pos = line_items[1]
                QUAL = line_items[5]
                Info = line_items[7].split(';')
                AF = process_Info(Info)
                m_c = 0
                f0_c = 0
                fdot_c = 0
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
                m_c=male_counter(m1,m_c)
                m_c=male_counter(m3,m_c)
                m_c=male_counter(m5,m_c)
                m_c=male_counter(m7,m_c)
                m_c=male_counter(m9,m_c)
                f0_c=female_0_counter(f1,f0_c)
                f0_c=female_0_counter(f2,f0_c)
                f0_c=female_0_counter(f4,f0_c)
                f0_c=female_0_counter(f6,f0_c)
                f0_c=female_0_counter(f8,f0_c)
                fdot_c=female_dot_counter(f1,fdot_c)
                fdot_c=female_dot_counter(f2,fdot_c)
                fdot_c=female_dot_counter(f4,fdot_c)
                fdot_c=female_dot_counter(f6,fdot_c)
                fdot_c=female_dot_counter(f8,fdot_c)
                if m_c == 5 and (f0_c == 5 or fdot_c == 5):
                    out.write(line)


if __name__ == '__main__':
    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", vcf_file)
    print("output ", output_file)

    # output_file = 'count_evidence.txt'
    # vcf_file = 'Female_M5.txt'
    count_evidence(vcf_file, output_file)

