import sys


def count_evidence(vcf_file, output_file):
    out = open(output_file, "a")
    out.write("CHROM\tPOS\tMALE\tFEMALE\tQUAL\tAF\n")
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith('N'):
                chrom = line_items[0]
                pos = line_items[1]
                QUAL = line_items[5]
                Info = line_items[7].split(';')
                AF = Info[19]
                male_counter = 0
                female_counter = 0
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
                if m1.startswith('0') or m1.startswith('1'):
                    male_counter += 1
                if m3.startswith('0') or m3.startswith('1'):
                    male_counter += 1
                if m5.startswith('0') or m5.startswith('1'):
                    male_counter += 1
                if m7.startswith('0') or m7.startswith('1'):
                    male_counter += 1
                if m9.startswith('0') or m9.startswith('1'):
                    male_counter += 1
                if f1.startswith('0') or f1.startswith('1'):
                    female_counter += 1
                if f2.startswith('0') or f2.startswith('1'):
                    female_counter += 1
                if f4.startswith('0') or f4.startswith('1'):
                    female_counter += 1
                if f6.startswith('0') or f6.startswith('1'):
                    female_counter += 1
                if f8.startswith('0') or f8.startswith('1'):
                    female_counter += 1
                out.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(chrom,pos,male_counter,female_counter,QUAL,AF))


if __name__ == '__main__':
    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", vcf_file)
    print("output ", output_file)

    # output_file = 'count_evidence.txt'
    # vcf_file = '2snip.vcf'
    count_evidence(vcf_file, output_file)
