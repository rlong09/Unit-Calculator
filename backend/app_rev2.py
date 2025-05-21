"""
Unit Converter Application (Backend)
====================================

This Flask application provides a REST API for performing unit conversions between metric and imperial/standard units.
Flask is a lightweight web framework for Python that allows you to build web applications and APIs quickly with minimal code.

How it works:
------------
1. Architecture:
   - Flask-based RESTful API that handles conversion requests
   - CORS-enabled to allow requests from browser-based frontend
   - Stateless design with each request being self-contained

2. Unit Conversion System:
   - Uses a base unit approach for each measurement category
   - All conversions use a two-step process:
     a) Convert input unit to base unit (e.g., feet → meters)
     b) Convert base unit to target unit (e.g., meters → kilometers)
   - Base units for each category:
     * Length: meter
     * Weight: gram 
     * Volume: liter
     * Temperature: direct formulas (no base unit)
     * Area: square meter

3. API Endpoints:
   - GET /units: Returns available units grouped by category
   - POST /convert: Performs unit conversion based on input parameters

4. Usage:
   - Run this script with Python: `python app.py`
   - Server starts on http://localhost:5000 by default
   - Frontend can make requests to endpoints to perform conversions

5. Data Flow:
   - Frontend sends conversion request with: value, from_unit, to_unit, category
   - Backend processes request through appropriate conversion method
   - Result is returned to frontend as JSON

Author: Ryan Long & Thomas Long
Date: May 12, 2025
"""

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# Conversion functions for different measurement types
class UnitConverter:
    """
    Handles all unit conversion operations for different measurement categories.
    Each method follows the same pattern:
    1. Convert from source unit to a standard base unit
    2. Convert from base unit to target unit
    
    Base units for each category:
    - Length: meter
    - Weight: gram
    - Volume: liter
    - Temperature: direct conversion (no base unit)
    - Area: square meter
    """
    @staticmethod
    def length_conversion(value, from_unit, to_unit):
        """
        Convert between length units.
        Base unit: meter
        
        Supported units:
        - Metric: meter, kilometer, centimeter, millimeter
        - Imperial: mile, yard, foot, inch
        
        Args:
            value (float): The value to convert
            from_unit (str): Source unit identifier
            to_unit (str): Target unit identifier
            
        Returns:
            float: The converted value
        """
        # Convert everything to meters first, then to the target unit
        meters = 0
        
        # Convert from source unit to meters
        if from_unit == "meter":
            meters = value
        elif from_unit == "kilometer":
            meters = value * 1000
        elif from_unit == "centimeter":
            meters = value * 0.01
        elif from_unit == "millimeter":
            meters = value * 0.001
        elif from_unit == "mile":
            meters = value * 1609.34
        elif from_unit == "yard":
            meters = value * 0.9144
        elif from_unit == "foot":
            meters = value * 0.3048
        elif from_unit == "inch":
            meters = value * 0.0254
        
        # Convert from meters to target unit
        if to_unit == "meter":
            return meters
        elif to_unit == "kilometer":
            return meters / 1000
        elif to_unit == "centimeter":
            return meters * 100
        elif to_unit == "millimeter":
            return meters * 1000
        elif to_unit == "mile":
            return meters / 1609.34
        elif to_unit == "yard":
            return meters / 0.9144
        elif to_unit == "foot":
            return meters / 0.3048
        elif to_unit == "inch":
            return meters / 0.0254
    
    @staticmethod
    def weight_conversion(value, from_unit, to_unit):
        """
        Convert between weight/mass units.
        Base unit: gram
        
        Supported units:
        - Metric: gram, kilogram, milligram, metric ton
        - Imperial: pound, ounce, stone, US ton
        
        Args:
            value (float): The value to convert
            from_unit (str): Source unit identifier
            to_unit (str): Target unit identifier
            
        Returns:
            float: The converted value
        """
        # Convert everything to grams first, then to the target unit
        grams = 0
        
        # Convert from source unit to grams
        if from_unit == "gram":
            grams = value
        elif from_unit == "kilogram":
            grams = value * 1000
        elif from_unit == "milligram":
            grams = value * 0.001
        elif from_unit == "metric_ton":
            grams = value * 1000000
        elif from_unit == "pound":
            grams = value * 453.592
        elif from_unit == "ounce":
            grams = value * 28.3495
        elif from_unit == "stone":
            grams = value * 6350.29
        elif from_unit == "us_ton":
            grams = value * 907185
        
        # Convert from grams to target unit
        if to_unit == "gram":
            return grams
        elif to_unit == "kilogram":
            return grams / 1000
        elif to_unit == "milligram":
            return grams * 1000
        elif to_unit == "metric_ton":
            return grams / 1000000
        elif to_unit == "pound":
            return grams / 453.592
        elif to_unit == "ounce":
            return grams / 28.3495
        elif to_unit == "stone":
            return grams / 6350.29
        elif to_unit == "us_ton":
            return grams / 907185
    
    @staticmethod
    def volume_conversion(value, from_unit, to_unit):
        """
        Convert between volume units.
        Base unit: liter
        
        Supported units:
        - Metric: liter, milliliter, cubic meter
        - Imperial/US: US gallon, US quart, US pint, US cup, US fluid ounce, Imperial gallon
        
        Args:
            value (float): The value to convert
            from_unit (str): Source unit identifier
            to_unit (str): Target unit identifier
            
        Returns:
            float: The converted value
        """
        # Convert everything to liters first, then to the target unit
        liters = 0
        
        # Convert from source unit to liters
        if from_unit == "liter":
            liters = value
        elif from_unit == "milliliter":
            liters = value * 0.001
        elif from_unit == "cubic_meter":
            liters = value * 1000
        elif from_unit == "us_gallon":
            liters = value * 3.78541
        elif from_unit == "us_quart":
            liters = value * 0.946353
        elif from_unit == "us_pint":
            liters = value * 0.473176
        elif from_unit == "us_cup":
            liters = value * 0.236588
        elif from_unit == "us_fluid_ounce":
            liters = value * 0.0295735
        elif from_unit == "imperial_gallon":
            liters = value * 4.54609
        
        # Convert from liters to target unit
        if to_unit == "liter":
            return liters
        elif to_unit == "milliliter":
            return liters * 1000
        elif to_unit == "cubic_meter":
            return liters / 1000
        elif to_unit == "us_gallon":
            return liters / 3.78541
        elif to_unit == "us_quart":
            return liters / 0.946353
        elif to_unit == "us_pint":
            return liters / 0.473176
        elif to_unit == "us_cup":
            return liters / 0.236588
        elif to_unit == "us_fluid_ounce":
            return liters / 0.0295735
        elif to_unit == "imperial_gallon":
            return liters / 4.54609
    
    @staticmethod
    def temperature_conversion(value, from_unit, to_unit):
        """
        Convert between temperature units.
        Note: Temperature conversion uses direct formulas rather than a base unit approach.
        
        Supported units:
        - Celsius (°C)
        - Fahrenheit (°F)
        - Kelvin (K)
        
        Args:
            value (float): The value to convert
            from_unit (str): Source unit identifier
            to_unit (str): Target unit identifier
            
        Returns:
            float: The converted value
        """
        # Convert directly between temperature units
        if from_unit == to_unit:
            return value
        
        # Celsius to other units
        if from_unit == "celsius":
            if to_unit == "fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "kelvin":
                return value + 273.15
        
        # Fahrenheit to other units
        elif from_unit == "fahrenheit":
            if to_unit == "celsius":
                return (value - 32) * 5/9
            elif to_unit == "kelvin":
                return (value - 32) * 5/9 + 273.15
        
        # Kelvin to other units
        elif from_unit == "kelvin":
            if to_unit == "celsius":
                return value - 273.15
            elif to_unit == "fahrenheit":
                return (value - 273.15) * 9/5 + 32
    
    @staticmethod
    def area_conversion(value, from_unit, to_unit):
        """
        Convert between area units.
        Base unit: square meter
        
        Supported units:
        - Metric: square meter, square kilometer, square centimeter, hectare
        - Imperial: square mile, acre, square yard, square foot, square inch
        
        Args:
            value (float): The value to convert
            from_unit (str): Source unit identifier
            to_unit (str): Target unit identifier
            
        Returns:
            float: The converted value
        """
        # Convert everything to square meters first, then to the target unit
        square_meters = 0
        
        # Convert from source unit to square meters
        if from_unit == "square_meter":
            square_meters = value
        elif from_unit == "square_kilometer":
            square_meters = value * 1000000
        elif from_unit == "square_centimeter":
            square_meters = value * 0.0001
        elif from_unit == "hectare":
            square_meters = value * 10000
        elif from_unit == "square_mile":
            square_meters = value * 2589988.11
        elif from_unit == "acre":
            square_meters = value * 4046.86
        elif from_unit == "square_yard":
            square_meters = value * 0.836127
        elif from_unit == "square_foot":
            square_meters = value * 0.092903
        elif from_unit == "square_inch":
            square_meters = value * 0.00064516
        
        # Convert from square meters to target unit
        if to_unit == "square_meter":
            return square_meters
        elif to_unit == "square_kilometer":
            return square_meters / 1000000
        elif to_unit == "square_centimeter":
            return square_meters * 10000
        elif to_unit == "hectare":
            return square_meters / 10000
        elif to_unit == "square_mile":
            return square_meters / 2589988.11
        elif to_unit == "acre":
            return square_meters / 4046.86
        elif to_unit == "square_yard":
            return square_meters / 0.836127
        elif to_unit == "square_foot":
            return square_meters / 0.092903
        elif to_unit == "square_inch":
            return square_meters / 0.00064516

