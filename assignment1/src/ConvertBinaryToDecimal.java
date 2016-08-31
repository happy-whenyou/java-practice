//Problem 5
public class ConvertBinaryToDecimal {

	public static void main(String[] args) {
		ConvertBinaryToDecimal convert = new ConvertBinaryToDecimal();
		int d1 = convert.toDecimal("1010");
		System.out.println("Decimal Representation of 1010 is " + d1);
		int d2 = convert.toDecimal("10100");
		System.out.println("Decimal Representation of 10100 is " + d2);
		
	}
	
	/**
	 * Everything in computers is 1 or 0 which is known as binary.
	 * So whatever you store/write in computers is binary. 
	 * This is a simple implementation which should convert a number to its binary representation
	 * For Example : 10 should be converted to 2 
	 * 11 should be converted to 3
	 * 100 should be converted to 4
	 * @param a
	 * @return
	 */
	private int toDecimal(String a) {
		//TODO Actual Logic here;
		return 0;
	}

}
