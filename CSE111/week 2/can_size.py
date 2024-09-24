import math

def compute_volume(radius, height):
    """Calcula o volume de uma lata de aço em centímetros cúbicos."""
    return math.pi * radius**2 * height

def compute_surface_area(radius, height):
    """Calcula a área de superfície de uma lata de aço em centímetros quadrados."""
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(volume, surface_area):
    """Calcula a eficiência de armazenamento de uma lata de aço."""
    return volume / surface_area

def main():
    # Dados das latas: nome, raio (cm), altura (cm)
    can_sizes = [
        ("#1 Piquenique", 6.83, 10.16),
        ("#1 Alto", 7.78, 11.91),
        ("#2", 8.73, 11.59),
        ("#2.5", 10.32, 11.91),
        ("#3 Cilindro", 10.79, 17.78),
        ("#5", 13.02, 14.29),
        ("#6Z", 5.40, 8.89),
        ("#8Z curto", 6.83, 7.62),
        ("#10", 15.72, 17.78),
        ("#211", 6.83, 12.38),
        ("#300", 7.62, 11.27),
        ("#303", 8.10, 11.11)
    ]
    
    print("Tamanho da lata e eficiência de armazenamento:")
    for name, radius, height in can_sizes:
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        efficiency = compute_storage_efficiency(volume, surface_area)
        print(f"{name} {efficiency:.2f}")

if __name__ == "__main__":
    main()