#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 9:39
# @Author  : NingAnMe <ninganme@qq.com>
import os
from pymodis import convertmodis_gdal

indir = '../sourceData'  # 输入文件的所在文件夹
filename = 'MCD19A2.A2019001.h26v03.006.2019009051509.hdf'  # 输入文件的文件名
infile = os.path.join(indir, filename)  # 输入数据的完整路径
prefix = os.path.splitext(filename)[0]  # 输出文件名的前缀
bands = [1]  # 选取的通道，这里只选了一个，选取多个[1, 1, 1, 1]
resolution = 0.01  # 单位是degree
outformat = 'GTiff'  # 输出格式，可以是gdal模块支持的所有格式
epsg = 4326  # 重投影方式，投影方式可以在https://spatialreference.org/ref/epsg/查，4326是等经纬
resampl = 'BILINEAR'

mds = convertmodis_gdal.convertModisGDAL(
    infile, prefix, bands, resolution, outformat=outformat, epsg=epsg, resampl=resampl)
mds.run()
