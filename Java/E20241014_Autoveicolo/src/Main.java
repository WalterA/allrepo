
public class Main {

	public static void main(String[] args) {
		Autoveicolo auto1 = new Autoveicolo(1500, 18.0, 50, 25000, "Rosso");
        Autoveicolo auto2 = new Autoveicolo(1200, 20.0, 45, 22000, "Blu");
        Autoveicolo auto3 = new Autoveicolo(2000, 15.0, 55, 30000, "Nero");

        
        double velocitaMedia1 = 80.0; 
        double velocitaMedia2 = 90.0; 
        double velocitaMedia3 = 85.0; 

        
        double distanzaAuto1_3h = auto1.calcolaDistanza(velocitaMedia1, 3);
        double distanzaAuto1_11h = auto1.calcolaDistanza(velocitaMedia1, 11);

        double distanzaAuto2_3h = auto2.calcolaDistanza(velocitaMedia2, 3);
        double distanzaAuto2_11h = auto2.calcolaDistanza(velocitaMedia2, 11);

        double distanzaAuto3_3h = auto3.calcolaDistanza(velocitaMedia3, 3);
        double distanzaAuto3_11h = auto3.calcolaDistanza(velocitaMedia3, 11);

        //Print
        System.out.println("Dettagli Auto 1:");
        System.out.println(auto1);
        System.out.println("Distanza percorsa in 3 ore: " + distanzaAuto1_3h + " km");
        System.out.println("Distanza percorsa in 11 ore: " + distanzaAuto1_11h + " km");
        System.out.println();

        System.out.println("Dettagli Auto 2:");
        System.out.println(auto2);
        System.out.println("Distanza percorsa in 3 ore: " + distanzaAuto2_3h + " km");
        System.out.println("Distanza percorsa in 11 ore: " + distanzaAuto2_11h + " km");
        System.out.println();

        System.out.println("Dettagli Auto 3:");
        System.out.println(auto3);
        System.out.println("Distanza percorsa in 3 ore: " + distanzaAuto3_3h + " km");
        System.out.println("Distanza percorsa in 11 ore: " + distanzaAuto3_11h + " km");

	}

}
