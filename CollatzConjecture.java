public class CollatzConjecture{
	public static void main(String[] args){

		
		// I initially calculated values for 1 -> 100000 so kind of a bootleg version of memoization, haha
		long seed = 1000000;
		long max = 350;
		long maxSeed = 77031;
		long val = 0;
		while(seed > 100000){
			val = measureChain(seed, 0);
			if(val > max){
				max = val;
				maxSeed = seed;

			}
			seed--;
		}
		System.out.println("The longest chain is " + maxSeed + " of length " + max);
	}

	public static long measureChain(long num, long count){
		while(num != 1){
			if(num%2 == 0){
				num = num/2;
				count++;
			}
			else{
				num = (3 * num) + 1;
				num = num/2;
				count += 2;

			}
		}
		return count;
	}






}




