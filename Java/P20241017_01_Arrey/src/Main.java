public class Main {

    public static void main(String[] args) { 
        // Dichiarare un array di 1000 double
        // Inserire nell'array un valore casuale compreso tra 0 e 100
        // Confrontare quanti elementi dell'array sono minori di 50
        
        double[] num = new double[1000];
        int conta = 0;
        for (int i = 0; i < num.length; i++) {
            num[i] = Math.random() * 100; // Genera un numero casuale tra 0 e 100
            if (num[i] < 50.00) { // Controlla se è minore di 50
                conta++;
            }
        }
        System.out.println("Elementi minori di 50: " + conta);
        
        // Calcolare la somma e la media dei numeri presenti nell'array
        double somma = 0.0;
        for (int i = 0; i < num.length; i++) {
            somma += num[i];
        }
        double media = somma / num.length;
        
        // Calcolare quante volte il numero successivo è maggiore del precedente
        int maggiore = 0;
        for (int i = 0; i < num.length - 1; i++) {
            if (num[i + 1] > num[i]) {
                maggiore++;
            }
        }

        // Calcolare la lunghezza della più lunga sequenza di numeri crescenti
        int maxSeqLength = 0; // Lunghezza massima della sequenza crescente
        int currentSeqLength = 1; // Lunghezza della sequenza corrente
        for (int i = 0; i < num.length - 1; i++) {
            if (num[i + 1] > num[i]) {
                currentSeqLength++;
            } else {
                if (currentSeqLength > maxSeqLength) {
                    maxSeqLength = currentSeqLength; // Aggiorna la sequenza più lunga
                }
                currentSeqLength = 1; // Resetta la lunghezza della sequenza corrente
            }
        }
        // Verifica se l'ultima sequenza era la più lunga
        if (currentSeqLength > maxSeqLength) {
            maxSeqLength = currentSeqLength;
        }

        // Stampa i risultati
        System.out.println("Somma: " + somma);
        System.out.println("Media: " + media);
        System.out.println("Numero di volte che il successivo è maggiore del precedente: " + maggiore);
        System.out.println("Lunghezza della più lunga sequenza crescente: " + maxSeqLength);
    }
}
