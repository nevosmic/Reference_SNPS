import sys


def get_type(info):
    parse_info = info.split('VDB=')
    snip_info = parse_info[-1].split(';')[1:]
    if len(snip_info) > 2:
        if snip_info[0]== 'INDEL':
            type = snip_info[1]
        else:
            type = snip_info[0]
    else:
        type = snip_info[0]
    return type


def add_type(vcf_file, output_file):
    out = open(output_file, "a")
    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            info = line_items[7]
            type = get_type(info)
            out.write(f'{line[:-1]}\t{type}\n')


if __name__ == '__main__':

    vcf_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", vcf_file)
    print("output ", output_file)

    add_type(vcf_file, output_file)


