import pathlib

from pydplace import DatasetWithSocieties


class Dataset(DatasetWithSocieties):
    dir = pathlib.Path(__file__).parent
    id = "dplace-dataset-sccs"
