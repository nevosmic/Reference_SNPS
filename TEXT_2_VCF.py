import sys


def turn2vcf(vcf_file, text_file, output_file):
    """ print vcf first lines """
    out = open(output_file, "a")
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith('##') or line_items[0].startswith('#'):
                out.write(line)
    """ print text lines """
    with open(text_file) as text_object:
        while True:
            line = text_object.readline()
            if not line:
                break
            out.write(line)

    out.close()
    vcf_object.close()
    text_object.close()


if __name__ == '__main__':

    vcf_file = sys.argv[-3]
    text_file = sys.argv[-2]
    output_file = sys.argv[-1]
    print("vcf ", vcf_file)
    print("text ", text_file)
    print("output ", output_file)

    turn2vcf(vcf_file, text_file, output_file)