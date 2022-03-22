import sys


def process_line(info):
    if info.startswith('INDEL'):
        return False
    return True


def remove_indels(vcf_file, output_file):
    out = open(output_file, "a")
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if process_line(line_items[20]):
                out.write(line)


if __name__ == '__main__':

    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]
    print("input ", vcf_file)
    print("output ", output_file)

    remove_indels(vcf_file, output_file)