#!/usr/bin/env python
#
# WFF Interface Design
# Created By Nipun Jaswal
# Email : mail@nipunjaswal.info
# Statitics Required Variables
import os
from conf import notation
#===========================================
#Cap Infos
cap="capinfos "
#===========================================
#Current File Loaded	
#Capture File Stats
start_time="-a "+notation.pack_file
end_time="-e "+notation.pack_file
duration="-u "+notation.pack_file
nna="tshark -r "+notation.pack_file+" -R wlan.fc.type_subtype==0x04 -T fields -E separator=, wlan_mgt.ssid -e wlan.da -e | sort | uniq"

