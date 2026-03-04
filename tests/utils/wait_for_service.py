import time
import sys
import requests


def wait_for_service(url: str, timeout: int = 40):
    for i in range(timeout):
        try:
            r = requests.get(url, timeout=2)
            print("health:", r.status_code, r.text)

            if r.status_code == 200:
                return True

        except Exception as e:
            print("waiting...", e)

        time.sleep(1)

    return False


if __name__ == "__main__":
    url = sys.argv[1]

    if not wait_for_service(url):
        raise SystemExit("Service did not become healthy")