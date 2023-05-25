/**
 * @file Program.c
 * @author Khaled Abdulaziz
 * @brief This is the implementation file for the DIO module which is responsible for controlling
 *        the DIO_INPUT/DIO_OUTPUT directions and values of the microcontroller's pins and ports.
 * @version 0.1
 * @date 2023-03-29
 *
 *
 */

#include "../../LIB/STD_TYPES.h"
#include "../../LIB/BIT_MATH.h"

#include "DIO_Interface.h"
#include "DIO_Private.h"
#include "DIO_Config.h"

void DIO_voidSetPinDirection(u8 Copy_u8PortId, u8 Copy_u8PinId, u8 Copy_u8Direction)
{
    if ((Copy_u8PortId <= PORTD) && (Copy_u8PortId >= PORTA))
    {
        if ((Copy_u8PinId <= PIN7) && (Copy_u8PinId >= PIN0))
        {
            switch (Copy_u8Direction)
            {
            case OUTPUT:
            {
                switch (Copy_u8PortId)
                {
                case PORTA:
                    SET_BIT(DIO_DDRA, Copy_u8PinId);
                    break;
                case PORTB:
                    SET_BIT(DIO_DDRB, Copy_u8PinId);
                    break;
                case PORTC:
                    SET_BIT(DIO_DDRC, Copy_u8PinId);
                    break;
                case PORTD:
                    SET_BIT(DIO_DDRD, Copy_u8PinId);
                    break;
                default:
                    /* Error handling */
                    break;
                }
                break;
            }
            case INPUT:
            {
                switch (Copy_u8PortId)
                {
                case PORTA:
                    CLEAR_BIT(DIO_DDRA, Copy_u8PinId);
                    break;
                case PORTB:
                    CLEAR_BIT(DIO_DDRB, Copy_u8PinId);
                    break;
                case PORTC:
                    CLEAR_BIT(DIO_DDRC, Copy_u8PinId);
                    break;
                case PORTD:
                    CLEAR_BIT(DIO_DDRD, Copy_u8PinId);
                    break;
                default:
                    /* Error handling */
                    break;
                }
                break;
            }
            default:
            {
                /* Error Handling  */
                break;
            }
            }
        }
        else
        {
            /* Error Handling */
        }
    }
    else
    {
        /* Error Handling */
    }
}

void DIO_voidSetPinValue(u8 Copy_u8PortId, u8 Copy_u8PinId, u8 Copy_u8Value)
{
    if ((Copy_u8PortId <= PORTD) && (Copy_u8PortId >= PORTA))
	{
		if ((Copy_u8PinId <= PIN7) && (Copy_u8PinId >= PIN0))
        {
            switch (Copy_u8Value)
            {
            case HIGH:
            {
                switch (Copy_u8PortId)
                {
                case PORTA:
                    SET_BIT(DIO_PORTA, Copy_u8PinId);
                    break;
                case PORTB:
                    SET_BIT(DIO_PORTB, Copy_u8PinId);
                    break;
                case PORTC:
                    SET_BIT(DIO_PORTC, Copy_u8PinId);
                    break;
                case PORTD:
                    SET_BIT(DIO_PORTD, Copy_u8PinId);
                    break;
                default:
                    /* Error handling */
                    break;
                }
                break;
            }
            case LOW:
            {
                switch (Copy_u8PortId)
                {
                case PORTA:
                    CLEAR_BIT(DIO_PORTA, Copy_u8PinId);
                    break;
                case PORTB:
                    CLEAR_BIT(DIO_PORTB, Copy_u8PinId);
                    break;
                case PORTC:
                    CLEAR_BIT(DIO_PORTC, Copy_u8PinId);
                    break;
                case PORTD:
                    CLEAR_BIT(DIO_PORTD, Copy_u8PinId);
                    break;
                default:
                    /* Error handling */
                    break;
                }
                break;
            }
            default:
            {
                /* Error Handling  */
                break;
            }
            }
        }
        else
        {
            /* Error Handling */
        }
    }
    else
    {
        /* Error Handling */
    }
}

u8   DIO_u8GetPinValue(u8 Copy_u8PortId, u8 Copy_u8PinId)
{
    u8 Local_u8Variable = LOW;
    if ((Copy_u8PortId <= PORTD) && (Copy_u8PortId >= PORTA))
    {
        if ((Copy_u8PinId <= PIN7) && (Copy_u8PinId >= PIN0))
        {
            switch (Copy_u8PortId)
            {
            case PORTA:
                Local_u8Variable = GET_BIT(DIO_PINA, Copy_u8PinId);
                break;
            case PORTB:
                Local_u8Variable = GET_BIT(DIO_PINB, Copy_u8PinId);
                break;
            case PORTC:
                Local_u8Variable = GET_BIT(DIO_PINC, Copy_u8PinId);
                break;
            case PORTD:
                Local_u8Variable = GET_BIT(DIO_PIND, Copy_u8PinId);
                break;
            default:
                /* do nothing */
                break;
            }
        }
        else
        {
            /* Error Handling */
        }
    }
    else
    {
        /* Error Handling */
    }
    return Local_u8Variable;
}

