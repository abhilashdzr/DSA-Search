from csv import DictWriter

def my_write(file, d):
    with open(file, 'a') as f:
        w = DictWriter(f, d.keys())

        if f.tell() == 0:
            w.writeheader()

        w.writerow(d)

def process(s):
    return ' '.join(s.split())