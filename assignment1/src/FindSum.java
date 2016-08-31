public class FindSum {

	public static void main(String[] args) {
		FindSum findSum = new FindSum();
		int one_to_ten = findSum.addMe(1, 100);
		System.out.println("Sum is " + one_to_ten);
		int minus_one_to_ten = findSum.addMe(-1, 10);
		System.out.println("Sum is " + minus_one_to_ten);
		int minus_two_to_minus_two = findSum.addMe(-2, -2);
		System.out.println("Sum is " + minus_two_to_minus_two);
	}
	
	
	/**
	 * This method adds all the numbers lying between the given input numbers
	 * e.g. if a=1 and b=3 then it would return 6 (1+2+3)
	 * 
	 * @param a
	 * @param b
	 * @return
	 */
	private int addMe(int a, int b) {
		//TODO - Fill in the actual logic here
		return 0;
	}
	
}
