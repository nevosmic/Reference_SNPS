import sys


def create_bed(minimap2, output_file):
    out = open(output_file, "a")
    with open(minimap2) as minimap2_object:
        while True:
            line = minimap2_object.readline()
            if not line:
                break
            line_items = line.split()
            query_header = line_items[0]
            target_name = line_items[5]
            target_start = line_items[7]
            target_end = line_items[8]
            values = "\t".join([target_name, target_start, target_end, query_header])
            out.write(values+"\n")


if __name__ == '__main__':

    in_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("input ", in_file)
    print("output ", output_file)

    create_bed(in_file, output_file)

