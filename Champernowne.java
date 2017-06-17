import java.lang.StringBuilder;

public class Champernowne{
	public static void main(String[] args){
		StringBuilder sb = new StringBuilder(3000000);


		for(int i = 1; i <= 1000000; i++){
			sb.append(i);
		}

		String x = sb.toString();


		int d1 = Character.getNumericValue(x.charAt(0));
		int d2 = Character.getNumericValue(x.charAt(9));
		int d3 = Character.getNumericValue(x.charAt(99));
		int d4 = Character.getNumericValue(x.charAt(999));
		int d5 = Character.getNumericValue(x.charAt(9999));
		int d6 = Character.getNumericValue(x.charAt(99999));
		int d7 = Character.getNumericValue(x.charAt(999999));

		int total = d1 * d2 * d3 * d4 * d5 * d6 * d7;
		System.out.println(total);
	}
}