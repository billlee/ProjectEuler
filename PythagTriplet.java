public class PythagTriplet{
	public static void main(String[] args){
		int a = 1;
		int b = 2; 
		int c = 3;

		run(a,b,c);
			

	}

	public static int run(int a, int b, int c){
	while(a < 333){
			while(b >= a && b < 1000){
				while(c >= b && c <1000){
					if(isTriplet(a,b,c)){
						System.out.println(a + " " + b + " " + c);
						return 0;
					}
					c++;
				}
				c = b+1;
				b++;
			}
			b = a+1;
			a++;
		}
		return 0;
	}


	public static boolean isTriplet(int a, int b, int c){
		return ((c*c) == ((a*a) + (b*b))) && ((a+b+c)== 1000);
	}
		}

