def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    X = []
    f = open(csv_file_path, "r")
    while(True):
        line = f.readline()
        if not line:
            break
        line = line.strip().replace('"', '').split(',')
        x = []
        for i in line:
            if i.isdecimal():
                x.append(int(i))
            elif i.isdigit():
                x.append(float(i))
            else:
                x.append(str(i))
        X.append(x)
    f.close
    return X
