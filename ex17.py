from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file)
#print(">>> in_file=", repr(in_file))
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file,'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()


#先创建一个test.txt，
# PS C:\Users\miran\lpthw> echo "This is a test file." > test.txt                 #echo指令创建文件:在test.txt中输入写入一句话
# PS C:\Users\miran\lpthw> cat test.txt                                           #cat指令显示文件内容，查看这个文件，cat是concatenate拼接
# This is a test file.
# PS C:\Users\miran\lpthw> python ex17.py test.txt new_file.txt                   #输入python A.py B.txt(已创建) C.txt(可以未创建)
# Copying from test.txt to new_file.txt
# The input file is 46 bytes long
# Does the output file exist? False
# Ready, hit RETURN to continue, CTRL-C to abort.
#
# Alright, all done.
# PS C:\Users\miran\lpthw>
