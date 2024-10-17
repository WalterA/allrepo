

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
		//1)calcolare il numero totale di caloria assunte con questo pranzo
		//2)costruire a partire da questo pranzo un pranzo pre 50 persone
		//dove ogni portata è composta da tre cibi presi a caso da questo array
		//esempio se pranzo dosse di 5 elementi ,allora una portata del pranzo per 50 persone
		//sara composta di tre elementi di pranzo presi a caso 
		/*
		 * difficolta:
		 * il pranzo di 50 persone e un arrey di pranzi dove ogni singolo pranto contiene tre portate . come fare?
		 * esempio
		 * supponiamo che pranzo sia composto da solo elenco per l'esempio
		 * [(pasta e ceci, lombata , sogliola, pesce persico,delizia al limone , carciofi , pasta al forno, creme brulee, carbonara]
		 * io intendo realizzare un pranzo per 50 persone del tipo persona 1 persona 2 persona 3 
		 * persona1 pasta e ceci
		 * persona 2 pasta al forno
		 * persona 3 carbonara
		 * persona 1 sogliola 
		 * persona 2 sogliola 
		 * persona 3 lombata 
		 * persona 1 creme brulee
		 * persona 2 limone
		 * persona 3 carciofi 
		 */
	}

}
