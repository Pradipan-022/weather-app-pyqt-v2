import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QMessageBox
)

from weather_app.backend.weather_backend import get_current_weather
from weather_app.ui.historical_tab import HistoricalTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Weather Data Visulization")
        self.setGeometry(510, 240, 900, 600)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(12)
        central_widget.setLayout(main_layout)
        
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter City Name")
        self.city_input.setFixedWidth(300)
        main_layout.addWidget(self.city_input, alignment=Qt.AlignCenter)
        
        self.search_button =QPushButton("Search")
        self.search_button.setFixedWidth(120)
        self.search_button.clicked.connect(self.search_weather)
        main_layout.addWidget(self.search_button, alignment=Qt.AlignCenter)
        
        self.city_label = QLabel("City: --")
        self.city_label.setObjectName("cityLabel")

        self.temp_label = QLabel("Temperature: -- °C")
        self.temp_label.setObjectName("tempLabel")

        self.humidity_label = QLabel("Humidity: -- %")
        self.humidity_label.setObjectName("humidityLabel")

        self.pressure_label = QLabel("Pressure: -- hPa")
        self.pressure_label.setObjectName("pressureLabel")

        self.wind_label = QLabel("Wind Speed: -- km/h")
        self.wind_label.setObjectName("windLabel")

        self.condition_label = QLabel("Condition: --")
        self.condition_label.setObjectName("conditionLabel")

        
        weather_labels = [
            self.city_label,
            self.temp_label,
            self.humidity_label,
            self.pressure_label,
            self.wind_label,
            self.condition_label
        ]
        
        for label in weather_labels:
            label.setAlignment(Qt.AlignCenter)
            main_layout.addWidget(label)
        
        self.historical_button = QPushButton("View Historical Data")
        self.historical_button.setFixedWidth(200)
        self.historical_button.clicked.connect(self.open_historical_tab)
        main_layout.addWidget(self.historical_button, alignment=Qt.AlignCenter)
        
        self.search_button.setObjectName("searchButton")
        self.historical_button.setObjectName("historicalButton")
        
    def search_weather(self):
        city = self.city_input.text().strip().lower().title()
        
        if not city:
            QMessageBox.warning(self, "Input Error", "Please enter a city name.")
            return
        
        try:
            df = get_current_weather(city)
            
            if df.empty:
                raise ValueError("No Data returned")
            
            self.city = city
            self.update_weather_ui(df)
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to fetch weather data. \n\n{str(e)}"
            )
    
    def update_weather_ui(self, df):
        self.city_label.setText(f"City: {df.loc[0, 'city']}")
        self.temp_label.setText(f"Temperature: {df.loc[0, 'temperature']} °C")
        self.humidity_label.setText(f"Humidity: {df.loc[0, 'humidity']} %")
        self.pressure_label.setText(f"Pressure: {df.loc[0, 'pressure']} hPa")
        self.wind_label.setText(f"Wind Speed: {df.loc[0, 'wind_speed']} km/h")
        self.condition_label.setText(f"Condition: {df.loc[0, 'description']}")
        
    def open_historical_tab(self):
        if not hasattr(self, "city"):
            QMessageBox.warning(
                self, "No City Selected", "Please search for a city first."
            )
            return
        
        self.history_window = HistoricalTab(self.city, parent=self)
        self.history_window.show()
        self.hide()
    
