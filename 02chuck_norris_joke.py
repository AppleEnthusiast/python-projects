import requests
import json


def get_joke():
	url = "https://api.chucknorris.io/jokes/random"

	try:
		response = requests.get(url,timeout=5)
		response.raise_for_status()
		try:
			data = response.json()
		except json.JSONDecodeError:
			return "error: server returned invalid json"
		joke = data.get("value","joke was not found")
		return joke
	except requests.exceptions.Timeout:
		return f"request timed out"
	except requests.exceptions.HTTPError as e:
		return f"http error: {e}"
	except requests.exceptions.RequestException as e:
		return f"request error: {e}"


def main():
	joke = get_joke()
	print("here is your joke:")
	print(joke)


if __name__ == "__main__":
	main()




