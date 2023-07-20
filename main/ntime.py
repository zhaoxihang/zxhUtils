from datetime import timezone
from utils.item import Item
from utils.timeTools import TimeTools


class NTime:
    @staticmethod
    def ntime(query):
        items = []
        try:
            if isinstance(query, int):
                utcDate = TimeTools.formatTimestamp(query, fmt="%Y-%m-%d %H:%M:%S", tz=timezone.utc)
                items.append(Item.create_item(utcDate, 'UTC date', {'type': 'default', 'path': 'icon.png'},
                                              utcDate))
                localDate = TimeTools.formatTimestamp(query)
                items.append(Item.create_item(localDate, 'Local date', {'type': 'default', 'path': 'icon.png'},
                                              localDate))
            elif isinstance(query, str):
                utcInt = TimeTools.timeStamp(query, timezone.utc)
                items.append(Item.create_item(utcInt, 'utc time', {'type': 'default', 'path': 'icon.png'},
                                              utcInt))
                localInt = TimeTools.timeStamp(query)
                items.append(Item.create_item(localInt, 'Local time', {'type': 'default', 'path': 'icon.png'},
                                              localInt))
            else:
                items.append(
                    Item.create_item('类型错误', '类型错误',
                                     {'type': 'default', 'path': 'icon.png'},
                                     ''))

            return items
        except ValueError:
            items.append(
                Item.create_item('Invalid input', 'Please enter a valid Unix timestamp',
                                 {'type': 'default', 'path': 'icon.png'},
                                 ''))
            return items
