import java.util.*;
import java.io.*;


public class Problem11{
	
	public static void main(String[] args) throws IOException{
	Scanner sc = new Scanner(new File("grid.txt"));
	int[][] grid = new int[20][20];
	while(sc.hasNext()){
		for(int i = 0; i < 20; i++){
			for(int j = 0; j < 20; j++){
				grid[i][j] = Integer.parseInt(sc.next());
				System.out.println(grid[i][j]);
			}
		}
	}

		int  x = traverseDiag(grid);
		int  y = traverseHoriVert(grid);
		System.out.println ( x  + " or " + y );

	}


	public static int traverseHoriVert(int[][] x){
		int max = 0;
		max = x[0][0];
		for(int i = 0; i < 20; i++){
			for(int j = 0 ; j <17; j++){
				int temp = x[i][j]*x[i][j+1]*x[i][j+2]*x[i][j+3];
				if(temp > max){
					max = temp;
				}
			}
		}

		for(int i = 0; i < 17; i++){
			for(int j = 0 ; j <20; j++){
				int temp = x[i][j]*x[i+1][j]*x[i+2][j]*x[i+3][j];
				if(temp > max){
					max = temp;
				}
			}
		}

		return max;

	} 


	public static int traverseDiag(int[][] x){
		int max = 0;
		max = x[0][0];
		for(int i = 0; i < 17; i++){
			for(int j = 0 ; j < 17; j++){
				int temp = x[i][j]*x[i+1][j+1]*x[i+2][j+2]*x[i+3][j+3];
				if(temp > max){
					max = temp;
				}
			}
		}

		for(int i = 0; i <17 ; i++){
			for(int j = 19; j >= 3; j--){
				int temp = x[i][j]*x[i+1][j-1]*x[i+2][j-2]*x[i+3][j-3];
				if(temp > max){
					max = temp;
				}
			}
		}
		return max;
	}









}








