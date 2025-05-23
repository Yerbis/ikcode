import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout)

from PyQt5.QtCore import Qt



class IKweather(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)
        self.symbol_label = QLabel(self)
        self.desc_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('IKweather Weather App -- IKcode')

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.symbol_label)
        vbox.addWidget(self.desc_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.symbol_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temp_label.setObjectName("temp_label")
        self.symbol_label.setObjectName("symbol_label")
        self.desc_label.setObjectName("desc_label")

        self.setFixedWidth(350)
        # Ensure both QLineEdit and QPushButton have the same fixed width

        # Make QPushButton expand to match QLineEdit width using layout stretch
        self.city_input.setMinimumWidth(0)
        self.get_weather_button.setMinimumWidth(0)
        self.city_input.setSizePolicy(self.city_input.sizePolicy().horizontalPolicy(), self.city_input.sizePolicy().verticalPolicy())
        self.get_weather_button.setSizePolicy(self.city_input.sizePolicy().horizontalPolicy(), self.get_weather_button.sizePolicy().verticalPolicy())

        # Style for the whole widget except temp_label
        self.setStyleSheet("""
            QWidget {
            background-color: #1a7689;
            font-family: Verdana;
            color: white;
            }
            QLabel#city_label, QLabel#desc_label {
            color: white;
            font-size: 20px;
            }
            QLabel#symbol_label {
            color: white;
            font-size: 48px;
            font-family: Segoe UI Emoji;
            }
            QLineEdit#city_input {
            background-color: #145c6b;
            color: white;
            border: 2px solid #ffcc00;
            border-radius: 6px;
            padding: 8px;
            font-size: 16px;
            min-width: 0px;
            margin-left: auto;
            margin-right: auto;
            }
            QPushButton#get_weather_button {
            background-color: #145c6b;
            color: white;
            border: 2px solid #ffcc00;
            border-radius: 6px;
            padding: 10px 20px;
            font-size: 16px;
            min-width: 0px;
            margin-left: auto;
            margin-right: auto;
            }
            QPushButton#get_weather_button:hover {
            background-color: #ffcc00;
            color: #145c6b;
            }
        """)
        # Separate style for temp_label
        self.temp_label.setStyleSheet("""
            color: white;
            font-size: 32px;
            font-weight: bold;
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        
        api_key = "3ff2ef14e298dbc9ff3b69629883307a"
        city = self.city_input.text()

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease Check your request")
                    self.symbol_label.setText("❌")
                    self.desc_label.setText("No info")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                    self.symbol_label.setText("❌")
                    self.desc_label.setText("No info")
                case 403:
                    self.display_error("Access Error:\nAccess Denied")
                    self.symbol_label.setText("❌")
                    self.desc_label.setText("No info")
                case 404:
                    self.display_error(f"Not found:\nThe city '{city}' was not found")
                    self.symbol_label.setText("❌")
                    self.desc_label.setText("No info")
                case 500:
                    self.display_error("Internal Server Error:\nNot available; Please try again later")
                    self.symbol_label.setText("❌")
                    self.desc_label.setText("No info")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                    self.symbol_label.setText("❌")
                    self.desc_label.setText("No info")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                    self.symbol_label.setText("❌")
                    self.desc_label.setText("No info")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                    self.symbol_label.setText("❌")
                    self.desc_label.setText("No info")
                case _:
                    self.display_error(f"HTTP Error:\n{http_error}")
                    self.symbol_label.setText("❌")
                    self.desc_label.setText("No info")
        
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
            self.symbol_label.setText("❌")
            self.desc_label.setText("No info")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
            self.symbol_label.setText("❌")
            self.desc_label.setText("No info")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects:\n Check the URL")
            self.symbol_label.setText("❌")
            self.desc_label.setText("No info")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")
            self.symbol_label.setText("❌")
            self.desc_label.setText("No info")


    def display_error(self, message):
        self.temp_label.setStyleSheet("font-size: 15px")
        self.temp_label.setText(message)

    def display_weather(self, data):
        self.temp_label.setStyleSheet("font-size: 32px")
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15
        temp_f = (temp_k * 9/5) - 459.67
        weather_id = data["weather"][0]["id"]
        weather_desc = data["weather"][0]["description"]


        self.temp_label.setText(f"{temp_f:.0f}°F")
        #self.temp_label.setText(f"{temp_c}°C")
        #self.temp_label.setText(f"{temp_k}°K")
        self.symbol_label.setText(self.get_symbol(weather_id))
        self.desc_label.setText(weather_desc)

    @staticmethod
    def get_symbol(weather_id):
        
        if 200 <= weather_id <= 232:
           return "⛈️" 
        elif 300 <= weather_id <= 321:
            return "⛅"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return "❌"



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ikweather = IKweather()
    ikweather.setWindowTitle('IKweather')
    ikweather.show()
    sys.exit(app.exec_())