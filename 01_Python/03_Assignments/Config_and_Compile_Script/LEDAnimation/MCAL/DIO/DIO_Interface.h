/**
 * @file DIO_Interface.h
 * @author Khaled Abdulaziz
 * @brief This is the interface file for the DIO module which is responsible for controlling
 *        the input/output directions and values of the microcontroller's pins and ports.
 * @version 0.1
 * @date 2023-03-29
 *
 * This interface file defines the functions that can be used to control the direction and
 * value of the microcontroller's pins and ports. It also includes some macro definitions
 * for commonly used values such as pin numbers, port numbers, and pin directions/values.
 */

#ifndef LEDANIMATION_MCAL_DIO_DIO_INTERFACE_H_
#define LEDANIMATION_MCAL_DIO_DIO_INTERFACE_H_

#include "../../LIB/STD_TYPES.h"

#define PORTA 0
#define PORTB 1
#define PORTC 2
#define PORTD 3

#define PIN0 0
#define PIN1 1
#define PIN2 2
#define PIN3 3
#define PIN4 4
#define PIN5 5
#define PIN6 6
#define PIN7 7

#define LOW 0
#define HIGH 1

#define INPUT 0
#define OUTPUT 1

#define PORT_INPUT   0x00
#define PORT_OUTPUT  0xFF
#define PORT_LOW     0x00
#define PORT_HIGH    0xFF

void DIO_voidSetPinDirection(u8 Copy_u8PortId, u8 Copy_u8PinId, u8 Copy_u8Direction);
void DIO_voidSetPinValue(u8 Copy_u8PortId, u8 Copy_u8PinId, u8 Copy_u8Value);
u8   DIO_u8GetPinValue(u8 Copy_u8PortId, u8 Copy_u8PinId);
void DIO_voidSetPortDirection(u8 Copy_u8PortId, u8 Copy_u8Direction);
void DIO_voidSetPortValue(u8 Copy_u8PortId, u8 Copy_u8Value);
u8   DIO_u8GetPortValue(u8 Copy_u8PortId);
void DIO_voidTogglePinValue(u8 Copy_u8Port, u8 Copy_u8Pin);
void DIO_voidTogglePortValue(u8 Copy_u8PortId);

#endif /* LEDANIMATION_MCAL_DIO_DIO_INTERFACE_H_ */
