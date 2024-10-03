# water_flow.py

def water_column_height(tower_height, tank_height):
    """
    Calculate the height of the water column based on tower and tank heights.
    
    Parameters:
    tower_height (float): Height of the tower in meters.
    tank_height (float): Height of the tank walls in meters.
    
    Returns:
    float: Height of the water column in meters.
    """
    return tower_height + (3/4) * tank_height


def pressure_gain_from_water_height(height):
    """
    Calculate the pressure caused by gravity pulling down the water in a tank.
    
    Parameters:
    height (float): Height of the water column in meters.
    
    Returns:
    float: Pressure in kilopascals.
    """
    rho = 998.2  # density of water in kg/m^3
    g = 9.80665  # acceleration due to gravity in m/s^2
    return (rho * g * height) / 1000  # pressure in kPa


def pressure_loss_from_pipe(diameter, length, friction_factor, fluid_velocity):
    """
    Calculate the pressure loss due to friction in a pipe.
    
    Parameters:
    diameter (float): Diameter of the pipe in meters.
    length (float): Length of the pipe in meters.
    friction_factor (float): Friction factor for the pipe.
    fluid_velocity (float): Velocity of the fluid in m/s.
    
    Returns:
    float: Pressure loss in kilopascals.
    """
    rho = 998.2  # density of water in kg/m^3
    return - (friction_factor * length * rho * fluid_velocity**2) / (2000 * diameter)
