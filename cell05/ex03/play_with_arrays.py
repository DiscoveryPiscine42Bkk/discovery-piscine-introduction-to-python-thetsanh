original_array = [2, 8, 9, 48, 8, 22, -12, 2]
print(original_array)
filtered = [x for x in original_array if x > 5]
processed = [x + 2 for x in filtered]
unique_processed = list(set(processed))
print(unique_processed)
