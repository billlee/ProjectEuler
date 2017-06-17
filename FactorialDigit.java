import java.math.BigInteger;
public class FactorialDigit{
	
	public static void main(String[] args){
		BigInteger x = new BigInteger("1");
		for(int i = 1; i <= 100; i++){
			BigInteger y = BigInteger.valueOf(i);
			x = x.multiply(y);
		}
		System.out.println(x);
		String  y = x.toString();
		int sum = 0;
		for(int i = 0; i< y.length(); i++){
			sum += Character.getNumericValue(y.charAt(i));
		}
		System.out.println(sum);
	}	

}