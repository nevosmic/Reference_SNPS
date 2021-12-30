import sys


def create_bed(input_file, output_file):
    out = open(output_file, "a")
    with open(input_file) as input_object:
        while True:
            line = input_object.readline()
            if not line:
                break
            line_items = line.split()
            Name_line = line_items[0]
            first,second = Name_line.split("gene=")
            Name_list = second.split("_[")
            Name_first = Name_list[1]
            Name_second = Name_list[2]
            Name = f'[{Name_first}_[{Name_second}'
            sseqid = line_items[1]
            qstart = line_items[6]
            qend = line_items[7]
            evalue = line_items[10]
            # sseqid /t qstart /t qend /t NAME /t evalue
            values = "\t".join([sseqid, qstart, qend, Name, evalue])
            out.write(values+"\n")


if __name__ == '__main__':
    in_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", in_file)
    print("output ", output_file)

    # output_file = 'bed_out.txt'
    # in_file = 'blastRes-cds_sample.txt'
    create_bed(in_file, output_file)

