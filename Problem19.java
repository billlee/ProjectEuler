public class Problem19{
	public static void main(String[] args){

	int modVal = 1; 
	int x = 0;
	int counter = 0;
	for(int year = 1901; year <= 2000; year++ ){
		for(int month = 1; month <= 12; month++){
			x = findDays(month, year);
			if((x+modVal)%7 == 6){ counter++; }
			modVal = (x+modVal)%7;
		}
	}

	System.out.println(counter + " hahahah ");

	}

	public static int february(int year){
		if((year%4 == 0 && year%100 != 0) || year%400 == 0){	
			return 29;
		}
		else{
			return 28;
		}


	}

	public static int findDays(int month, int year){
		switch(month){
			case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                return 31;
            case 4:
            case 6:
            case 9:
            case 11:
                return 30;
            case 2:
            	return february(year);

		}
		return 0;
	}

}