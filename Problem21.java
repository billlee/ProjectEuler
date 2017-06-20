public class Problem21{
	public static void main(String[] args){
		int temp = 0;
		int sum = 0;
		for(int i = 2; i < 10000; i++){
			temp = amicableVal(i);
			if(amicableVal(temp) == i && (temp != 1) && (temp != i)){
				sum += i;
			}
			
		}
		System.out.println(sum);
	}

	public static int amicableVal(int number){
		int sum = 1;

		for(int i = 2; i < (int)(Math.sqrt(number)); i++ ){
			if(number%i == 0){
				sum += i;
				sum += (number/i);
			}
		}
		return sum;

	}


}