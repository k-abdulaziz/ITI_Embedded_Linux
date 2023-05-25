/**
 * @file LED_Interface.h
 * @author Khaled Abdulaziz 
 * @brief 
 * @version 0.1
 * @date 2023-05-23
 * 
 * 
 */

#ifndef LEDANIMATION_HAL_LED_LED_INTERFACE_H_
#define LEDANIMATION_HAL_LED_LED_INTERFACE_H_

#include "../../LIB/STD_TYPES.h"

void LED_voidInit(void);
void LED_voidTurnON(u8 Copy_u8LED_Port, u8 Copy_u8LED_No);
void LED_voidTurnOFF(u8 Copy_u8LED_Port, u8 Copy_u8LED_No);

#endif /* LEDANIMATION_HAL_LED_LED_INTERFACE_H_ */
