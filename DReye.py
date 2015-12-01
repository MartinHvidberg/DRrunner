# Running Data Reviewer, via ArcPy
# This .py file is just eye'ing into a .gdb file

import os
import sys
import DRrunner_reporter

if __name__ == "__main__":
    
    # *** Init
    
    print "DReye : Init phase Begin ..."    
    # Set reviewer workspace
    reviewer_db = r"C:\Martin\Work\DR_runner_10_3_GR96.gdb"   
    if not os.path.exists(reviewer_db):
        print "!!! Can't find reviewer_db: "+reviewer_db
        sys.exit(101) 
        
    # *** eye into the .gdb ...
    
    print "DReye : Eye'ing phase Begin ..."  
    DRrunner_reporter.eye(reviewer_db)
    print "DReye : Eye'ing phase End ..."

# Music that accompanied the coding of this script:
#    C.V. Joergensen - Tidens tern
