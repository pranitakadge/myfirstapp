import requests
r = requests.get("http://mobilelistings.tvguide.com/Listingsweb/ws/rest/schedules/80004.null/start/1517214600/duration/1440?ChannelFields=Name&ScheduleFields=ProgramId%2CEndTime%2CStartTime%2CTitle%2C&formattype=json")
data = r.json()
print(data)

channel = data[0]['Channel']
# program = [i[1]['ProgramSchedules'] for i in data ]

print(channel)
# print(program)

# for x in data:
#     print(data[x]['ProgramSchedules'])



