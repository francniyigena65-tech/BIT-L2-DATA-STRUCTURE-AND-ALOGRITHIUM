import array
# --- Integers ---
# Sample honey weights (in kg) collected from different hives
honey_weights = [12, 15, 10, 18, 20, 14]
total_weight = sum(honey_weights)
average_weight = total_weight / len(honey_weights)
min_weight = min(honey_weights)
max_weight = max(honey_weights)
print("=== Integer Calculations ===")
print(f"Total honey collected: {total_weight} kg")
print(f"Average honey per hive: {average_weight:.2f} kg")
print(f"Minimum honey collected: {min_weight} kg")
print(f"Maximum honey collected: {max_weight} kg\n")
# --- Strings ---
report = (f"Beekeeping Honey Report\n"
    f"Total honey: {total_weight} kg\n"
    f"Average per hive: {average_weight:.2f} kg\n")
print("=== String Report ===")
print(report)
# --- Booleans ---
threshold = 14
if (average_weight > threshold) and (max_weight >= 18):
    status = "Above Standard"
else:
    status = "Below Standard"
    print("=== Boolean Condition ===")
print(f"Average check: {status}\n")
# --- Lists ---
print("=== List Operations ===")
print("Original list:", honey_weights)
# Add a new record
honey_weights.append(16)
# Remove the smallest if below threshold
honey_weights = [w for w in honey_weights if w >= 12]
# Sort the list
honey_weights.sort()
print("Modified list:", honey_weights, "\n")
# --- Arrays ---
print("=== Array Operations ===")
# Create an array with a subset (first 4 hives)
honey_array = array.array("i", [12, 15, 10, 18])
array_sum = sum(honey_array)
print("Array values:", honey_array.tolist())
print("Array sum:", array_sum)
print("Compare with list sum:", sum(honey_weights), "\n")
# --- Dictionaries ---
print("=== Dictionary Records ===")
honey_records = [{"id": 1, "name": "Hive A", "value": 12},
    {"id": 2, "name": "Hive B", "value": 15},
    {"id": 3, "name": "Hive C", "value": 10},]
# Update Hive B's value
for rec in honey_records:
   if rec["id"] == 2:rec["value"] = 17
# Delete Hive C
honey_records = [rec for rec in honey_records if rec["id"] != 3]
# Compute total value
total_value = sum(rec["value"] for rec in honey_records)
print("Records:", honey_records)
print("Total honey from records:", total_value)