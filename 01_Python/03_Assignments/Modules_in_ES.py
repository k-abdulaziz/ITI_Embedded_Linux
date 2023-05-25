import sys

# Define the list of modules with their numbers
modules = [
    ("MicroPython", "MicroPython is a lean and efficient implementation of the Python programming language optimized for microcontrollers and embedded systems. It provides a subset of the Python standard library tailored for resource-constrained environments."),
    ("RPi.GPIO", "RPi.GPIO is a library specifically designed for Raspberry Pi boards. It allows Python developers to interact with the GPIO (General Purpose Input/Output) pins, enabling control over external devices and sensors."),
    ("Adafruit CircuitPython", "Adafruit CircuitPython is an easy-to-use platform for programming microcontrollers using Python. It offers support for a wide range of microcontroller boards and peripherals, providing higher-level abstractions for interacting with sensors, displays, and other hardware components."),
    ("pySerial", "pySerial is a library that provides a way to communicate with serial ports in Python. It allows for easy integration with external devices and enables serial communication protocols commonly used in embedded systems, such as UART and SPI."),
    ("OpenCV", "OpenCV (Open Source Computer Vision Library) is widely used for computer vision applications. It provides various image processing and computer vision algorithms, making it valuable in embedded systems that require visual data analysis or object detection."),
    ("machine", "The machine module offers various classes and functions that enable control and communication with hardware peripherals, such as GPIO pins, I2C devices, SPI devices, ADC, PWM, UART, and more."),
    ("picamera", "picamera is a Python library for accessing the camera module of the Raspberry Pi. It enables capturing images and recording videos using the Raspberry Pi's camera, allowing for image processing and computer vision applications in embedded systems."),
    ("pybluez", "pybluez is a Python extension module that provides support for Bluetooth functionality. It allows developers to interact with Bluetooth devices and create applications that leverage Bluetooth communication capabilities in embedded systems."),
    ("TensorFlow Lite", "TensorFlow Lite for Microcontrollers is designed to run machine learning models on microcontrollers and other devices with only a few kilobytes of memory. The core runtime just fits in 16 KB on an Arm Cortex M3 and can run many basic models. It doesn't require operating system support, any standard C or C++ libraries, or dynamic memory allocation."),
    ("pyusb", "pyusb is a library that provides support for USB (Universal Serial Bus) communication in Python. It allows developers to interact with USB devices, send and receive data over USB interfaces, and control USB-based hardware components."),
    ("pycrypto", "pycrypto is a library that provides cryptographic functions and algorithms. It allows for encryption, decryption, secure hashing, and other cryptographic operations, which can be useful in securing data in embedded systems."),
    ("paho-mqtt", "paho-mqtt is a Python library that implements the MQTT (Message Queuing Telemetry Transport) protocol. It allows for communication with MQTT brokers, enabling publish-subscribe messaging between embedded systems and other devices or services."),
    ("pyQT", "pyQT is a Python binding for the Qt application framework. It provides a powerful toolkit for building graphical user interfaces (GUIs) in Python. Using pyQT, developers can create responsive and feature-rich user interfaces for their embedded systems applications."),
    ("pyCAN", "pyCAN is a library for working with CAN buses. It enables sending and receiving CAN messages, monitoring bus activity, and controlling CAN-based systems in embedded applications."),
    ("pyTest", "pyTest is a testing framework for Python. It allows developers to write and execute tests efficiently, helping ensure the reliability and correctness of their embedded systems applications.")
]

def show_module_info(module):
    module_name, module_description = modules[module - 1]
    print(f"\nModule: {module_name}")
    print("Description: ", module_description)

def display_modules():
    print("Welcome to the Embedded Systems Python Libraries and Modules Viewer!")
    print("====================================================================\n")
    print("Available Modules:")
    for i, (module_name, _) in enumerate(modules, 1):
        print(f"{i}. {module_name}")

def main():
    display_modules()

    while True:
        try:
            user_input = int(input("\nEnter the number of a module to view its information (or 0 to exit): "))
            if user_input == 0:
                print("Exiting the program...")
                sys.exit()

            if 1 <= user_input <= len(modules):
                show_module_info(user_input)
            else:
                print("Invalid input. Please enter a valid module number.")

        except ValueError:
            print("Invalid input. Please enter a valid module number.")

        user_choice = input("\nContinue viewing modules? (yes/no): ")
        if user_choice.lower() != "yes":
            print("Exiting the program...")
            sys.exit()

if __name__ == "__main__":
    main()