import java.math.BigInteger;
public class Problem16{
	
	public static void main(String[] args){
		BigInteger large = new BigInteger("2");
		large = large.pow(1000);
		String x = large.toString();
		char a = '0';
		int sum = 0;

		for(int i = 0; i < x.length(); i++){
			a = x.charAt(i);
			int y = Character.getNumericValue(a);
			sum += y;
		}


		System.out.println("wow, this is " +large);
		System.out.println("the sum of the digits is " + sum);
	}
}