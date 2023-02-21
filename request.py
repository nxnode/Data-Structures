import requests


def echo():
    response = requests.post("http://localhost:5000/echo", json={"a": "b"})
    return response.text


if __name__ == "__main__":
    # print(requests.get("http://localhost:5000/abc").text)
    print(echo())
