import sys


def male_counter(m, m_counter):
    if m.startswith('0') or m.startswith('1'):
        m_counter += 1
    return m_counter


def female_counter(f, f_counter):
    if f.startswith('0') or f.startswith('1'):
        f_counter += 1
    return f_counter


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
                m_counter = 0
                f_counter = 0
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
                m_counter = male_counter(m1, m_counter)
                m_counter = male_counter(m3, m_counter)
                m_counter = male_counter(m5, m_counter)
                m_counter = male_counter(m7, m_counter)
                m_counter = male_counter(m9, m_counter)
                f_counter = female_counter(f1, f_counter)
                f_counter = female_counter(f2, f_counter)
                f_counter = female_counter(f4, f_counter)
                f_counter = female_counter(f6, f_counter)
                f_counter = female_counter(f8, f_counter)
                if m_counter == 5 and AF == "1.0":
                    out.write(line)


if __name__ == '__main__':
    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", vcf_file)
    print("output ", output_file)

    # output_file = 'count_evidence.txt'
    # vcf_file = '2snip.vcf'
    count_evidence(vcf_file, output_file)