void DIO_voidSetPortDirection(u8 Copy_u8PortId, u8 Copy_u8Direction)
{
    if ((Copy_u8PortId <= PORTD) && (Copy_u8PortId >= PORTA))
    {
        switch (Copy_u8Direction)
        {
        case PORT_OUTPUT:
        {
            switch (Copy_u8PortId)
            {
            case PORTA:
                SET_REG(DIO_DDRA);
                break;
            case PORTB:
                SET_REG(DIO_DDRB);
                break;
            case PORTC:
                SET_REG(DIO_DDRC);
                break;
            case PORTD:
                SET_REG(DIO_DDRD);
                break;
            default:
                /* Error handling */
                break;
            }
            break;
        }
        case PORT_INPUT:
        {
            switch (Copy_u8PortId)
            {
            case PORTA:
                CLEAR_REG(DIO_DDRA);
                break;
            case PORTB:
                CLEAR_REG(DIO_DDRB);
                break;
            case PORTC:
                CLEAR_REG(DIO_DDRC);
                break;
            case PORTD:
                CLEAR_REG(DIO_DDRD);
                break;
            default:
                /* Error handling */
                break;
            }
            break;
        }
        default:
        {
            /* Error Handling  */
            break;
        }
        }
    }
    else
    {
        /*Error Handling*/
    }
}

void DIO_voidSetPortValue(u8 Copy_u8PortId, u8 Copy_u8Value)
{
    if ((Copy_u8PortId <= PORTD) && (Copy_u8PortId >= PORTA))
    {
        if ((Copy_u8Value <= PORT_HIGH) && (Copy_u8Value >= PORT_LOW))
        {
        switch (Copy_u8PortId)
            {
            case PORTA:
            	DIO_PORTA = Copy_u8Value;
                break;
            case PORTB:
            	DIO_PORTB = Copy_u8Value;
                break;
            case PORTC:
            	DIO_PORTC = Copy_u8Value;
                break;
            case PORTD:
            	DIO_PORTD = Copy_u8Value;
                break;
            default:
                /* Error handling */
                break;
            }
        }
        else
        {
            /* Error Handling */
        }
    }
    else
    {
        /*Error Handling*/
    }
}

u8   DIO_u8GetPortValue(u8 Copy_u8PortId)
{
    u8 Local_u8Variable = 0;

    if ((Copy_u8PortId <= PORTD) && (Copy_u8PortId >= PORTA))
    {
        switch (Copy_u8PortId)
        {
        case PORTA:
            Local_u8Variable = GET_REG(DIO_PINA);
            break;
        case PORTB:
            Local_u8Variable = GET_REG(DIO_PINB);
            break;
        case PORTC:
            Local_u8Variable = GET_REG(DIO_PINC);
            break;
        case PORTD:
            Local_u8Variable = GET_REG(DIO_PIND);
            break;
        default:
            /* do nothing */
            break;
        }
    }
    else
    {
        /*Error Handling*/
    }
    return Local_u8Variable;
}

void DIO_voidTogglePinValue(u8 Copy_u8PortId, u8 Copy_u8PinId)
{
    if ((Copy_u8PortId <= PORTD) && (Copy_u8PortId >= PORTA))
    {
        if ((Copy_u8PinId <= PIN7) && (Copy_u8PinId >= PIN0))
        {
            switch(Copy_u8PortId)
            {
                case PORTA:
                    TOGGLE_BIT(DIO_PORTA, Copy_u8PinId); // set pin value to low
                    break;

                case PORTB:
                    TOGGLE_BIT(DIO_PORTB, Copy_u8PinId); // set pin value to low
                    break;

                case PORTC:
                    TOGGLE_BIT(DIO_PORTC, Copy_u8PinId); // set pin value to low
                    break;

                case PORTD:
                    TOGGLE_BIT(DIO_PORTD, Copy_u8PinId); // set pin value to low
                    break;

                default:
                    // Do nothing, invalid port
                    break;
            }
        }
    }
}

void DIO_voidTogglePortValue(u8 Copy_u8PortId)
{
    if ((Copy_u8PortId <= PORTD) && (Copy_u8PortId >= PORTA))
    {
        switch (Copy_u8PortId)
        {
        case PORTA:
            TOGGLE_REG(DIO_PORTA);
            break;

        case PORTB:
            TOGGLE_REG(DIO_PORTB);
            break;

        case PORTC:
            TOGGLE_REG(DIO_PORTC);
            break;

        case PORTD:
            TOGGLE_REG(DIO_PORTD);
            break;

        default:
            // Do nothing, invalid port
            break;
        }
    }
}
