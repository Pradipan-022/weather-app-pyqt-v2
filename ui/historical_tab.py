import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QMessageBox
)
from weather_app.visulization.plots import (
    plot_avg_temp_trend,
    plot_temp_range,
    plot_humidity_trend,
    plot_precipitation,
    plot_max_wind,
    plot_condition_counts,
    plot_temp_vs_humidity,
    plot_uv_trend
)

class HistoricalTab(QWidget):
    def __init__(self, city, parent=None):
        super().__init__()
        self.city = city
        self.parent_window = parent
        self.selected_plot = None
        
        self.setWindowTitle("Historical Weather Data")
        self.setGeometry(510, 240, 900, 600)
        
        self.load_styles()
        
        self.init_ui()
        
    def init_ui(self):
        main_layout = QVBoxLayout()

        top_layout = QHBoxLayout()

        back_btn = QPushButton("← Back")
        back_btn.setObjectName("backButton")
        back_btn.clicked.connect(self.go_back)

        title = QLabel("Historical Weather Data (Last 7 Days)")
        title.setObjectName("historyTitle")
        title.setAlignment(Qt.AlignCenter)


        top_layout.addWidget(back_btn)
        top_layout.addStretch()
        top_layout.addWidget(title)
        top_layout.addStretch()

        main_layout.addLayout(top_layout)

        self.description_label = QLabel("Select a weather parameter to visualize.")
        self.description_label.setObjectName("descriptionLabel")
        self.description_label.setWordWrap(True)
        self.description_label.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(self.description_label)

        options_layout = QVBoxLayout()

        buttons = [
            ("Average Temperature Trend", self.select_avg_temp),
            ("Min/Max Temperature Range", self.select_temp_range),
            ("Humidity Trend", self.select_humidity),
            ("Precipitation", self.select_precipitation),
            ("Max Wind Speed", self.select_wind),
            ("Weather Condition Count", self.select_condition),
            ("Temperature vs Humidity", self.select_temp_vs_humidity),
            ("UV Index Trend", self.select_uv),
        ]

        for text, handler in buttons:
            btn = QPushButton(text)
            btn.setObjectName("optionButton")
            btn.clicked.connect(handler)
            options_layout.addWidget(btn)

        main_layout.addLayout(options_layout)

        plot_btn = QPushButton("Generate Plot")
        plot_btn.setObjectName("plotButton")
        plot_btn.clicked.connect(self.generate_plot)

        main_layout.addWidget(plot_btn, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)

        
    def select_avg_temp(self):
        self.selected_plot = plot_avg_temp_trend
        self.description_label.setText(
            "Shows how the average temperature changed over the last 7 days."
        )
    
    def select_temp_range(self):
        self.selected_plot = plot_temp_range
        self.description_label.setText(
            "Displays daily minimum and maximum temperatures for comparison."            
        )
    
    def select_humidity(self):
        self.selected_plot = plot_humidity_trend
        self.description_label.setText(
            "Shows the variation in average humidity over the last 7 days."            
        )
    
    def select_precipitation(self):
        self.selected_plot = plot_precipitation
        self.description_label.setText(
            "Shows total daily rainfall (precipitation in mm)."            
        )
    
    def select_wind(self):
        self.selected_plot = plot_max_wind
        self.description_label.setText(
            "Displays the maximum wind speed recorded each day."            
        )
    
    def select_condition(self):
        self.selected_plot = plot_condition_counts
        self.description_label.setText(
            "Counts how many days each weather condition occurred."            
        )
        
    def select_temp_vs_humidity(self):
        self.selected_plot = plot_temp_vs_humidity
        self.description_label.setText(
            "Compares average temperature and humidity trends together."
        )

    def select_uv(self):
        self.selected_plot = plot_uv_trend
        self.description_label.setText(
            "Shows daily UV index variation over the last 7 days."
        )
    
    
    def generate_plot(self):
        if not self.selected_plot:
            QMessageBox.warning(self, "No Selection", "Please select a plot first.")
            return
        
        try:
            self.selected_plot(self.city)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        
    def go_back(self):
        self.close()
        if self.parent_window:
            self.parent_window.show()
    
    def load_styles(self):
        from PyQt5.QtWidgets import QApplication

        app = QApplication.instance()
        if not app:
            return

        with open("weather_app/ui/styles/historical.qss") as f:
            app.setStyleSheet(app.styleSheet() + f.read())

            
