import java.util.*;
public  class Problem10{
	
	public static void main(String[] args){


		ArrayList<Integer> collezioni = new ArrayList<Integer>();

		collezioni.add(2);
		collezioni.add(3);
		boolean isPrime = true;


		for(int i = 4 ; i < 2000000; i++){
			int val = (int)Math.sqrt(i);

			for(int j =0; j < collezioni.size() && collezioni.get(j) <= val ; j++){
				if(i%collezioni.get(j) == 0){
					isPrime = false;
					break;
				}
			}
			if(isPrime){
				collezioni.add(i);
			}
			isPrime = true;
		}

		long sum = 0;
		for(int x : collezioni){
			sum +=x;
		}
		System.out.print(" The sum is equal to " + sum);


	}

}