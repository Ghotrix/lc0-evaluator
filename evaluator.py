import glob
import re


weight_files = glob.glob('*.txt.gz')

weights = sorted([int(re.search('(.*)_(\d*)\.txt\.gz', file).group(2)) for file in weight_files])

print(weights)
