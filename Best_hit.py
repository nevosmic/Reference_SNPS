import sys


def calculate_cov(query_length, query_start, query_end):
    cov = ((int(query_end) - int(query_start)) / int(query_length)) * 100
    return cov


def best_hits(input_file, output_file):
    out = open(output_file, "a")
    with open(input_file) as input_object:
        # first line
        line_1 = input_object.readline()
        best_hit = line_1
        max_cov = -1
        first_is_pair = False
        second_is_best = False
        while True:
            line_2 = input_object.readline()
            if not line_2:
                out.write(line_1)
                break
            line1_items = line_1.split()
            line2_items = line_2.split()
            Name_line1 = line1_items[0]
            Name_line2 = line2_items[0]
            if Name_line1 == Name_line2:
                if first_is_pair:  # case 3
                    cov_2 = calculate_cov(line2_items[1],line2_items[2],line2_items[3])
                    if cov_2 > max_cov:
                        max_cov = cov_2
                        best_hit = line_2
                        second_is_best = True
                else:
                    cov_1 = calculate_cov(line1_items[1],line1_items[2],line1_items[3])
                    cov_2 = calculate_cov(line2_items[1],line2_items[2],line2_items[3])
                    if cov_1 >= cov_2:
                        max_cov = cov_1
                        best_hit = line_1
                    else:
                        max_cov = cov_2
                        best_hit = line_2
                        second_is_best = True
                    first_is_pair = True
            elif first_is_pair:  # case 2
                if second_is_best:
                    best_hit = '{}\tSecond is best hit\n'.format(best_hit[:-1])
                    second_is_best = False
                out.write(best_hit)
                first_is_pair = False
                max_cov = -1
                best_hit = line_2
            else:
                # case 1
                out.write(line_1)
            line_1 = line_2


if __name__ == '__main__':

    input = sys.argv[-2]
    output = sys.argv[-1]

    best_hits(input, output)

