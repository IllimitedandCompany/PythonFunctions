import tkinter as tk
import json

def save_to_json():
    # Get the values from the input fields
    metaCloud_value = metaCloud_entry.get()
    brokerAccount_value = brokerAccount_entry.get()
    brokerPassword_value = brokerPassword_entry.get()
    brokerServer_value = brokerServer_entry.get()

    # Create a dictionary with the entered values
    data = {
        'metaCloud': metaCloud_value,
        'brokerAccount': brokerAccount_value,
        'brokerPassword': brokerPassword_value,
        'brokerServer': brokerServer_value
    }

    # Save the data to a JSON file
    with open('config.json', 'w') as json_file:
        json.dump(data, json_file)

# Create the main window
window = tk.Tk()
window.title("Configuration")

# Create labels and input fields
metaCloud_label = tk.Label(window, text="MetaCloud:")
metaCloud_label.pack()
metaCloud_entry = tk.Entry(window)
metaCloud_entry.pack()

brokerAccount_label = tk.Label(window, text="Broker Account:")
brokerAccount_label.pack()
brokerAccount_entry = tk.Entry(window)
brokerAccount_entry.pack()

brokerPassword_label = tk.Label(window, text="Broker Password:")
brokerPassword_label.pack()
brokerPassword_entry = tk.Entry(window, show="*")  # Password entry
brokerPassword_entry.pack()

brokerServer_label = tk.Label(window, text="Broker Server:")
brokerServer_label.pack()
brokerServer_entry = tk.Entry(window)
brokerServer_entry.pack()

# Create the save button
save_button = tk.Button(window, text="Save", command=save_to_json)
save_button.pack()

# Start the Tkinter main loop
window.mainloop()
