"""Stuff used for more than one day"""

import json
from pathlib import Path
from binascii import unhexlify
import requests as rq
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def load_user_data():
    """Read the user specific data from file"""
    with open("userdata.json", "r", encoding="utf-8") as f:
        user_data = json.load(f)

    # Get seed from API, seed is constant for account so can be written to file
    if "seed" not in user_data:
        cookies = user_data
        r = rq.get("https://everybody.codes/api/user/me", cookies=cookies, timeout=5)
        user_data["seed"] = r.json()["seed"]

        with open("userdata.json", "w", encoding="utf-8") as f:
            json.dump(user_data, f)

    return user_data


def decrypt_aes(key: str, encrypted_hex: str) -> str:
    """
    Decrypt AES/CBC/PKCS5Padding ciphertext, IV = first 16 bytes of key
    """
    encrypted_bytes = unhexlify(encrypted_hex)

    key_bytes = key.encode("utf-8")
    iv = key[:16].encode("utf-8")

    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)

    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    unpadded = unpad(decrypted_bytes, AES.block_size)

    return unpadded.decode("utf-8")


def get_input(year: int, day: int):
    """Get the input data for given year and day"""
    user_data = load_user_data()
    cookies = {"everybody-codes": user_data["everybody-codes"]}
    base_url = "https://everybody-codes.b-cdn.net/assets"

    # Get the coded input notes
    r = rq.get(
        f"{base_url}/{year}/{day}/input/{user_data['seed']}.json",
        cookies=cookies,
        timeout=5,
    )
    notes = r.json()

    # Get the AES Key
    r = rq.get(
        f"https://everybody.codes/api/event/{year}/quest/{day}",
        cookies=cookies,
        timeout=5,
    )
    aes_keys = r.json()

    # Decoding
    input_dict = {}
    for number, note in notes.items():
        try:
            plaintext = decrypt_aes(aes_keys[f"key{number}"], note)
            input_dict[number] = plaintext
        except KeyError:
            break

    return input_dict


def load_input(year: int, day: int, number: int, reload: bool = False):
    """Load Input form File or Get from Web and save to File"""
    file_path = Path(f"{year}/inputs/{day:02d}_{number}.txt")
    try:
        if reload or not file_path.exists():
            input_dict = get_input(year, day)
            input_str = input_dict[str(number)]
            file_path.write_text(input_str, "utf-8")
        else:
            input_str = file_path.read_text("utf-8")
        return input_str
    except KeyError:
        print("Do previous quest first")
        return "Do previous quest first"


if __name__ == "__main__":
    print(load_input(2024, 1, 1))
