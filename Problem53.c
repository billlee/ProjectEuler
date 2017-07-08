#include <stdio.h>
#include <stdlib.h>


double choose(int n, int r){
    double result = 1;
    double divisor = 1;
    int difference = n-r;
    int i;
    if ( r > difference){
        for(i = n; i != r; i--){
            result *= i;
        }    
        for( i = 1; i <= difference; i++){
            divisor *=i;
        }
    }
    else{
        for(i = n; i != difference; i--){
            result *= i; 
        }
        for(i = 1; i <= r; i++){
            divisor *= i;
        }
    }
    
    
    return (result/divisor);
}


int main(){
    int i;
    int j = 1;
    int counter = 0;
    for (i=2; i <= 100; i++){
        for(j=1; j <= i; j++){
            if(choose(i,j) > 1000000){
                counter ++;
            }
        }
   
    }
    printf("%d \n", counter);
    return 0;

}


