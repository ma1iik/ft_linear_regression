from classes import LinearModel
import json
import os

def get_valid_mileage():
	"""Get and validate car mileage input from the user."""
	try:
		while True:
			user_input = input("Input the car mileage: ").strip()
			if not user_input:
				print("Error: Mileage cant be empty.")
				continue
			if not all(c.isdigit() for c in user_input):
				print("Error: Mileage must contain only digits.")
				continue
			mileage = float(user_input)
			if mileage < 0:
				print("Error: Mileage cant be negative.")
				continue
			if mileage > 1000000:
				print("Warning: Mileage seems unusually high. Please confirm.")
				confirm = input("Is this correct? (y/n): ").lower().strip()
				if confirm != 'y':
					continue
			return mileage
	except KeyboardInterrupt:
		print("\nInput cancelled by user.")
		return None
	except ValueError:
		print("Error: Please enter a valid number for mileage.")
		return None

def ft_prediction():
	"""Predict car price based on user-input mileage using the trained linear regression model."""
	LM = LinearModel()
	mileage = get_valid_mileage()
	if mileage is None:
		print("Prediction cancelled.")
		return
	try:
	
		with open('thetas.json', 'r') as file:
			data = json.load(file)
			LM.theta0 = data.get('theta0')
			LM.theta1 = data.get('theta1')
			print(f"Price for a car with {mileage} km milleage: {LM.predict(mileage):.2f}")
	except FileNotFoundError:
		print(f"Pricee for a car with {mileage} km milleage: {LM.predict(mileage):.2f}")
	except json.JSONDecodeError:
		print("Invalid JSON format!")
	except Exception as e:
		print(f"Unexpected error: {e}")

if __name__ == "__main__":
	ft_prediction()