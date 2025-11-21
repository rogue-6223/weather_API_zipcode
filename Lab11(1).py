import requests
import json

def main():
    with open("zips.txt","r") as f:
        data=f.read()

    lines=data.split("\n")
    zip_dict = {}
    for line in lines:
        parts = line.split(",")
        if len(parts)>= 9:
            postal = parts[1]
            lat=float(parts[7])
            lng=float(parts[8])
            zip_dict[postal]=(lat,lng)
    while True:
        zipcode=input("Enter a 5-digit zipcode: ")
        if len(zipcode)==5 and zipcode.isdigit():
            break
        print("Invalid input. Try again.")
    if zipcode in zip_dict:
        lat,lng=zip_dict[zipcode]
        print(f"Latitude: {lat}")
        print(f"Longitude: {lng}")
    else:
        print("Zipcode not found")
        return

    url = f"https://api.weather.gov/points/{lat},{lng}"
    response=requests.get(url)
    html_content=response.text
    print(html_content)
    myDict = json.loads(html_content)
    print(myDict)

if __name__ == "__main__":
    main()
