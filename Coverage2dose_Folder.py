#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This code combine counts from feature counts
"""

from sys import argv
import glob
import os

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value
# auto

def cover2dose (cover) :
    "As name"
    out = 0
    if cover > 1 and cover <3 :
        out = 1
    elif cover >= 3 :
        out = 2
    return (out)

def main():
    script, working_dir, data_out = argv
    out_stream = open(data_out, 'w')
    list_f = glob.glob(os.path.join(working_dir, '*cover.txt'))
    file_out_list = []
    site_list = []
    data_dict = AutoVivification()
    for file_in in sorted(list_f):
        dir2, file_short = os.path.split(file_in)
        if file_short[0].isdigit():
            file_short = 'S'+file_short
        file_short = file_short[0:-10] # remove the suffix
        file_out_list.append(file_short)
        with open(file_in, 'r') as in_stream:
            for line in in_stream:
                line_record = line.rstrip().split("\t")
                site_id = ':'.join(line_record[0:3])
                if len(file_out_list) <= 1:
                    site_list.append(site_id)
                count = int(line_record[3])
                dose = cover2dose(count)
                data_dict[site_id][file_short] = str(dose)
    # get the output
    for site_id in site_list :
        out_line = [site_id,'.','.']
        check_cover = AutoVivification()
        for file_id in file_out_list :
            out_c = 'NA'
            if file_id in data_dict[site_id].keys():
                out_c = data_dict[site_id][file_id]
            check_cover[out_c] = 1
            out_line.append(out_c)
        if len(check_cover.keys()) > 1:
            out_stream.write("\t".join(out_line) + "\n")
    out_stream.close()
    data_out2= 'SampleList_' + data_out
    out_stream2 = open(data_out2, 'w')
    out_stream2.write("\n".join(file_out_list))
    out_stream2.close()

## Author : lxue@uga.edu

if __name__ == '__main__':
    main()


