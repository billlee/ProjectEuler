import java.util.*;
import java.io.*;

public class MaxPathSum{

	
	public static void main(String[] args) throws IOException{ 
		Scanner sc = new Scanner(new File("triangle.txt"));
		String[][] arr = new String[15][15];
		sc.useDelimiter("\\n");
		int p = 0;
		while(sc.hasNext()){
			String x = sc.next();
			arr[p] = x.split(" ");
			p++;
			}
		
	
		int[][] arr2=  new int[15][15];
		for(int i = 0; i<arr.length; i++){
			for(int j = 0; j < arr[i].length; j++){
				arr2[i][j] = Integer.parseInt(arr[i][j]);
			}
		}

		for(int i = arr2.length-2 ; i >= 0 ; i--){
			for(int j = 0; j <= i; j++){
				arr2[i][j] = arr2[i][j] + Math.max(arr2[i+1][j],arr2[i+1][j+1]);
			}
		}



		System.out.println(arr2[0][0]);
	}



}