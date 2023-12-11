from zipfile import ZipFile

with ZipFile("metanit.zip", "a") as myzip:
    myzip.write("eggs.txt")
    myzip.write("serialized_data.pickle")