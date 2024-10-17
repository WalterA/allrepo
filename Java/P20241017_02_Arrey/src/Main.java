

public class Main {

	public static void main(String[] args) {
		/*
		 * istanziamo una classe cibo con attributi che decidere voi
		 * istanziamo un arrey di 10 cibi (che sarebbe il pranzo o cena)
		 * 
		 */
		Cibo[] pranzo = new Cibo[10];
		for (int i=0; i<pranzo.length; i++) {
			pranzo[i]=(Cibo)salva.Parse(Cibo.class);
		}
		for (int i=0; i<pranzo.length;i++) {
			System.out.println(pranzo[i]);
		}
	}

}
