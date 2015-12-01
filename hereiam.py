
import os,sys
print "os.path.abspath() = ", os.path.dirname(os.path.abspath(__file__))
print "os.getcwd() =       ", os.getcwd()

non_symbolic=os.path.realpath(sys.argv[0])
print "non_symbolic =      ", non_symbolic
program_filepath=os.path.join(sys.path[0], os.path.basename(non_symbolic))
print "program_filepath =  ", program_filepath