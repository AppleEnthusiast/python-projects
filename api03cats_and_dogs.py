import requests
import random


def get_cat():
	response = requests.get("https://api.thecatapi.com/v1/images/search")
	if response.status_code == 200:
		data = response.json()
		url = data[0]["url"]
		return url
	else:
		raise Exception("failed to fetch cat data")


def get_dog():
	response = requests.get("https://dog.ceo/api/breeds/image/random")
	if response.status_code == 200:
		data = response.json()
		url  = data["message"]
		return url
	else:
		raise Exception("failed to fetch dog data")

def download_image(url,filename):
	image_data = requests.get(url).content
	with open(filename,"wb") as handler:
		handler.write(image_data)
	print(f"image saved as {filename}")


def main():
	choice = random.choice(["cat","dog"])
	print(f"fetching {choice} image...")

	try:
		if choice == "cat":
			url = get_cat()
		else:
			url = get_dog()

		print("url:",url)

		pos = url.rfind("/")
		suffix = url[pos+1:]
		filename = f"{choice}_{suffix}"

		download_image(url,filename)

	except Exception as e:
		print(f"error: {e}")

if __name__ == "__main__":
	main()
