/**
 * @file LED_Program.c
 * @author Khaled Abdulaziz 
 * @brief 
 * @version 0.1
 * @date 2023-04-03
 * 
 * 
 */

#include "../../LIB/STD_TYPES.h"
#include "../../LIB/BIT_MATH.h"

#include "../../MCAL/DIO/DIO_Interface.h"

#include "LED_Interface.h"
#include "LED_Private.h"
#include "LED_Config.h"

void LED_voidInit(void)
{
	DIO_voidSetPortDirection(LEDS_PORT, PORT_OUTPUT);
}

void LED_voidTurnON(u8 Copy_u8LED_Port, u8 Copy_u8LED_No)
{
	DIO_voidSetPinValue(Copy_u8LED_Port, Copy_u8LED_No, LED_HIGH);
}

void LED_voidTurnOFF(u8 Copy_u8LED_Port, u8 Copy_u8LED_No)
{
	DIO_voidSetPinValue(Copy_u8LED_Port, Copy_u8LED_No, LED_LOW);
}
