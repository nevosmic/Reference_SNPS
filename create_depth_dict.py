import sys


def create_depth_dict(depth_file):
    depth_dict = {}
    with open(depth_file) as depth_object:
        while True:
            line = depth_object.readline()
            if not line:
                break
            line_items = line.split()
            if not line_items[0].startswith('#'):
                chrom = line_items[0]
                pos = line_items[1]
                f1 = line_items[2]
                f2 = line_items[3]
                f4 = line_items[4]
                f6 = line_items[5]
                f8 = line_items[6]
                m1 = line_items[7]
                m3 = line_items[8]
                m5 = line_items[9]
                m7 = line_items[10]
                m9 = line_items[11]
                key = f'{chrom}_{pos}'
                depth_dict[key] = f'depth  F1:{f1}     F2:{f2}     F4:{f4}     F6:{f6}     F8:{f8}     M1:{m1}     M3:{m3}     M5:{m5}     M7:{m7}     M9:{m9}'
    return depth_dict


if __name__ == '__main__':
    depth_file = sys.argv[-2]
    output_file = sys.argv[-1]

    print("depth_file ", depth_file)
    print("output ", output_file)

    depth_dict = create_depth_dict(depth_file)
    out = open(output_file, "a")
    out.write(str(depth_dict))

