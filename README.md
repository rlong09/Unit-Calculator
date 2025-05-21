# Unit-Calculator
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

Unit Converter Application (frontend)
====================================
An easy unit calculator that converts units to your request!
This UI can be pointed to the included backend.

 It Includes:

 *Weight
 *Length
 *Area
 *Temperature
 *Volume
 

 

Author: Ryan Long & Thomas Long
Date: May 12, 2025
