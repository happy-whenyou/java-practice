public class FindModulus {

	public static void main(String[] args) {
		FindModulus findModulus = new FindModulus();
		int a = findModulus.lastDigit(100);
		System.out.println(" Last digit of number 100 is " + a);
		int b = findModulus.lastDigit(-101);
		System.out.println(" Last digit of number 101 is " + b);
		int c = findModulus.lastDigit(443482344);
		System.out.println(" Last digit of number 443482344 is " + c);
	}
	
	/**
	 * In this method we find the last digit of the passed in number
	 * For Example: if a=123 then our answer should return 3
	 * if a=10 then our answer should be 0
	 * @param a
	 * @return
	 */
	private int lastDigit(int a) {
		//TODO Actual logic here
		return 0;
	}
	
}
