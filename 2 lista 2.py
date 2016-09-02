ALGORITIMO "contador"

contador regular <-- 0
contador bom <-- 0
contador otimo <-- 0

PARA i <-- 0 ATE 10 FAÇA

DECLARE opinião NUMERAL

ESCREVA Digite sua opinião sobre o filme com as alternativa abaixo:
ESCREVA 3 - otimo, 2 - bom, 1 regular

LEIA opinião NUMERAL
SE opinião = 1
	ENTÃO contador regular <-- contador regular +1
SENÃO opinião = 2
	ENTÃO bom contador bom <-- contador regular +1
ENTÃO
	ENTÃO contador otimo <-- contador regular +1

ESCREVA contador regular
ESCREVA contador bom
ESCREVA contador otimo

FIM_ALGORITIMO
