import os
def file_read_from_tail(fname, lines):
    buf_size = 8192
    f_size = os.stat(fname).st_size
    iterito = 0
    with open(fname) as f:
        if buf_size > f_size:
            buf_size = f_size-1
            data = []
            while True:
                iterito += 1
                f.seek(f_size - buf_size * iterito)
                data.extend(f.readlines())
                if len(data) >= lines or f.tell() == 0:
                    print(''.join(data[-lines:]))
                    break

file_read_from_tail('a.txt', 0)

#dont get it