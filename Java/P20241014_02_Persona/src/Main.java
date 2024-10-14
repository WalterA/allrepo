
public class Main {

	public static void main(String[] args) {
		Persona pr = new Persona("Mario", "Rossi", "fasddfs", "via", "roma", "m", "1980-06-15", "4343434334");
		System.out.println(pr);
		
		System.out.println(Somma(1,2));
		System.out.println(Somma("1","2"));
	}

	static int Somma(int a, int b) {
		return a + b;
	}

	static String Somma(String a, String b) {
		return a + b;
	}
	
}