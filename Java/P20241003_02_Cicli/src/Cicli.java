import java.util.Scanner;

public class Cicli {
	public static void main(String[] args) {
		int pippo = 100;
		// TODO Auto-generated method stub
		for (int i = 0; i < 10; i++) {
			pippo = pippo + 1;
//			System.out.println(i);
		}

		for (int i = 1; i <= 10; i++) {
			int sette = 7;
			int moltiploco = i * sette;
			System.out.println(moltiploco);
		}
		for (int i = 7; i < 77; i += 7) {
			System.out.println(i);
		}
		int n = 7;
		for (int i = 0; i < 10; i++) {
			System.out.println(n);
			n += 7;
		}
		for (int i = 0; i < 70;) {
			for (int j = 0; j < 7; j++) {
				i = i + 1;
			}
			System.out.println(i);
		}
//		int ni = 7;
//		if (ni % 2 == 0) {
//			System.out.println("è pari");
//		} else {
//			System.out.println("è dispari");
//		}
		// Come leggere da tastiera
//		Scanner leggi = new Scanner(System.in);
//		int n2 = leggi.nextInt();
//		String s1 =leggi.nextLine();
		System.out.println("Inserisci un numero:");
		Scanner leggi = new Scanner(System.in);
		for (int i = 0; i <= 10; i++) {
			int n2 = leggi.nextInt();
			if (n2 > 10) {
				System.out.println("Maggiore");
			} else {
				System.out.println("Minore");
			}
		}

	}

}