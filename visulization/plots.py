import matplotlib.pyplot as plt
import pandas as pd
from weather_app.backend.weather_backend import (
    get_current_weather,
    get_historical_weather
)

def apply_dark_theme():
    plt.rcParams.update({
        "figure.facecolor": "#0f172a",
        "axes.facecolor": "#020617",
        "axes.edgecolor": "#334155",
        "axes.labelcolor": "#e5e7eb",
        "text.color": "#e5e7eb",
        "xtick.color": "#cbd5f5",
        "ytick.color": "#cbd5f5",
        "grid.color": "#334155",
        "axes.grid": True,
        "grid.linestyle": "--",
        "grid.alpha": 0.3,
        "legend.facecolor": "#020617",
        "legend.edgecolor": "#334155",
    })


def plot_avg_temp_trend(city: str):
    """Line chart of average temperature over the last 7 days"""
    apply_dark_theme()
    df = get_historical_weather(city)
    df["date"] = pd.to_datetime(df["date"])
    
    plt.figure(figsize=(9,5))
    plt.plot(df["date"], df["avg_temp"], marker="o", color="tomato")
    plt.title("Average Temperature Trend (Last 7 Days)")
    plt.xlabel("Date")
    plt.ylabel("Avg Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(alpha=0.4)
    plt.tight_layout()
    plt.show()

def plot_temp_range(city: str):
    """Bar chart showing min and max temperature per day"""
    apply_dark_theme()
    df = get_historical_weather(city)
    df["date"] = pd.to_datetime(df["date"])
    
    plt.figure(figsize=(10,5))
    plt.bar(df["date"] - pd.Timedelta(hours=2), df["min_temp"], width=0.4, label="Min Temp", color="skyblue")
    plt.bar(df["date"] + pd.Timedelta(hours=2), df["max_temp"], width=0.4, label="Max Temp", color="orange")
    plt.title("Daily Min and Max Temperature")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(alpha=0.4)
    plt.tight_layout()
    plt.show()

def plot_humidity_trend(city: str):
    """Line chart of average humidity over last 7 days"""
    apply_dark_theme()
    df = get_historical_weather(city)
    df["date"] = pd.to_datetime(df["date"])
    
    plt.figure(figsize=(9,5))
    plt.plot(df["date"], df["humidity"], marker="o", color="skyblue")
    plt.title("Humidity Trend (Last 7 Days)")
    plt.xlabel("Date")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)
    plt.grid(alpha=0.4)
    plt.tight_layout()
    plt.show()

def plot_precipitation(city: str):
    """Bar chart of total precipitation per day"""
    apply_dark_theme()
    df = get_historical_weather(city)
    df["date"] = pd.to_datetime(df["date"])
    
    plt.figure(figsize=(9,5))
    plt.bar(df["date"], df["precipitation"], color="deepskyblue")
    plt.title("Daily Precipitation (mm)")
    plt.xlabel("Date")
    plt.ylabel("Precipitation (mm)")
    plt.xticks(rotation=45)
    plt.grid(alpha=0.4)
    plt.tight_layout()
    plt.show()

def plot_max_wind(city: str):
    """Line chart of max wind speed per day"""
    apply_dark_theme()
    df = get_historical_weather(city)
    df["date"] = pd.to_datetime(df["date"])
    
    plt.figure(figsize=(9,5))
    plt.plot(df["date"], df["max_wind"], marker="o", color="green")
    plt.title("Max Wind Speed Trend (kph)")
    plt.xlabel("Date")
    plt.ylabel("Max Wind Speed (kph)")
    plt.xticks(rotation=45)
    plt.grid(alpha=0.4)
    plt.tight_layout()
    plt.show()

def plot_condition_counts(city: str):
    """Bar chart counting how many days per weather condition"""
    apply_dark_theme()
    df = get_historical_weather(city)
    
    counts = df["condition"].value_counts()
    
    plt.figure(figsize=(8,5))
    plt.bar(counts.index, counts.values, color="goldenrod")
    plt.title("Weather Condition Counts (Last 7 Days)")
    plt.xlabel("Condition")
    plt.ylabel("Number of Days")
    plt.xticks(rotation=45)
    plt.grid(alpha=0.4)
    plt.tight_layout()
    plt.show()

def plot_temp_vs_humidity(city: str):
    """Line chart comparing average temperature vs humidity"""
    apply_dark_theme()
    df = get_historical_weather(city)
    df["date"] = pd.to_datetime(df["date"])
    
    plt.figure(figsize=(9,5))
    plt.plot(df["date"], df["avg_temp"], marker="o", label="Avg Temp (°C)", color="tomato")
    plt.plot(df["date"], df["humidity"], marker="o", label="Humidity (%)", color="skyblue")
    plt.title("Temperature vs Humidity (Last 7 Days)")
    plt.xlabel("Date")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(alpha=0.4)
    plt.tight_layout()
    plt.show()

def plot_uv_trend(city: str):
    """Line chart of UV index"""
    apply_dark_theme()
    df = get_historical_weather(city)
    df["date"] = pd.to_datetime(df["date"])
    
    plt.figure(figsize=(9,5))
    plt.plot(df["date"], df["uv"], marker="o", color="purple")
    plt.title("UV Index Trend (Last 7 Days)")
    plt.xlabel("Date")
    plt.ylabel("UV Index")
    plt.xticks(rotation=45)
    plt.grid(alpha=0.4)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    city = "Durgapur"
    
    plot_avg_temp_trend(city)
    plot_temp_range(city)
    plot_humidity_trend(city)
    plot_precipitation(city)
    plot_max_wind(city)
    plot_condition_counts(city)
    plot_temp_vs_humidity(city)
    plot_uv_trend(city)