import csv
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_directory, 'LEDAnimation', 'ETC', 'User_Configs.csv')
config_file_path = os.path.join(current_directory, 'LEDANIMATION', 'HAL', 'LED', 'LED_Config.h')

with open(csv_file_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)
        leds_port = row['LEDS PORT']
        led_pins = [row[f'LED{i} PIN'] for i in range(1, 9)]
