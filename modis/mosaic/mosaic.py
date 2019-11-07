#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 9:39
# @Author  : NingAnMe <ninganme@qq.com>
import os
import glob
from pymodis import convertmodis_gdal
"""
拼接所需的xml文件的下载地址：https://e4ftl01.cr.usgs.gov
"""

# ######################### 需要修改的参数 ###########################
indir = r"../sourceData"  # 存放原始数据的目录
outdir = r'../resultData'  # 存放结果数据的目录
# ##################################################################

if not os.path.isdir(outdir):
    os.makedirs(outdir)

# ######################### 生成HDF格式 ############################
infiles = glob.glob(os.path.join(indir, '*.hdf'))  # 获取sourceData目录下所有的原始数据文件
filename_first = os.path.basename(infiles[0])  # 获取原始数据的文件名
outfilename = '.'.join(filename_first.split('.')[:-2]) + '.hdf'  # 生成输出数据的文件名
outfile = os.path.join(outdir, outfilename)  # 生成输出数据的完整路径
bands = [1]  # 第几通道的数据
outformat = 'GTiff'  # 输出文件的格式，默认为HDF4，这里设置为GEOTiff
mds = convertmodis_gdal.createMosaicGDAL(infiles, bands, outformat=outformat)
mds.run(outfile)
print(">>>: {}".format(outfile))
