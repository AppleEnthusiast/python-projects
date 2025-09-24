import requests
import json

def get_advice():
	url = "https://api.adviceslip.com/advice"
	try:
		response = requests.get(url,timeout=5)
		response.raise_for_status()
		try:
			data = response.json()
		except json.JSONDecodeError:
			return "error: server returned invalid json"

		advice = data.get("slip",{}).get("advice","no advice found")
		return advice
	except requests.exceptions.Timeout:
		return "error: request timed out"
	except requests.exceptions.HTTPError as e:
		return f"http error: {e}"
	except requests.exceptions.RequestException as e:
		return f"request error: {e}"


def main():
	hello_to = lambda name: f"Hello {name}!"
	print(hello_to("AppleEnthusiast"))
	advice = get_advice()
	print("here is your random advice:")
	print(advice)

if __name__ == "__main__":
	main()
