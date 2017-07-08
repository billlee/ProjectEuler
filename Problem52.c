#include <stdio.h>
#include <stdlib.h>


int isPermutation(int num1, int num2){
    int digits[10];
    int i;

    for(i = 0; i < 10; i++)
        digits[i] = 0;

    while(num1 != 0){
        digits[num1%10]++;
        num1 = num1/10;
    }          

    while(num2 != 0){
        digits[num2%10]--;
        num2 = num2/10;
    }
    
    for(i = 0; i < 10; i++){
        if(digits[i] > 0){
            return 0;
        }
    }
    return 1;
}

int main(){
    long i;
    int total;
    int j;
    for(i = 125874; i < 5000000; i++){
        j = 1;
        total = 1;
        while(j < 7){
            total *=  isPermutation(i,(j*i));
            j += 1;
            if(total == 0)
                break;
        }    
        if(j==7)
            printf("The number is %ld :\n", i);
    } 
    
    
    return 0;
}

