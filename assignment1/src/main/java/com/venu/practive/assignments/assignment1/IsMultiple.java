package com.venu.practive.assignments.assignment1;

public class IsMultiple {

	public static void main(String[] args) {
		IsMultiple is_multiple = new IsMultiple();
		boolean a = is_multiple.findIsMultipleOfDigit(30, 5);
		System.out.println(" 30 is a multiple of 5 " + a);
		boolean a1 = is_multiple.findIsMultipleOfDigit(127, 11);
		System.out.println(" 127 is a multiple of 11 " + a1);
		boolean a2 = is_multiple.findIsMultipleOfDigit(8998, 2);
		System.out.println(" 8998 is a multiple of 2 " + a2);
	}
	
	
	/** 
	 * This method should be used to find whether an integer
	 * is a multiple of another integer
	 * is even or not. 
	 * @param a
	 * @return
	 */
	private boolean findIsMultipleOfDigit(int numberToTest, int multiple) {
		//TODO - Fill in the actual logic here
		return true;
	}

}
