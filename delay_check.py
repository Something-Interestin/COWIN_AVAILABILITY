import time
import sys
import os

# to check for - available_capacity_dose1
# delay can be any time interval after which we want to recheck

delay = sys.argv[1]
check_for = sys.argv[2]
date = sys.argv[3]

while True:
    os.system("bash get_data.sh {} {}".format(check_for,date))
    print("Waiting")
    time.sleep(int(delay))
