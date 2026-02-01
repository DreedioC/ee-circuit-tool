# ohm_law.py
# Calculates Voltage (V = IR) and Power (P = VI)

def calculate_voltage(current_amps, resistance_ohms):
    """
    Returns voltage in Volts given current (A) and resistance (Ω).
    """
    if resistance_ohms < 0:
        return None 
    return current_amps * resistance_ohms

def calculate_power(voltage_volts, current_amps):
    """
    Returns power in Watts given voltage (V) and current (A).
    """
    return voltage_volts * current_amps

if __name__ == "__main__":
    # Test case: 2 Amps through 10 Ohms
    i = 2.0
    r = 10.0
    v = calculate_voltage(i, r)
    p = calculate_power(v, i)
    
    print(f"Current: {i} A, Resistance: {r} Ω")
    print(f"Voltage: {v} V")
    print(f"Power Dissipation: {p} W")