import json
from datetime import UTC, datetime
from urllib.parse import urlencode

import requests
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission


def _geocode(location_name: str) -> dict[str, str]:
    params = {"format": "json", "count": 1, "name": location_name}
    encoded_params = urlencode(params)
    response = requests.get(
        f"https://geocoding-api.open-meteo.com/v1/search?{encoded_params}",
        headers={"Content-Type": "application/json", "Accept": "application/json"},
    )
    response.raise_for_status()
    results = response.json().get("results", [])
    if not results:
        raise ValueError(f"Location '{location_name}' not found.")
    return results[0]


def _get_forecast_params(geocode: dict[str, str]) -> dict:
    today = datetime.now(tz=UTC).date()
    return {
        "current": ",".join(
            [
                "temperature_2m",
                "rain",
                "relative_humidity_2m",
                "wind_speed_10m",
            ]
        ),
        "daily": ",".join(["temperature_2m_max", "temperature_2m_min", "rain_sum"]),
        "timezone": "UTC",
        "latitude": geocode.get("latitude", ""),
        "longitude": geocode.get("longitude", ""),
        "start_date": str(today),
        "end_date": str(today),
        "temperature_unit": "celsius",
    }


@tool(
    name="OpenMeteo",
    description="Retrieve weather information from OpenMeteo.",
    permission=ToolPermission.ADMIN,
)
def open_meteo_tool(location_name: str) -> str:
    """
    Retrieve today's weather information for the specified location.

    :param location_name: The name of the location to retrieve weather information.
    :returns: Formatted string with today's weather information.
    """
    try:
        # Get location coordinates
        geocode = _geocode(location_name)

        # Get weather data
        params = _get_forecast_params(geocode)
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params=params,
            headers={"Accept": "application/json"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        return json.dumps(data, indent=2)

    except Exception as e:
        return f"Error retrieving weather data: {str(e)}"


if __name__ == "__main__":
    # Example usage
    print(open_meteo_tool("Tel Aviv"))
