import os
import sys
import glob

import gdal


def get_range(infile):
    dataset = gdal.Open(infile)
    rows = dataset.RasterYSize
    cols = dataset.RasterXSize
    gtf = dataset.GetGeoTransform()
    x_min = gtf[0]
    y_max = gtf[3]
    x_max = gtf[0] + gtf[1] * rows
    y_min = gtf[3] + gtf[5] * cols
    return x_min, y_max, x_max, y_min


def get_extent(infiles):
    x_min, y_max, x_max, y_min = get_range(infiles[0])
    for infile in infiles[1:]:
        x_min_, y_max_, x_max_, y_min_ = get_range(infile)
        x_min = min(x_min, x_min_)
        y_max = max(y_max, y_max_)
        x_max = max(x_max, x_max_)
        y_min = min(y_min, y_min_)
    return x_min, y_max, x_max, y_min


def get_gtf(infile):
    return gdal.Open(infile).GetGeoTransform()


def get_project(infile):
    return gdal.Open(infile).GetProjection()


def get_row_col(gtf, x_min, y_max, x_max, y_min):
    row = int(x_max - x_min) / abs(gtf[5])
    col = int(y_max - y_min) / gtf[1]
    return int(row), int(col)


def get_new_gtf(gtf, y_min, y_max):
    gtf_new = list(gtf)
    gtf_new[0], gtf_new[3] = y_min, y_max
    return gtf_new


def mosaic_geotiff(infiles, outfile):
    x_min, y_max, x_max, y_min = get_extent(infiles)

    file_first = infiles[0]
    gtf = get_gtf(file_first)
    project = get_project(file_first)

    gtf_new = get_new_gtf(gtf, y_max, y_min)
    row, col = get_row_col(gtf, x_min, y_max, x_max, y_min)

    driver = gdal.GetDriverByName('gtiff')
    dataset_out = driver.Create(outfile, col, row)
    dataset_out.SetProjection(project)
    dataset_out.SetGeoTransform(gtf_new)

    band_out = dataset_out.GetRasterBand(1)

    for infile in infiles:
        dataset_in = gdal.Open(infile)
        trans = gdal.Transformer(dataset_in, dataset_out, [])
        success, xyz = trans.TransformPoint(False, 0, 0)
        print(success, xyz)
        x, y, z = map(int, xyz)
        data = dataset_in.GetRasterBand(1).ReadAsArray()
        print(data.shape)
        band_out.WriteArray(data, x, y)


if __name__ == "__main__":
    argv = sys.argv[1:]

    dir_in = argv[0]
    file_out = argv[1]
    print('DIR_IN: {}'.format(dir_in))
    print('FILE_OUT: {}'.format(file_out))

    infiles_ = glob.glob(os.path.join(dir_in, '*.tif'))
    map(print, infiles_)
    mosaic_geotiff(infiles_, file_out)
    print('>>> Outfile: {}'.format(file_out))
