class Item:
    @staticmethod
    def create_item(title, subtitle, icon, arg):
        item = {'title': title, 'subtitle': subtitle, 'icon': icon, 'arg': arg}
        return item
