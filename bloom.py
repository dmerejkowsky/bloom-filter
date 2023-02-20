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


class Filter:
    def __init__(self, max_index):
        self.max_index = max_index
        self.indexes = set()

    def add(self, word):
        """Add a word to the table.

        Note: this mutates self.indexes - which means I'm not sure we can
        call add() several times before calling test - the spec does not
        explicitely say - but the drawing seems to indicate that calling add()
        for is fine
        """
        self.indexes.update(self._get_indexes(word))

    def test(self, word):
        indexes = set(self._get_indexes(word))
        return indexes.issubset(self.indexes)

    def _get_indexes(self, word):
        """Returns an iterotar for all the indexes of the given word,
        one per algorithm in the Algorithms enum
        """
        return (
            get_index(word, algorithm=algorithm, max_index=self.max_index)
            for algorithm in Algorithms
        )

    def __repr__(self):
        return f"Filter<{self.indexes}>"
