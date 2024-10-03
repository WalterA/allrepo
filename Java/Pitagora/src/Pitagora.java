
public class Pitagora {

	public static void main(String[] args) {
		// TODO Auto-generated method stub


		//Calcolo dell'ipotenusa di un triangolo rettangolo

		 /*

		 * Sia dato un triangolo rettangolo i cui cateti misurano rispettivamente 10.345 e 20.415 cm

		 * Calcolare

		 * 1) la lunghezza dell'ipotenusa

		 * 2) il perimetro del triangolo rettangolo

		 * 3) L'area del triangolo rettangolo

		 * NB:

		 * a) Teorema di pitagora

		 * dati c1 w c2 cateti di un triangolo rettangolo, l'ipotenusa è la radice quadrata della somma dei quadrati dei cateti

		 * b) In java la rqdica quadrata si calcola con Math.sqrt(numero)

		 */
		
		double l1,l2, lu, a, perimetro, lur, d;
		l1 = 10.345 ;
		l2= 20.415;
		d=2.0;
		lu = Math.sqrt(l1*l1+l2* l2);
		perimetro = l1+l2+lu;
		a= l1 * l2 /d;
		System.out.println("Lunghezza:"+lu);
		System.out.println("Perimetro:"+perimetro);
		System.out.println("Aria:"+a);
	}

}
