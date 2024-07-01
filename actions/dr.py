import http.client

conn = http.client.HTTPSConnection("chatgpt-42.p.rapidapi.com")

payload = "{\"messages\":[{\"role\":\"user\",\"content\":\"What is AI?\"}],\"system_prompt\":\"\",\"temperature\":0.9,\"top_k\":5,\"top_p\":0.9,\"image\":\"\",\"max_tokens\":256}"

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "chatgpt-42.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("POST", "/matag2", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))