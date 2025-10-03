import requests

def main():
	response = requests.get("http://randomfox.ca/floof")
	print("status code:",response.status_code)
	print("raw text:")
	print(response.text)
	print("json:")
	print(response.json())
	fox_url = response.json()["image"]
	print("image url:")
	print(fox_url)


if __name__ == "__main__":
	main()
