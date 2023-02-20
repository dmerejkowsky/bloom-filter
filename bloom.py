from enum import Enum
import hashlib


class Algorithms(Enum):
    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA512 = "sha512"


def hash_input(input, algorithm):
    match algorithm:
        case Algorithms.SHA1:
            hasher = hashlib.sha1()
        case Algorithms.SHA256:
            hasher = hashlib.sha256()
        case Algorithms.SHA512:
            hasher = hashlib.sha512()
    hasher.update(input.encode("utf-8"))
    return hasher.digest()


def get_index(input, *, algorithm, max_index):
    hash = hash_input(input, algorithm)
    as_int = int.from_bytes(hash, byteorder="little")
    return as_int % max_index
