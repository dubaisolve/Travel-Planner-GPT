# Travel Assistant Application :earth_americas:

## Introduction :page_facing_up:
Welcome to the **Travel Assistant** application repository. This tool is designed to streamline your travel planning process by integrating APIs like Google Maps and TripAdvisor. It offers a variety of features for action initialization, output formatting, information enrichment, and much more.

Demo - https://youtu.be/QGnqj9K4dgs

## Features :sparkles:

### 1. Action Initialization :rocket:
- **TextSearch Action (Google Maps)**: Initiates broad queries using Google Maps TextSearch for versatile search capabilities.

### 2. Output Formatting :clipboard:
- **Presentation**: Displays information in a tabular format, including name, location, ratings, prices, and opening hours.

### 3. Information Enrichment :mag:
- **Details**: Uses additional actions to gather more information about locations.

### 4. Route Planning :world_map:
- **APIs Used**: Employs Google Maps API for comprehensive route planning.

### 5. Sequential Action Triggering :link:
- **Process**: After Google Maps API results, automatically triggers TripAdvisor API actions for further details.

### 6. Comparative Analysis :balance_scale:
- **Functionality**: Offers analysis by comparing data from Google Maps and TripAdvisor.

### 7. Tabular Presentation for Comparisons :bar_chart:
- **Display**: Presents comparative analysis in an easy-to-read table format.

### 8. Intelligent Trip Planning :bulb:
- **Strategy**: Begins with popular attractions and tailors the plan based on user preferences, including comprehensive details.

## Google Actions Configuration :gear:

### 1. TextSearch Action (Google Maps)
- **Trigger & Response**: User requests initiate a search and the response is parsed for user-friendly display.

### 2. findPlaceJson (Google Maps)
- **Purpose**: Retrieves detailed place information.

### 3. getDirectionsJson (Google Maps)
- **Objective**: Provides directions and various route options.

### 4. photoSearch (Google Maps)
- **Endpoint**: `/place/photo` with parameters for photo searches.

## TripAdvisor Actions Configuration :camera:

### 1. locationSearch (TripAdvisor API)
- **Initial Step**: Triggered first to get the location id for subsequent actions.

### 2. locationReviews (TripAdvisor API)
- **Purpose**: Retrieves recent reviews for specific locations.

### 3. locationPhotos (TripAdvisor API)
- **Functionality**: Shows recent photos of locations.

### 4. locationDetails (TripAdvisor API)
- **Details Provided**: Offers in-depth information about a location.

### 5. nearbySearch (TripAdvisor API)
- **Usage**: Finds locations near the user’s current coordinates.

---

Feel free to explore the individual action files in this repository for more detailed information.
