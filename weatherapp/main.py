
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()

    def search_location(self, API_KEY=""):
        search_url = f'https://api.openweathermap.org/data/2.5/weather?q={self.search_input.text}&units=imperial&appid={API_KEY}'
        UrlRequest(search_url, on_success=self.found_location, on_error=self.fail, on_failure=self.fail)
        # print(f'The user searched for {search_url}')

    def found_location(self, request, data):
        forecast = [{'text': f'{k}: {v}'} for k, v in data['main'].items()]
        self.search_results.data = forecast

    def fail(self, request, data):
        print(f'Fail: {request}, {data}')


class RV(RecycleView):
    pass


class WeatherApp(App):
    pass


if __name__ == '__main__':
    WeatherApp().run()


