import sys


def collect_AF(vcf_file):
    AF_vector=[]
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith('N'):
                Info = line_items[7].split(';')
                AF = Info[19].split('=')
                if AF[1].__contains__(','):  # in case there is more than one value
                    AF_items = AF[1].split(',')
                    AF_vector.append(float(AF_items[0]))
                    AF_vector.append(float(AF_items[1]))
                else:
                    AF_vector.append(float(AF[1]))
    return AF_vector


if __name__ == '__main__':
    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", vcf_file)
    print("output ", output_file)

    AF_vector = collect_AF(vcf_file)

    f = open(output_file, "w")
    f.write(str(AF_vector))
