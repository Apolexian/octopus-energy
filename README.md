# Octopus Energy API Python Wrapper

This Python script provides a simple wrapper for interacting with the Octopus Energy API.

## Requirements

- Python 3
- `requests` library
- `pandas` library
- `python-dotenv` library

## Installation

You can install the required libraries using pip:

```bash
pip install requests pandas python-dotenv
```

## Usage

First, initialize the `OctopusEnergyAPI` class with your API key, MPAN (Meter Point Administration Number), and meter serial number:

```python
from octo import OctopusEnergyAPI

api = OctopusEnergyAPI(api_key="your_api_key", mpan="your_mpan", serial_number="your_serial_number")
```

Then, you can use the `get_consumption_data` method to fetch consumption data. This method requires the following parameters:

- `group_by`: How to group the consumption data.
- `page_size`: The number of results to return per page.
- `period_from`: The start of the period for which to fetch consumption data.
- `period_to`: The end of the period for which to fetch consumption data.

```python
data = api.get_consumption_data(group_by="day", page_size=100, period_from="2021-01-01", period_to="2021-12-31")
```

This will return a JSON object with the consumption data.

## Environment Variables

This script uses the `dotenv` library to load environment variables. You can store your API key, MPAN, and serial number in a `.env` file in the same directory as the script. The `.env` file should look like this:

```
API_KEY=your_api_key
MPAN=your_mpan
SERIAL_NUMBER=your_serial_number
```

Then, you can initialize the `OctopusEnergyAPI` class without passing any arguments:

```python
api = OctopusEnergyAPI()
```
