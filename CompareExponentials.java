import java.util.*;
import java.io.*;
import java.math.*;
public class CompareExponentials{
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(new File("base_exp.txt"));
		long max = 0;
		long x = 0;
		long y = 0;
		int line = 1;
		int maxLine = 1;
		sc.useDelimiter(",|\\n");
		while(sc.hasNext()){
			x = Long.parseLong(sc.next());
			y = Long.parseLong(sc.next());

			long num = (long)(y * Math.log(x));
			if(line == 1){
				max = num;
			}
			else if(num > max){
				max = num;
				maxLine = line;	

			}
			line++;
		}

		System.out.println("The max line occurs at " + maxLine);
	}


}