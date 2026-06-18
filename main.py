from datetime import datetime
import heapq

notifications = [
    {
        "ID": "1",
        "Type": "Placement",
        "Message": "CSX Corporation hiring",
        "Timestamp": "2026-04-22 17:51:18"
    },
    {
        "ID": "2",
        "Type": "Result",
        "Message": "Mid-sem results released",
        "Timestamp": "2026-04-22 17:51:30"
    },
    {
        "ID": "3",
        "Type": "Event",
        "Message": "Farewell event",
        "Timestamp": "2026-04-22 17:51:06"
    }
]

weights = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}

for n in notifications:
    timestamp = datetime.strptime(
        n["Timestamp"],
        "%Y-%m-%d %H:%M:%S"
    )
    n["priority"] = (
        weights[n["Type"]],
        timestamp
    )

top10 = heapq.nlargest(
    10,
    notifications,
    key=lambda x: x["priority"]
)

print("Top Notifications")
for n in top10:
    print(
        n["Type"],
        "-",
        n["Message"]
    )