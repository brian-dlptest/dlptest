import requests

url = "https://dlptest.com/https-post/"

# 1. Prepare the files and data
try:
    with open('sensitive_data.txt', 'rb') as f:
        files = {'file_upload': f}
        data = {
            'test_message': 'Automated Test',
            'its_human': ''  # Keep this empty!
        }

        # 2. Add "Headers" to trick the firewall into thinking you are a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Referer': 'https://dlptest.com/https-post/',
            'Origin': 'https://dlptest.com'
        }

        # 3. Send the request
        response = requests.post(url, data=data, files=files, headers=headers)

        if response.status_code == 200:
            print("Success! The upload went through.")
        else:
            print(f"Still blocked. Status: {response.status_code}")
            print(f"Server Response: {response.text[:300]}") # Shows the error message

except FileNotFoundError:
    print("Error: Please create a file named 'sensitive_data.txt' in this folder first.")