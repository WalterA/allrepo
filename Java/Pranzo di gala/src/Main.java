
public class Main {

	public static void main(String[] args) {
		/*
		 * Creiamo una classe Cibo con gli attributi che deciderete voi Creiamo un array
		 * di 10 Cibi (che sarebbe il pranzo o la cena)
		 */

		Cibo[] menu = new Cibo[5];
		for (int i = 0; i < menu.length; i++) {
			menu[i] = (Cibo) ParseClas.Parse("Cibo");
		}

		for (int i = 0; i < menu.length; i++) {
			System.out.println(menu[i]);
		}

		// 1) Calcolare il numero totale di calorie assunte con questo menu
		double totaleCalorie = 0.0;
		for (int i = 0; i < menu.length; i++) {
			totaleCalorie += menu[i].getCalorie();
		}
		System.out.println(totaleCalorie);
		// 2) Costruire a partire da questo menu un pranzo per 50 persone,
		// dove ogni portata è composta da tre cibi presi a caso da questo menu
		// Esempio, se menu fosse di 5 elementi, allora una
		// portata del pranzo per 50 persone
		// sarà composta di tre elementi di menu presi a caso
		/*
		 * Difficoltà: Il pranzo di 50 persone è un array di pranzi dove ogni singolo
		 * pranzo contiene tre portate. Come fare?
		 *
		 * Altro esempio Supponiamo che menu sia composto da (elenco solo i nomi delle
		 * pietanze, senza indicare calorie o quant'altro, per semplicità di lettura
		 * dell'esempio stesso [pasta e ceci, lombata, sogliola, pesce persico, delizia
		 * al limone, carciofi, pasta al forno, creme brulee, carbonara] Io intendo
		 * realizzare un pranzo per 50 persone del tipo persona1 persona2 persona3 ...
		 * pasta e ceci pasta al forno carbonara sogliola sogliola lombata creme brulee
		 * del al limone carciofi
		 */
		Persona[] persone = new Persona[50];

		for (int i = 0; i < persone.length; i++) {
			int numeroCasuale = 0;
			persone[i] = new Persona("Persona " + (i + 1), menu[numeroCasuale= (int) (Math.random() * 4)].getNome(), menu[numeroCasuale= (int) (Math.random() * 4)].getNome(), menu[numeroCasuale= (int) (Math.random() * 4)].getNome());
		}
		for (int i = 0; i < persone.length; i++) {
			System.out.println(persone[i]);
		}
		
	}
}
