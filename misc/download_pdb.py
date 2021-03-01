# Use PDB ID to download PDB files
# Authored by Chris Swain (http://www.macinchem.org)
# Copyright CC-BY

import csv
import os
import sys

# Python 2 and 3 compatibility
if sys.version_info[0] == 2:
    from urllib import urlrelative
else:
    from urllib.request import urlretrieve

# You may want to edit these parameters

# File containing comma-separated list of the desired PDB IDs
pdb_codes_file = 'pdbcodes.csv'

# Folder to download files to
download_folder = 'PDB/'

# Whenther to download gzip compressed files
compressed = True

# Read the PDB IDs from the input file
with open(pdb_codes_file) as f:
    # Change to .split('\n') if PDB IDs are 1 per line
    pdb_codes = f.read().split(',')

# Alternatively, hard code PDB IDs:
# pdb_codes = ['1LS6', '1Z28', '2D06', '3QVU', '3QVV', '3U3J', '3U3K']

#For testing
#print(pdb_codes)

# Ensure download folder exists
try:
    os.makedirs(download_folder)
except OSError as e:
    # Ignore OSError is it already exists
    pass

for pdb_code in pdb_codes:
    # Add .pdb extension and remove ':1' suffilx in entities
    filename = '%s.pdb' % pdb_code[:4]
    # Add .gz extenison is compressed
    if compressed:
        filename = '%s.gz' % filename
    url = 'https://files.rcsb.org/download/%s' % filename
    destination_file = os.path.join(download_folder, filename)
    # Download the file
    urlretrieve(url, destination_file)
