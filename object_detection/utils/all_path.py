import pathlib
from dataclasses import dataclass
from dataclasses import field


@dataclass
class AllPath:
    """Class for keeping track of an item in inventory."""
    _DATA_BASE_DIR:pathlib.Path = pathlib.Path('raw_data')
    _DATA_ANOTATIONs:pathlib.Path  = _DATA_BASE_DIR / 'Annotations' / 'Annotations'
    DATA_ANOTATIONs_DAY_TRAIN:pathlib.Path = _DATA_ANOTATIONs / 'dayTrain'
    DATA_ANOTATIONs_NIGHT_TRAIN:pathlib.Path = _DATA_ANOTATIONs / 'nightTrain'
    DATA_FILE_LOCATION_DAY_TRAIN:pathlib.Path = _DATA_BASE_DIR / 'dayTrain' / 'dayTrain'
    DATA_FILE_LOCATION_NIGHT_TRAIN:pathlib.Path = _DATA_BASE_DIR / 'nightTrain' / 'nightTrain'
    


if __name__ == 'main':
    print(AllPath())
