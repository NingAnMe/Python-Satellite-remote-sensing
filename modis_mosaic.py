import argparse
import glob
import os
import warnings
from convertmodis_gdal import createMosaicGDAL, convertModisGDAL
warnings.filterwarnings('ignore')

parser = argparse.ArgumentParser()
parser.add_argument('--indir', help='输入文件夹', required=True)
parser.add_argument('--outfilename', help='输出文件的文件名: aaabbbccc', required=True)
args = parser.parse_args()

indir = args.indir
outfile = args.outfilename + '.hdf'

infiles = glob.glob(os.path.join(indir, '*.hdf'))
print(infiles)
mds = createMosaicGDAL(infiles, [1])
mds.run(outfile)

prefix = ''.join(outfile.split('.')[:-1])
mds = convertModisGDAL(outfile, prefix, [1], 0, outformat='GTiff', epsg=4326, resampl='BILINEAR')
mds.run()
