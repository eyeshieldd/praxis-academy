class Api:
    def fetch_remote_data(self):
        print('Api called')
        return 42


class BusinessLogic:
    def __init__(self, api: Api):
        self.api = api

    def do_stuff(self):
        api_result = self.api.fetch_remote_data()
        print(f'the api returned a result: {api_result}')
        # do something with the data and return a result

# ---

if __name__ == '__main__':
    api = Api()
    logic = BusinessLogic(api=api)

    # ...
    print(logic.do_stuff())