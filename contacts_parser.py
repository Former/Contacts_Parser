# Copyright © 2024 Alexei Bezborodov. Contacts: <AlexeiBv+contact_xml@narod.ru>
# License: Public domain: http://unlicense.org/

import sys

def Contact_Parse(vnt_file):
    f = open(vnt_file, 'r')
    lines = f.readlines()
    f.close()

    str_vcard = ""
    n = "\n"
    vcard = False
    fn = ""
    index = 1
    for line in lines:
        if not vcard:
            start_s = "<vcard>"
            start = line.find(start_s)
            if start == -1:
                continue

            str_vcard = line[start + len(start_s):]# + n
            vcard = True
        else:
            stop_s = "</vcard>"
            stop = line.find(stop_s)
            if stop != -1:
                str_vcard += line[:stop]# + n
                file_name = fn.replace("/","")
                file_name = file_name.replace("\n","")
                f = open("out/" + str(index) + "." + file_name + ".vcf", 'w') #, encoding='utf-8')
                vcard = False
                f.write(str_vcard) # .encode('utf-8')
                f.close()
                index += 1
            else:
                fn_start = "FN;CHARSET=UTF-8:"
                fn_i = line.find(fn_start)
                if fn_i != -1:
                    fn = line[fn_i + len(fn_start):]
                str_vcard += line#  + n

files_to_decode = []

if __name__ == "__main__":
    for i in range(len(sys.argv)):
        param = sys.argv[i]
        if i > 0:
            files_to_decode.append(param)

for f in files_to_decode:
    Contact_Parse(f)
