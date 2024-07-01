import http.client

conn = http.client.HTTPSConnection("open-ai-text-to-speech1.p.rapidapi.com")

payload = "{\"model\":\"tts-1\",\"input\":\"Today is a wonderful day\",\"voice\":\"alloy\"}"

headers = {
    'x-rapidapi-key': "66af666e5amsh95ff504da2fe721p1a83c1jsnf2e444edb4c5",
    'x-rapidapi-host': "open-ai-text-to-speech1.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("POST", "/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))