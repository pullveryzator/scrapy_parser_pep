from pathlib import Path

BASE_DIR = Path(__file__).parent
DATETIME_FOR_FILE_FORMAT = '%Y-%m-%dT%H-%M-%S'
EXPECTED_STATUS = [
    'Active',
    'Accepted',
    'Deferred',
    'Final',
    'Provisional',
    'Rejected',
    'Superseded',
    'Withdrawn',
    'Draft'
    ]
