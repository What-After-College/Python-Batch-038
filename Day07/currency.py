import requests

url = "https://currencyapi.net/api/v1/rates?key=Y66FaaklzWWmyEV3n8ew7U10y90VLrXC6PBH"

def convertor(n):

    response = requests.get(url)
    inr = 0
    data = response.json()

    for x in data.keys():
        if x == 'rates':
            y = data[x]
            for i in y.keys():
                if i == 'INR':
                    inr = y[i]

    print("The amount when converted in INR is:",n*inr)
    return

if __name__ == "__main__":
    n = int(input("Enter the Amount in USD: "))
    convertor(n)