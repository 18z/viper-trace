import os

def store_sample(file_object):
    sha256 = file_object.sha256

    folder = os.path.join('binaries', sha256[0], sha256[1], sha256[2], sha256[3])
    if not os.path.exists(folder):
        os.makedirs(folder, 0750)

    file_path = os.path.join(folder, sha256)

    if not os.path.exists(file_path):
        with open(file_path, 'wb') as stored:
            for chunk in file_object.get_chunks():
                stored.write(chunk)

    return file_path

def get_sample_path(sha256):
    path = os.path.join('binaries', sha256[0], sha256[1], sha256[2], sha256[3], sha256)
    if not os.path.exists(path):
        return None
    return path
