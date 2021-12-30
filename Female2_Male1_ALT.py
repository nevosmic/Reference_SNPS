import sys


def male_1_counter(m,m1_c):
    global m_counter
    m = m[:7]
    if m == '1/1':
        m1_c += 1
    return m1_c


def male_2_counter(m,m2_c):
    global m_counter
    m = m[:7]
    if m == '2/2':
        m2_c += 1
    return m2_c


def female_1_counter(f,f1_c):# no evidence
    f = f[:7]
    if f == '1/1':
        f1_c += 1
    return f1_c


def female_2_counter(f,f2_c):
    f = f[:7]
    if f == '2/2':
        f2_c += 1
    return f2_c


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
                ALT_line = line_items[4]
                # Info = line_items[7].split(';')
                # AF = process_Info(Info)
                m1_c = 0
                m2_c = 0
                f1_c = 0
                f2_c = 0
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
                m1_c=male_1_counter(m1,m1_c)
                m1_c=male_1_counter(m3,m1_c)
                m1_c=male_1_counter(m5,m1_c)
                m1_c=male_1_counter(m7,m1_c)
                m1_c=male_1_counter(m9,m1_c)
                m2_c = male_2_counter(m1, m2_c)
                m2_c = male_2_counter(m3, m2_c)
                m2_c = male_2_counter(m5, m2_c)
                m2_c = male_2_counter(m7, m2_c)
                m2_c = male_2_counter(m9, m2_c)
                f1_c=female_1_counter(f1,f1_c)
                f1_c=female_1_counter(f2,f1_c)
                f1_c=female_1_counter(f4,f1_c)
                f1_c=female_1_counter(f6,f1_c)
                f1_c=female_1_counter(f8,f1_c)
                f2_c = female_2_counter(f1, f2_c)
                f2_c = female_2_counter(f2, f2_c)
                f2_c = female_2_counter(f4, f2_c)
                f2_c = female_2_counter(f6, f2_c)
                f2_c = female_2_counter(f8, f2_c)
                isALT = False
                if ALT_line.__contains__(','):
                    isALT = True
                    ALT1,ALT2 = ALT_line.split(',',1)
                    if ALT2.__contains__(','):
                        isALT = False

                if m1_c == 5 and f2_c == 5 and isALT:
                    out.write(line)


if __name__ == '__main__':
    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", vcf_file)
    print("output ", output_file)

    # output_file = 'count_evidence.txt'
    # vcf_file = 'Female_M5.txt'
    count_evidence(vcf_file, output_file)

