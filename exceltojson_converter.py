import pandas as pd
import json

# Read the Excel file
excel_file = 'Participants_List.xlsx' 
df = pd.read_excel(excel_file)

# Convert the DataFrame to a list of dictionaries
data = df['Name'].apply(lambda x: {"name": x}).tolist()

# Convert the list of dictionaries to a JSON string
json_data = json.dumps(data, indent=4)

# Save the JSON data to a file
json_file = 'participants.json' 
with open(json_file, 'w') as f:
    f.write(json_data)

print("JSON file created successfully!")
