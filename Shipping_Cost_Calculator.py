# Shipping Cost Calculator

## Iput package weight and shipping rate
weight = float(input("Enter package weight in kilograms :"))
rate = float(input("Enter shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * cost

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
