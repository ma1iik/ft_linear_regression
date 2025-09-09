from dataclasses import dataclass
import json

@dataclass
class LinearModel:
	theta0: float = 0.0
	theta1: float = 0.0
	data: dict = None
	line_progression: dict = None

	def __post_init__(self):
		"""Called automatically after the dataclass initializes"""
		self.data = self.read_data()
	
	def predict(self, mileage):
		"""Calculate the estimated price for a car based on its mileage using the linear model."""
		return self.theta0 + (self.theta1 * mileage)
	
	def read_data(self):
		"""Read data from CSV file and return as dictionary of lists"""
		data = {
			'km': [],
			'price': []
		}

		try:
			with open('data.csv', 'r') as file:
				next(file)
				for line in file:
					km, price = line.strip().split(',')
					data['km'].append(float(km))
					data['price'].append(float(price))
				return data
		except Exception as e:
			print(f"Unknown error: {e}")
			return  data
	
	def save_thetas(self, theta0 : float, theta1 : float):
		"""Save the model's theta parameters to a JSON file and update the instance variables."""
		self.theta0 = theta0
		self.theta1 = theta1
		data = {
			'theta0': self.theta0,
			'theta1': self.theta1,
		}
		try:
			with open('thetas.json', 'w') as file:
				json.dump(data, file, indent=4)
				return True
		except Exception as e:
			print(f"Error writing to JSON file: {e}")
			return False