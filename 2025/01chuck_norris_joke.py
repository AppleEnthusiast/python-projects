import requests

def get_joke():
    url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            joke = data["value"]
            return joke

    except Exception as e:
        print(f"error: {e}")


def main():
    joke = get_joke()
    print("here is your joke:\n",joke)


if __name__ == "__main__":
    main()
