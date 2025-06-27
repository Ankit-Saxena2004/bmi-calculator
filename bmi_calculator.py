# bmi_calculator.py

def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight 🟡"
    elif 18.5 <= bmi < 25:
        return "Normal weight ✅"
    elif 25 <= bmi < 30:
        return "Overweight 🟠"
    else:
        return "Obese 🔴"

def main():
    print("🔷🔷 Welcome to the BMI Calculator 🔷🔷\n")

    try:
        height = float(input("📏 Enter your height in meters (e.g. 1.75): "))
        weight = float(input("⚖️  Enter your weight in kilograms (e.g. 68): "))

        if height <= 0 or weight <= 0:
            print("❌ Height and weight must be positive numbers.")
            return

        bmi = calculate_bmi(height, weight)
        category = get_bmi_category(bmi)

        print(f"\n📊 Your BMI is: {bmi:.2f}")
        print(f"📌 Category: {category}")

    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()
