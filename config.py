import os
from pathlib import Path

SLEEP_RATELIMIT_DURATION_RANGE = [
    10,
    15,
]  # range of time in seconds to sleep during ratelimit

ARBISCAN_API_KEY = ""  # API key from arbiscan
TARGET_TRANSFER_ADDRESS = ""  # 0x...
START_BLOCK = 175000000  # change to your value
END_BLOCK = 195500000  # change to your value. could be "latest"


# Current directory
CWD = Path(os.getcwd())
WRITE_TO_DIR = 'results/results.txt'
READ_FROM_DIR = 'inputs/wallets.txt'
