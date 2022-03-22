import sys


def create_bed(minimap2, output_file):
    out = open(output_file, "a")
    with open(minimap2) as minimap2_object:
        while True:
            line = minimap2_object.readline()
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
            sstart = line_items[8]
            send = line_items[9]
            evalue = line_items[10]
            # sseqid /t sstart /t send /t NAME /t evalue
            if sstart > send:
                values = "\t".join([sseqid, send, sstart, '-', Name, evalue])
            else:
                values = "\t".join([sseqid, sstart, send, Name, evalue])
            out.write(values+"\n")


if __name__ == '__main__':

    in_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", in_file)
    print("output ", output_file)

    create_bed(in_file, output_file)

