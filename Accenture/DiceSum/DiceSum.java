import java.util.Scanner;
class DiceSum {
	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		int x=input.nextInt(),count=0;
		input.close();
		for (int i=1;i<=6;i++) {
			if ( (x-i)<=6 && (x-i)>=1 ) {
				count++;
			}
		}System.out.println(count);
	}
}
