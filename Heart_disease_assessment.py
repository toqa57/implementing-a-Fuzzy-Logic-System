import utils
from Fuzzy_logic import compute_risk


def main():
    age = utils.get_valid_input("Enter age (20-80): ", 20, 80, int)
    chol = utils.get_valid_input("Enter cholesterol level (100-600): ", 100, 600, int)
    trestbps = utils.get_valid_input("Enter resting blood pressure (80-200): ", 80, 200, int)
    thalach = utils.get_valid_input("Enter maximum heart rate achieved (60-210): ", 60, 210, int)
    oldpeak = utils.get_valid_input("Enter oldpeak (0-6.9): ", 0, 6.9, float)

    risk_level = compute_risk(age, chol, trestbps, thalach, oldpeak)
    print(f"Heart Disease Risk Level: {risk_level:.2f}")


if __name__ == "__main__":
    main()