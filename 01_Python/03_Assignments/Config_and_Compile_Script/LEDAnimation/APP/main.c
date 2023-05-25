/*
 * main.c
 *
 *  Created on: Mar 27, 2023
 *      Author: khale
 */
#define F_CPU 8000000UL

#include <util/delay.h>

#include "../HAL/LED/LED_Config.h"
#include "../MCAL/DIO/DIO_Interface.h"
#include "../HAL/LED/LED_Interface.h"

int main(void)
{
	LED_voidInit();
	s8 LEDS_Arr[] = {LED1, LED2, LED3, LED4, LED5, LED6, LED7, LED8};
	while (1)
	{
		for (int i = 0; i < 4; i++)
		{
			LED_voidTurnON(LEDS_PORT, LEDS_Arr[i]);
			LED_voidTurnON(LEDS_PORT, LEDS_Arr[7 - i]);
			_delay_ms(300);
			LED_voidTurnOFF(LEDS_PORT, LEDS_Arr[i]);
			LED_voidTurnOFF(LEDS_PORT, LEDS_Arr[7 - i]);
		}
		for (int i = 2; i > 0; i--)
		{
			LED_voidTurnON(LEDS_PORT, LEDS_Arr[i]);
			LED_voidTurnON(LEDS_PORT, LEDS_Arr[7 - i]);
			_delay_ms(300);
			LED_voidTurnOFF(LEDS_PORT, LEDS_Arr[i]);
			LED_voidTurnOFF(LEDS_PORT, LEDS_Arr[7 - i]);
		}
	}
	return 0;
}
