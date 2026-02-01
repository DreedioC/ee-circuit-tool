# ohm_law.py
# Calculates Voltage using V = I * R

def calculate_voltage(current_amps, resistance_ohms):
    """
    Returns voltage in Volts given current (A) and resistance (Ω).
    """
    if resistance_ohms < 0:
        return None # Physical impossibility for passive components
    return current_amps * resistance_ohms

if __name__ == "__main__":
    # Test case: 2 Amps through 10 Ohms
    i = 2.0
    r = 10.0
    v = calculate_voltage(i, r)
    print(f"Voltage across {r} Ω resistor with {i} A current is {v} V")