import tarfile

tar = tarfile.open("filename.tar.gz", "r:gz")
for member in tar.getmembers():
     f = tar.extractfile(member)
     if f is not None:
         content = f.read()