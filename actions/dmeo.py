import http.client

conn = http.client.HTTPSConnection("ai-vacation-planner.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "ai-vacation-planner.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("GET", "/vacationplan/paris/4/sightseeing,shopping,", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))