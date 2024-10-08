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

WATER_DENSITY = 998.2  # in kg/m^3

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    # Pressure loss formula due to fittings
    return -0.04 * WATER_DENSITY * (fluid_velocity ** 2) * quantity_fittings / 2000


WATER_VISCOSITY = 0.0010016  # dynamic viscosity in Pascal seconds

def reynolds_number(hydraulic_diameter, fluid_velocity):
    # Formula for Reynolds number
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_VISCOSITY




def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    # Formula to calculate the constant k
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    
    # Pressure loss formula for pipe diameter reduction
    return -k * WATER_DENSITY * (fluid_velocity ** 2) / 2000


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    # Calculations
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    
    # Pressure loss through supply pipe
    pressure += pressure_loss_from_pipe(diameter, length1, friction, velocity)
    # Loss through fittings
    pressure += pressure_loss_from_fittings(velocity, quantity_angles)
    # Loss from pipe reduction
    pressure += pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    
    # Pressure loss through household pipe
    pressure += pressure_loss_from_pipe(diameter, length2, friction, velocity)
    
    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()
