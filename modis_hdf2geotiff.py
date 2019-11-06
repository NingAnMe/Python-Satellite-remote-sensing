import argparse
from pymodis import convertmodis_gdal

parser = argparse.ArgumentParser()
parser.add_argument('--infile', help='输入文件', required=True)
# parser.add_argument('--prefix', help='输出文件的前缀', required=True)
args = parser.parse_args()

mds = convertmodis_gdal.convertModisGDAL(
    args.infile, args.infile, [1], 0, outformat='GTiff',
    epsg=4326, wkt=None, resampl='BILINEAR', vrt=False)
mds.run()
