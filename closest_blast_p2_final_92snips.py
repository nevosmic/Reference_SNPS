
def get_87_snips_from_blast(input_file, list_, final_file):
    file = open(final_file, "a")
    with open(input_file) as input_object:
        while True:
            line = input_object.readline()
            if not line:
                break
            line_items = line.split()
            # variables:
            pos_a = line_items[1]
            if pos_a in list_:
                file.write(line)


if __name__ == '__main__':

    list_ = []
    list_file = open('87_final_snips_p2.txt', "r")
    for line in list_file.readlines():
        if line == '2530587':
            list_.append(line)
        else:
            list_.append(line[:-1])

    input_file = 'closest_p2_unfiltered_k.bed'
    final_file = 'closest_p2_unfiltered_blast_87.bed'
    get_87_snips_from_blast(input_file, list_, final_file)
