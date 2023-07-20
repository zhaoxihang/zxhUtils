import sys
import json
from main.ntime import NTime

search_query = sys.argv[1]


class Script:
    fun = ""

    def __init__(self, str_fun):
        self.fun = str_fun

    @staticmethod
    def ntime(query):
        try:
            query = int(query)
        except ValueError:
            query = query
        return NTime.ntime(query)


if __name__ == "__main__":
    funStr, param = search_query.lstrip().split(' ', 1)
    controller = Script(funStr)
    result = {'items': getattr(controller, controller.fun)(param)}
    json.dump(result, sys.stdout)
    sys.stdout.flush()
