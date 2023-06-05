import time

import clipboard

if __name__ == '__main__':
    clipboard.copy("This is a sample Python script.")
    print("Copied to clipboard")
    print(clipboard.paste())

    print("Please copy something")

    time.sleep(10)

    print(f"You have copied to clipboard: {clipboard.paste()}")

