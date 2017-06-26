import java.util.*;
import java.math.BigInteger;
public class Problem48{
	public static void main(String[] args){
		BigInteger sum = new BigInteger("0");
		BigInteger mod = new BigInteger("100000000000000000000000");
		for(int i = 1; i <= 1000; i++){
			BigInteger x = BigInteger.valueOf(i);
			BigInteger num = x.modPow(x, mod);
			sum = sum.add(num);
		}
	System.out.println("Here we go " + sum); 
	}

}