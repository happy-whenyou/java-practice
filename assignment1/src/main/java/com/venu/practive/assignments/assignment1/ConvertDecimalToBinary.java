package com.venu.practive.assignments.assignment1;

//Problem 4

public class ConvertDecimalToBinary {

	public static void main(String[] args) {
		ConvertDecimalToBinary convert = new ConvertDecimalToBinary();
		String ten_binary = convert.toBinary(10);
		System.out.println("Binary Representation of 10 is " + ten_binary);
		String twenty_binary = convert.toBinary(20);
		System.out.println("Binary Representation of 20 is " + twenty_binary);
		
	}
	
	/**
	 * Everything in computers is 1 or 0 which is known as binary.
	 * So whatever you store/write in computers is binary. 
	 * This is a simple implementation which should convert a number to its binary representation
	 * For Example : 2 should be converted to 10 
	 * 3 should be converted to 11
	 * 4 should be converted to 100
	 * @param a
	 * @return
	 */
	private String toBinary(int a) {
		// Logic
		// Divide the number by 2, check the quotient
		// If quotient is 0 then stop
		// otherwise divide the number by 2 again
		String binary = "";
		int quotient =  a / 2;
		int remainder = a % 2;
		binary = binary + remainder;
		while (quotient != 0) {
			remainder = quotient % 2;
			quotient =  quotient / 2;
			binary = remainder + binary;
		}

		return binary;
	}
}
