import time
import random
import requests
from typing import Self
from loguru import logger
from eth_typing import ChecksumAddress
from config import (
    SLEEP_RATELIMIT_DURATION_RANGE,
    ARBISCAN_API_KEY,
    TARGET_TRANSFER_ADDRESS,
)


class TransferChecker:
    def __init__(self, address: str | ChecksumAddress) -> Self:
        self.address = address

    def find_transfer(
        self, start_block: int, end_block: int
    ) -> str | ChecksumAddress | None:
        logger.info(f"{self.address} - Getting transaction history...")

        datas = []
        for i in range(1, 6):
            url = f"https://api.arbiscan.io/api?module=account&action=txlist&address={self.address.lower()}&startblock={start_block}&endblock={end_block}&page={i}&offset=10&sort=asc&apikey={ARBISCAN_API_KEY}"
            while True:
                try:
                    response = requests.get(url)
                    data = response.json()
                    if data:
                        datas.extend(data["result"])
                    break
                except Exception as e:
                    logger.warning(
                        f"{self.address} - Most likely caught a ratelimit, sleeping..."
                    )
                    logger.error(str(e))
                    time.sleep(random.randint(*SLEEP_RATELIMIT_DURATION_RANGE))

        if datas:
            for item in datas:
                if TARGET_TRANSFER_ADDRESS[2:].lower() in item["input"]:
                    logger.success(
                        f"{self.address} - Was using this address in transfer!"
                    )
                    return self.address
            logger.info(f"{self.address} - Was not using this address in transfer.")
            return
