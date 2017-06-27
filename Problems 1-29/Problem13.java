import java.math.BigInteger;
public class Problem13{
	public static void main(String[] args){

		String[] x = new String[]{};

		System.out.println(run(x));
	}


	public static BigInteger run(String[] x){
		BigInteger y = new BigInteger("0");
		for(int i = 0; i < x.length; i++){
			BigInteger temp = new BigInteger(x[i]);
			y = y.add(temp);
		
		}
		return y;



}






}






