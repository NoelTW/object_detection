import pathlib
from dataclasses import dataclass


@dataclass
class AllPath:
    """Class for keeping track of an item in inventory."""
    _DATA_BASE_DIR:pathlib.Path = pathlib.Path('dataset')
    _DATA_ANOTATIONs:pathlib.Path  = _DATA_BASE_DIR / 'Annotations' / 'Annotations'
    DATA_ANOTATIONs_DAY_TRAIN:pathlib.Path = _DATA_ANOTATIONs / 'dayTrain'
    DATA_ANOTATIONs_NIGHT_TRAIN:pathlib.Path = _DATA_ANOTATIONs / 'nightTrain'
    DATA_FILE_LOCATION_DAY_TRAIN:pathlib.Path = _DATA_BASE_DIR / 'dayTrain' / 'dayTrain'
    DATA_FILE_LOCATION_NIGHT_TRAIN:pathlib.Path = _DATA_BASE_DIR / 'nightTrain' / 'nightTrain'

