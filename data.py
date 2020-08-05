import tarfile

fname = "data/2016/AN_2016130.taz"
tar = tarfile.open(fname, "r:")
tar.extractall()
tar.close()