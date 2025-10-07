from datetime import datetime

exercise_map = {
    0: 1.2,
    1: 1.375,
    2: 1.4625,
    3: 1.55,
    4: 1.725,
    5: 1.9
}

sex_correction = {
    "M": 5,
    "F": -161
}

def calculate_energy_burned(weight: float, height: float, birthday: datetime, exercise_level: int, sex: str) -> float:
    """
    Calculate Basal Metabolic Rate (BMR) using Mifflin-St Jeor Equation and adjust for activity level.

    0: Sedentary: little or no exercise
    1: Exercise 1-3 times/week
    2: Exercise 4-5 times/week
    3: Daily exercise or intense exercise 3-4 times/week
    4: Intense exercise 6-7 times/week
    5: Very intense exercise daily, or physical job

    More info: https://www.calculator.net/bmr-calculator.html

    Arguments:
        weight(float): Weight in kilograms.
        height(float): Height in centimeters.
        birthday(datetime): Date of birth.
        exercise_level(int): Activity level from 0 (sedentary) to 5 (very active).
        sex(str): Biological sex, either 'M' or 'F'.

    Returns:
        (float): Estimated daily energy expenditure in calories (kcal).
    """
    if exercise_level not in exercise_map:
        raise ValueError(f"exercise_level must be between 0 and 5, got {exercise_level}")

    if sex not in sex_correction:
        raise ValueError(f"sex must be 'M' or 'F', got {sex}")

    age = (datetime.today() - birthday).days / 365
    BMR = 10 * weight + 6.25 * height - 5 * age
    return (BMR + sex_correction[sex]) * exercise_map[exercise_level]
