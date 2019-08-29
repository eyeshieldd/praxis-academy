from injector import Module
from injector import Injector, inject

class Api:
    def fetch_remote_data(self):
        print('Api called')
        return 76

class BusinessLogic:
    def __init__(self, api: Api):
        self.api = api

    def do_stuff(self):
        api_result = self.api.fetch_remote_data()
        print(f'the api returned a result: {api_result}')

class TestApi(Api):
    def fetch_remote_data(self):
        print('Demo Api called')
        return 24

class AppModule(Module):

     @singleton
     @provider
     def provide_business_logic(self, api:Api) -> BusinessLogic:
        return BusinessLogic(api=api)

     @singleton
     @provider
     def provide_api(self) -> Api:
        # there is no complex logic in our case,
        # but you can use this method to hide the complexity of initial 
        configuration
        # e.g. when instantiating a particular DB connector.
        return Api()

class TestAppModule(Module):

     @singleton
     @provider
     def provide_api(self) -> Api:
        return TestApi()

if __name__ == '__main__':
    real_injector = Injector(AppModule())
    test_injector = Injector([AppModule(), TestAppModule()])

    real_logic = real_injector.get(BusinessLogic)
    real_logic.do_stuff()

    test_logic = test_injector.get(BusinessLogic)
    test_logic.do_stuff()