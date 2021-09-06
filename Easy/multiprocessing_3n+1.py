from decimal import Decimal
from multiprocessing import Pool
import signal
import time
import sys
import struct
import numpy
import io
import gzip
import json
import collections
import os

class ThreeNPlusOne():

    def __init__(self):
        self.logfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), '3n+1-log.txt')

    def init_pool(self):
        signal.signal(signal.SIGINT, signal.SIG_IGN)

    def process_number(self, number: int):
        run_count = 0
        curr_num = number
        data_dict = {}
        intermediate_num_list = [number]

        while curr_num != 1:
            if curr_num % 2 == 0:
                curr_num /= 2
            else:
                curr_num = (3 * curr_num) + 1

            if run_count > 10e5:
                print(f'Run Count Exceeded -> Number: {self.format_e(Decimal(str(number)))}')
                sys.exit(0)

            run_count += 1
            # intermediate_num_list.append(int(curr_num))

        return True
        # return [number, intermediate_num_list]


    def format_e(self, n):
        a = '%E' % n
        return a.split('E')[0].rstrip('0').rstrip('.') + 'E' + a.split('E')[1]

    def serialize(self, f, content):
        for k,v in content.items():
            # write length of key, followed by key as string
            k_bstr = k.encode('utf-8')
            f.write(struct.pack('L', len(k_bstr)))
            f.write(k_bstr)
            # write length of value, followed by value in numpy.save format
            memfile = io.BytesIO()
            numpy.save(memfile, v)
            f.write(struct.pack('L', memfile.tell()))
            f.write(memfile.getvalue())

    def deserialize(self, f):
        retval = {}
        while True:
            content = f.read(struct.calcsize('L'))
            if not content: break
            k_len = struct.unpack('L', content)[0]
            k_bstr = f.read(k_len)
            k = k_bstr.decode('utf-8')
            v_len = struct.unpack('L', f.read(struct.calcsize('L')))[0]
            v_bytes = io.BytesIO(f.read(v_len))
            v = numpy.load(v_bytes)
            retval[k] = v
        return retval


if __name__ == '__main__':
    exe_obj = ThreeNPlusOne()
    avg_time_list = []

    start = time.time()

    control = -1
    list_size = 1000000
    auto_adjust = False

    if os.path.exists(exe_obj.logfile):
        with open(exe_obj.logfile, 'r', encoding='utf-8') as rf:
            line = rf.readline()
            try:
                val = int(line.replace('3n+1 count: ', ''))
            except:
                print('Log file value error. Program terminated.', file=sys.stderr)
            control = val

            print(f'3n+1 log file found. Calculation starting from {control}...')
            auto_adjust = True
    else:
        with open(exe_obj.logfile, 'w', encoding='utf-8') as wf:
            wf.write('3n+1 count: 1')
            print('New 3n+1 log file created.')
            control = 1

    # No reason to create the pool over and over again:
    with Pool(processes=4, initializer=exe_obj.init_pool) as p:
        try:
            while True:
                if control > 1000000 + 1:

                    # data_dict = {}
                    # for sublist in result: data_dict[sublist[0]] = sublist[1]
                    # data_dict = {str(key): data_dict[key] for key in sorted(data_dict.keys())}

                    # with gzip.open('3n+1_dataset.gz', 'wb') as gzip_file:
                    #     exe_obj.serialize(gzip_file, data_dict)

                    #     data_dict.clear()

                    with open(exe_obj.logfile, 'w', encoding='utf-8') as wf:
                        wf.write(f'3n+1 count: {control}')


                    avg_time_list.append(time.time() - start)
                    if len(avg_time_list) > 10000000:
                        avg_time_list.pop(0)


                    print(f'Count: {control - 1}, Time Spent: [{round(time.time() - start, 4)} seconds], Avg Time: [{round(sum(avg_time_list)/len(avg_time_list), 4)} seconds]')
                    start = time.time()

                value_n_list = [n for n in range(control, control + list_size)]
                result = p.map(exe_obj.process_number, value_n_list)
                control += list_size

        except KeyboardInterrupt:
            print('Ctrl-c entered -> Program terminated.')