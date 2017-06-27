public class Problem12{
	
	public static void main(String[] args){


		//need to generate the list of triangular numbers 

		int x = 0;

		for(int i = 1; i <= 1000000; i++){
			x += i;  
			if(x > 1 && hasDivisors(x)){
				System.out.println(x);
				break;
			}
		}

	}

	public static boolean hasDivisors(int x){
		int temp = 0; 
		for(int i = 2; i <= Math.sqrt(x); i++){
			if(x % i == 0){
				temp++;
			}
		}

		if(temp >= 250){
			return true;
		}
		return false;
	}

}