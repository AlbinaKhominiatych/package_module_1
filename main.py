#приклад сиснення інформації
import gzip
with gzip.open('compressed_file.gz', "wb") as file:
    file.write(b"some text")
#ще один із видів стискання
data = b"some text"
compressed_data = gzip.compress(data)
print(compressed_data)
#розпакування стиснених данних
decompressed_data = gzip.decompress(compressed_data)
print(decompressed_data)
#розпакування і файлу
with gzip.open('compressed_file.gz', "rb") as file:
    new_data = file.read()
print(new_data)