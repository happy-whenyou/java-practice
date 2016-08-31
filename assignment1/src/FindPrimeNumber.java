public class FindPrimeNumber {

	public static void main(String[] args) {
		FindPrimeNumber find_is_prime = new FindPrimeNumber();
		boolean a = find_is_prime.isPrime(7);
		System.out.println(" 7 is a prime number " + a);
		boolean a1 = find_is_prime.isPrime(1237);
		System.out.println(" 1237 is a prime number " + a1);
		boolean a2 = find_is_prime.isPrime(99);
		System.out.println(" 99 is a prime number " + a2);
	}
	
	
	/**
	 * Used to find whether the passed in number is a prime
	 * number of not.
	 * @param a
	 * @return
	 */
	private boolean isPrime(int a) {
		//TODO Actual logic here
		return false;
	}
	
}
