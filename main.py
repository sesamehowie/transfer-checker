import os
from checker import TransferChecker
from pathlib import Path
from config import CWD, READ_FROM_DIR, WRITE_TO_DIR


def write_txt(new_filename: Path | str, data_list: list | tuple) -> bool | None:
    with open(new_filename, "w") as file:
        for item in data_list:
            file.write(item + "\n")
        return


def read_txt(filename: Path | str) -> list | tuple:
    with open(filename, "r") as file:
        data_list = file.read().splitlines()

    return data_list


def main():
    results = []
    wallet_addresses = read_txt(filename=os.path.join(CWD, Path(READ_FROM_DIR)))

    for wallet in wallet_addresses:
        checker = TransferChecker(address=wallet)
        res = checker.find_transfer()
        if res is not None:
            results.append(wallet)

    if results:
        write_txt(
            new_filename=os.path.join(CWD, Path(WRITE_TO_DIR)),
            data_list=results,
        )


if __name__ == "__main__":
    main()
