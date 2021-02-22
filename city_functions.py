def get_location(city, country, population=""):
    """Output city and country."""
    if population:
        location = f"{city}, {country} - population {population}"
    else:
        location = f"{city}, {country}."
    return location.title()
