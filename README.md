# Immo Eliza Deployment

A machine learning-powered property price prediction system for Belgian real estate. This project provides both a FastAPI backend for predictions and a Streamlit frontend for user interaction.

## Overview

**Immo Eliza Deployment** is a full-stack application that predicts property prices based on various features including location, property type, condition, amenities, and proximity to key services. The system is trained on Belgian property data and supports bilingual interface (English/French).

## Features

- 🏠 **Property Price Prediction** - Estimate Belgian property values using machine learning
- 🌐 **Bilingual Interface** - Support for English and French
- 📊 **Rich Feature Set** - Considers 17+ property and location features
- 🐳 **Docker Support** - Easy deployment with Docker containerization
- ⚡ **FastAPI Backend** - Robust REST API for predictions
- 🎨 **Streamlit Frontend** - Interactive web interface for users

## Architecture

### Backend (`/api`)
- **FastAPI** application (`api.py`) - REST API endpoint for property predictions
- **Prediction Model** (`predict.py`) - ML model inference and feature processing
- **Data Files** - Zipcode coordinates and salary data for enrichment

### Frontend (`/streamlit`)
- **Streamlit App** (`stream.py`) - Interactive UI for property valuation
- Bilingual form with comprehensive property input fields
- Real-time predictions via API integration

## Tech Stack

- **Backend**: FastAPI, Uvicorn, Pydantic
- **Frontend**: Streamlit
- **ML/Data**: scikit-learn, XGBoost, NumPy, Pandas
- **Deployment**: Docker
- **Dependencies**: See `requirements.txt`

## Installation

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Max96H/immo-eliza-deployment.git
   cd immo-eliza-deployment
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Docker Setup

Build and run the Docker container:

```bash
docker build -t immo-eliza .
docker run -p 8000:8000 immo-eliza
```

## Usage

### Running the API

```bash
uvicorn api.api:app --reload
```

The API will be available at `http://localhost:8000`

**API Endpoints:**
- `GET /` - Health check
- `POST /predict` - Get property price prediction

**Example Request:**
```json
{
  "postcode": "1000",
  "property_type": "house",
  "province": "brussels",
  "bedroom_count": 3,
  "livable_surface": 150,
  "total_surface": 200,
  "property_state": "Normal",
  "build_year": 1990,
  "energy_consumption_kWh": 150,
  "terrace": true,
  "swimming_pool": false,
  "garage": true,
  "preschool_distance_m": 500,
  "train_station_distance_m": 800,
  "supermarket_distance_m": 300,
  "nearest_city_distance_km": 2.5
}
```

### Running the Streamlit App

```bash
streamlit run streamlit/stream.py
```

The app will open in your browser at `http://localhost:8501`

## Input Features

The prediction model uses the following features:

| Feature | Type | Description |
|---------|------|-------------|
| `postcode` | string | Belgian postal code |
| `province` | string | Province in Belgium |
| `property_type` | string | "house" or "apartment" |
| `property_state` | string | Condition (Normal, To renovate, Excellent, etc.) |
| `bedroom_count` | int | Number of bedrooms |
| `livable_surface` | int | Livable area in m² |
| `total_surface` | int | Total area in m² |
| `energy_consumption_kWh` | int | Energy consumption (kWh/m²/year) |
| `build_year` | int | Year of construction |
| `terrace` | bool | Has terrace |
| `swimming_pool` | bool | Has swimming pool |
| `garage` | bool | Has garage |
| `preschool_distance_m` | int | Distance to nearest preschool (m) |
| `train_station_distance_m` | int | Distance to train station (m) |
| `supermarket_distance_m` | int | Distance to supermarket (m) |
| `nearest_city_distance_km` | float | Distance to nearest city (km) |

## Data Files

The application uses the following data files in `/data`:
- `zipcode_coordinates.csv` - Latitude/longitude for Belgian postal codes
- `salary_postcode.csv` - Average salary data by postcode (for feature enrichment)

## Deployment

The application is deployed on Render:
- **Backend URL**: https://immo-eliza-deployment-max.onrender.com

## Project Structure

```
immo-eliza-deployment/
├── api/
│   ├── api.py                 # FastAPI application
│   ├── predict.py             # ML model inference
│   └── src/                   # Supporting modules
├── streamlit/
│   └── stream.py              # Streamlit web interface
├── data/
│   ├── zipcode_coordinates.csv
│   └── salary_postcode.csv
├── Dockerfile                 # Docker configuration
├── requirements.txt           # Python dependencies
├── pyproject.toml            # FastAPI configuration
└── README.md                 # This file
```

## Development

### Adding New Features

To add new input features to the model:
1. Update the `Item` class in `api/api.py`
2. Update the form in `streamlit/stream.py`
3. Retrain the model in `predict.py`

### Environment Variables

Set the `PORT` environment variable to customize the API port (defaults to 8000):
```bash
PORT=3000 uvicorn api.api:app
```

## License

This project is open source and available under the MIT License.

## Author

Created by [Max96H](https://github.com/Max96H)

## Support

For issues, questions, or contributions, please open an issue on the [GitHub repository](https://github.com/Max96H/immo-eliza-deployment).
