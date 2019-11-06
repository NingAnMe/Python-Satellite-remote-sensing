import glob
import os
import warnings
from convertmodis_gdal import createMosaicGDAL, convertModisGDAL
warnings.filterwarnings('ignore')
"""
修改tmp为存放数据的目录，可以是绝对路径，数据的命名方式必须是MODIS的原始命名方式
输出目录为result
"""
# ######################### 需要修改的参数 ###########################
indir = r"tmp"  # 存放原始文件的目录
outdir = r'result'  # 存放结果的目录
# ##################################################################

infiles = glob.glob(os.path.join(indir, '*.hdf'))
infiles_info = {}
for infile in infiles:
    print(infile)
    filename = os.path.basename(infile)
    flag = filename.split('.')[1]
    if flag not in infiles_info:
        infiles_info[flag] = list()
    infiles_info[flag].append(infile)

if not os.path.isdir(outdir):
    os.makedirs(outdir)

for flag in infiles_info:
    infiles = infiles_info[flag]
    outfile = str(flag) + '.hdf'
    outfile = os.path.join(outdir, outfile)

    mds = createMosaicGDAL(infiles, [1])
    mds.run(outfile)
    print(outfile)

    prefix = ''.join(outfile.split('.')[:-1])
    mds = convertModisGDAL(outfile, prefix, [1], 0, outformat='GTiff', epsg=4326, resampl='BILINEAR')
    mds.run()
    print(outfile.replace('hdf', 'tif'))
