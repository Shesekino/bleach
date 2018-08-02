import pytz
import datetime
from dateutil import parser


LINE_TEMPLATE = "{title}\nopen for {days} days - owner is {user}"


def doFormat(data):
    return _listOfOldestRequests(data)


def _listOfOldestRequests(data, countOfOldest=5):
    assert type(data) == list
    sortedByDate = sorted(data, key=lambda record: record["createdAt"])
    recordsToKeep = sortedByDate[:countOfOldest]

    formattedData = []
    for record in recordsToKeep:
        daysAlive = _calculateDaysAlive(record["createdAt"])
        formattedLine = LINE_TEMPLATE.format(
            title=record["title"],
            days=daysAlive,
            user=record["user"]
        )
        formattedData.append(formattedLine)

    return "\n\n".join(formattedData)


def _calculateDaysAlive(stringOfDateFrom):
    now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
    dateFrom = parser.parse(stringOfDateFrom)

    return (now - dateFrom).days
