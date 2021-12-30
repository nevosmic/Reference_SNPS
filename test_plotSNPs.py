def get_keys(data):
    keys = []
    #print('data: ', data)
    chroms = data.split(',')
    for chrom in chroms:
        if chrom.__contains__('['):
            chrom = chrom[2:-1]
        elif chrom.__contains__(']'):
            chrom = chrom[2:-3]
        else:
            chrom = chrom[2:-1]
        keys.append(chrom)
    return keys


def get_vals(data):
    vals = []
    data = data[0:-1]
    #print('data', data)
    vals_data = data.split(']')
    vals_data = vals_data[:-2]
    print('vals_data',vals_data)
    for val_list in vals_data:
        val_to_add = []
        items = val_list.split(',')

        for item in items:
            if item != '' and item != ' ':
                if item.__contains__('[['):
                    item = item[2:]
                    print(item)
                elif item.__contains__('['):
                    split_1,split_2 = item.split('[')
                    item = split_2
                val_to_add.append(int(item))

        print('val_to_add', val_to_add)
        vals.append(val_to_add)
    #print(vals)
    return vals


def parse_chromosomes(file):
    chroms_file = open(file, 'r')
    while True:
        line = chroms_file.readline()
        if not line:
            break
        if line != "\n":
            first, second = line.split(':')
            if first == "dict_keys":
                keys = get_keys(second)
                # print(keys)
            elif first == "dict_values":
                vals = get_vals(second)


    dict = {keys[k]:vals[k] for k in range(len(keys))}
    print(dict)
    return dict


if __name__ == '__main__':
    dict = parse_chromosomes('keys_vals.txt')
