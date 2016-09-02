ALGORITIMO "media"

DECLARE N1 , N2 , N3, media REAL

LEIA N1 , N2 , N3 REAL
media <-- N1 + N2 + N3 / 3

SE media <= 3,9
	ESCREVA reprovado

ENTÃO media <= 6,9
	ESCREVA prova final

SENÃO
	ESCREVA aprovado

FIM_ALGORITIMO