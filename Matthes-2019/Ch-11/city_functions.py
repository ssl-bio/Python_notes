def format_city(name, country, population=None):
    """Format the location of a city
    """
    if population:
        name_f = f"{name.title()}, {country.title()} - {population}"
    else:
        name_f = f"{name.title()}, {country.title()}"
    return name_f
