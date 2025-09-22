import requests


def main():
	response = requests.get("https://randomfox.ca/floof")

	if response.status_code == 200:
		fox_json = response.json()
		fox_url  = fox_json["image"]
		print("json:",fox_json)
		print("image url:",fox_url)
		
		pos = fox_url.rfind("/")
		suffix = fox_url[pos+1:]
		image_name = "fox"+suffix	
		print("image name:",image_name)

		image_data = requests.get(fox_url).content

		try:
			with open(image_name,"wb") as handler:
				handler.write(image_data)

			print(f"image saved as {image_name}")
		except Exception as e:
			print(f"error: {e}")



if __name__ == "__main__":
	main()
