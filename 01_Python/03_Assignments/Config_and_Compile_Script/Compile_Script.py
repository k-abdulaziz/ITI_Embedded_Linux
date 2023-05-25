import csv
import os
import subprocess


def get_avr_tool_path(tool_name):
    avr_tool_path = os.path.join('C:', os.sep, 'avr-gcc', 'bin', tool_name)
    if not os.path.exists(avr_tool_path):
        raise FileNotFoundError(f"{tool_name} not found at {avr_tool_path}")
    return avr_tool_path


def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_directory, 'LEDAnimation', 'ETC', 'User_Configs.csv')
    config_file_path = os.path.join(current_directory, 'LEDANIMATION', 'HAL', 'LED', 'LED_Config.h')

    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            leds_port = row['LEDS PORT']
            led_pins = [row[f'LED{i} PIN'] for i in range(1, 9)]

    with open(config_file_path, 'w') as config_file:
        config_file.write(f'''/**
    * @file LED_Config.h
    * @brief 
    *version 0.1
    * @date 2023-04-03
    * 
    * 
    */

    #ifndef LEDANIMATION_HAL_LED_LED_CONFIG_H_
    #define LEDANIMATION_HAL_LED_LED_CONFIG_H_

    #define LEDS_NUM 8

    #define LED1  {led_pins[0]}
    #define LED2  {led_pins[1]}
    #define LED3  {led_pins[2]}
    #define LED4  {led_pins[3]}
    #define LED5  {led_pins[4]}
    #define LED6  {led_pins[5]}
    #define LED7  {led_pins[6]}
    #define LED8  {led_pins[7]}

    #define LEDS_PORT  {leds_port}

    #endif /* LEDANIMATION_HAL_LED_LED_CONFIG_H_ */
    ''')

    print("LED_Config.h file updated successfully.")

    source_files = [
        os.path.join(current_directory, 'LEDANIMATION', 'MCAL', 'DIO', 'DIO_Program.c'),
        os.path.join(current_directory, 'LEDANIMATION', 'HAL', 'LED', 'LED_Program.c'),
        os.path.join(current_directory, 'LEDANIMATION', 'APP', 'main.c')
    ]

    debug_directory = os.path.join(current_directory, 'LEDANIMATION', 'DEBUG')
    if not os.path.exists(debug_directory):
        os.makedirs(debug_directory)

    mcu = 'atmega32a'
    elf_file = os.path.join(debug_directory, 'LEDAnimation.elf')
    hex_file = os.path.join(debug_directory, 'LEDAnimation.hex')
    flags = ['-mmcu=' + mcu, '-Os', '-o', elf_file]

    try:
        compiler_path = get_avr_tool_path('avr-gcc.exe')
        subprocess.check_output([compiler_path] + flags + source_files)
        print('Code compiled successfully.')
    except subprocess.CalledProcessError as e:
        print('Error: Code compilation failed.')
        print('Command output:', e.output.decode())
    except FileNotFoundError as e:
        print(e)

    try:
        objcopy_path = get_avr_tool_path('avr-objcopy.exe')
        subprocess.check_output([objcopy_path, '-O', 'ihex', elf_file, hex_file])
        print('.hex file generated successfully.')
    except subprocess.CalledProcessError as e:
        print('Error: Generating .hex file failed.')
        print('Command output:', e.output.decode())
    except FileNotFoundError as e:
        print(e)


if __name__ == '__main__':
    main()