# API endpoint for unit conversion
@app.route('/convert', methods=['POST'])
def convert():
    """
    API endpoint to handle unit conversion requests.
    
    Expects a JSON object with the following properties:
    - value (float): The value to convert
    - from_unit (str): Source unit identifier
    - to_unit (str): Target unit identifier
    - category (str): Measurement category (length, weight, volume, temperature, area)
    
    Returns:
    - JSON object with:
      - result (float): The converted value
      - from_value (float): Original value
      - from_unit (str): Source unit
      - to_unit (str): Target unit
      - category (str): Measurement category
    
    Error response:
    - JSON object with error message if conversion fails
    """
    data = request.get_json()
    
    try:
        value = float(data['value'])
        from_unit = data['from_unit']
        to_unit = data['to_unit']
        category = data['category']
        
        result = 0
        
        if category == "length":
            result = UnitConverter.length_conversion(value, from_unit, to_unit)
        elif category == "weight":
            result = UnitConverter.weight_conversion(value, from_unit, to_unit)
        elif category == "volume":
            result = UnitConverter.volume_conversion(value, from_unit, to_unit)
        elif category == "temperature":
            result = UnitConverter.temperature_conversion(value, from_unit, to_unit)
        elif category == "area":
            result = UnitConverter.area_conversion(value, from_unit, to_unit)
        else:
            return jsonify({"error": "Invalid category"}), 400
        
        return jsonify({
            "result": round(result, 6),
            "from_value": value,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "category": category
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Serve the unit data for frontend
@app.route('/units', methods=['GET'])
def get_units():
    """
    API endpoint to provide available units organized by category.
    
    Returns:
    - JSON object with categories as keys, each containing an array of unit objects:
      - value (str): Unit identifier used in conversion calculations
      - label (str): Human-readable unit name with symbol for display
    
    This endpoint allows the frontend to dynamically populate unit selection dropdowns.
    """
    unit_data = {
        "length": [
            {"value": "meter", "label": "Meter (m)"},
            {"value": "kilometer", "label": "Kilometer (km)"},
            {"value": "centimeter", "label": "Centimeter (cm)"},
            {"value": "millimeter", "label": "Millimeter (mm)"},
            {"value": "mile", "label": "Mile (mi)"},
            {"value": "yard", "label": "Yard (yd)"},
            {"value": "foot", "label": "Foot (ft)"},
            {"value": "inch", "label": "Inch (in)"}
        ],
        "weight": [
            {"value": "gram", "label": "Gram (g)"},
            {"value": "kilogram", "label": "Kilogram (kg)"},
            {"value": "milligram", "label": "Milligram (mg)"},
            {"value": "metric_ton", "label": "Metric Ton (t)"},
            {"value": "pound", "label": "Pound (lb)"},
            {"value": "ounce", "label": "Ounce (oz)"},
            {"value": "stone", "label": "Stone (st)"},
            {"value": "us_ton", "label": "US Ton"}
        ],
        "volume": [
            {"value": "liter", "label": "Liter (L)"},
            {"value": "milliliter", "label": "Milliliter (mL)"},
            {"value": "cubic_meter", "label": "Cubic Meter (m³)"},
            {"value": "us_gallon", "label": "US Gallon (gal)"},
            {"value": "us_quart", "label": "US Quart (qt)"},
            {"value": "us_pint", "label": "US Pint (pt)"},
            {"value": "us_cup", "label": "US Cup"},
            {"value": "us_fluid_ounce", "label": "US Fluid Ounce (fl oz)"},
            {"value": "imperial_gallon", "label": "Imperial Gallon (gal)"}
        ],
        "temperature": [
            {"value": "celsius", "label": "Celsius (°C)"},
            {"value": "fahrenheit", "label": "Fahrenheit (°F)"},
            {"value": "kelvin", "label": "Kelvin (K)"}
        ],
        "area": [
            {"value": "square_meter", "label": "Square Meter (m²)"},
            {"value": "square_kilometer", "label": "Square Kilometer (km²)"},
            {"value": "square_centimeter", "label": "Square Centimeter (cm²)"},
            {"value": "hectare", "label": "Hectare (ha)"},
            {"value": "square_mile", "label": "Square Mile (mi²)"},
            {"value": "acre", "label": "Acre"},
            {"value": "square_yard", "label": "Square Yard (yd²)"},
            {"value": "square_foot", "label": "Square Foot (ft²)"},
            {"value": "square_inch", "label": "Square Inch (in²)"}
        ]
    }
    
    return jsonify(unit_data)

if __name__ == '__main__':
    # Start the Flask development server when this script is run directly
    # - debug=True enables auto-reload on code changes
    # - host='0.0.0.0' makes the server publicly accessible on the network
    # - port=5000 is the default Flask port
    app.run(debug=True, host='0.0.0.0', port=5000)
