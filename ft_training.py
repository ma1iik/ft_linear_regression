from classes import LinearModel
import json
import os

def ft_training(learning_rate=0.01, iterations=10000):
	"""Train a linear regression model on car mileage/price data using gradient descent."""
	LM = LinearModel()
	if not LM.data or len(LM.data['km']) == 0:
		print("No data available for training")
		LM.save_thetas(0.0, 0.0)
		return
	m = len(LM.data['km'])
	print(f"Training on {m} examples for {iterations} iterations...")
	km_min = min(LM.data['km'])
	km_max = max(LM.data['km'])
	km_range = km_max - km_min
	km_normalized = [(x - km_min) / km_range for x in LM.data['km']]
	tmp_theta0 = 0
	tmp_theta1 = 0
	for iteration in range(iterations):
		error_sum = 0
		weighted_error_sum = 0
		for i in range(m):
			mileage = km_normalized[i]
			price = LM.data['price'][i]
			estimate_price = tmp_theta0 + (tmp_theta1 * mileage)
			error = estimate_price - price
			error_sum += error
			weighted_error_sum += error * mileage
		
		tmp_theta0 = tmp_theta0 - learning_rate * (1.0/m) * error_sum
		tmp_theta1 = tmp_theta1 - learning_rate * (1.0/m) * weighted_error_sum
	final_theta1 = tmp_theta1 / km_range
	final_theta0 = tmp_theta0 - (final_theta1 * km_min)
	LM.save_thetas(final_theta0, final_theta1)
	print(f"Training complete. Final values: theta0 = {LM.theta0:.4f}, theta1 = {LM.theta1:.4f}")

if __name__ == "__main__":
	ft_training()