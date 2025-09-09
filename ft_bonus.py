import matplotlib.pyplot as plt
import json
import sys
from classes import LinearModel

def calculate_precision(LM):
	"""Calculate precision of the model using Mean Absolute Error (MAE) method"""
	data_prices = LM.data['price']
	errors_sum = 0
	for i in range(len(data_prices)):
		errors_sum += abs(data_prices[i] - LM.predict(LM.data['km'][i]))
	mae = errors_sum / len(data_prices)

	print("\n===== Model Precision =====")
	print(f"Mean Absolute Error: ${mae:.2f}")
	print(f"This means that, on average, our predictions are off by ${mae:.2f}")
	return mae


def visualize_data(LM):
	"""Create visualization of data points and regression line"""
	try:
		with open('thetas.json', 'r') as file:
			thetas = json.load(file)
			theta0 = thetas['theta0']
			theta1 = thetas['theta1']
			plt.figure(figsize=(10, 6))
			plt.scatter(LM.data['km'], LM.data['price'], color='Blue', label='Data Points')
			min_km = min(LM.data['km'])
			max_km = max(LM.data['km'])
			x = [min_km, max_km]
			y = [theta0 + theta1 * min_km, theta0 + theta1 * max_km]
			plt.plot(x, y, color='red', label=f'Regression line: y = {theta0:.2f} + {theta1:.4f}x')
			
			plt.title('Linear Regression: Car Price vs. Mileage')
			plt.xlabel('Mileage (km)')
			plt.ylabel('Price ($)')
			plt.grid(True)
			plt.legend()
			plt.savefig('visualisation.png')
			print("Visualization saved as 'visualization.png'")
			plt.show()
	except Exception as e:
		print(f"Unexpected error: {e}")
		return
	
def ft_bonus(option=None):
	"""Run bonus features based on the provided option"""
	LM = LinearModel()
	try:
		with open('thetas.json', 'r') as file:
			thetas = json.load(file)
			LM.theta0 = thetas['theta0']
			LM.theta1 = thetas['theta1']
			print(f"Loaded model parameters: theta0 = {LM.theta0:.4f}, theta1 = {LM.theta1:.8f}")
	except FileNotFoundError:
		print("No trained model found. Please run the training program first.")
		return
	except Exception as e:
		print(f"Error loading model: {e}")
		return
	if not LM.data or len(LM.data['km']) == 0:
		print("No available data for analysis")
		return
	if option in ['-v', '--visualize']:
		visualize_data(LM)
	elif option in ['-p', '--precision']:
		calculate_precision(LM)
	else:
		visualize_data(LM)
		calculate_precision(LM)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		option = sys.argv[1]
		ft_bonus(option)
	else:
		ft_bonus()