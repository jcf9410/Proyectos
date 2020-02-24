#include <stdio.h>
int main (){
	int n; // numero de valores a introducir
	float max;
	float min;
	float media; 
	float suma; 
	float valor;
		
	suma = 0;
	printf( "Introduce n: ");
	scanf("%d", &n);	
	
	for (int i=0;i<n;i++){
		printf( "Introduce valor %d: ", i+1);
		scanf("%f", &valor);	
		suma = suma + valor;
		
		// inicializar min y max solo en la primera iteracion
		if (i==0){
			min = valor;
			max = valor;
		}
		else{			
			if (valor > max){
				max = valor;
			}
			else if (valor < min){
				min = valor;
			}		
		}
	}
	media = suma/n;
	
	printf("Min: %f ", min);
	printf("Max: %f ", max);
	printf("Media: %f: ", media);

	return 0;
}
