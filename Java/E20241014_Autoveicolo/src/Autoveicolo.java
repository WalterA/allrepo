
public class Autoveicolo {
	private double cilindrata, consumo /* (km/litro) */, serbatorio, prezzo;
	private String colore;

	public double getCilindrata() {
		return cilindrata;
	}

	public Autoveicolo(double cilindrata, double consumo, double serbatorio, double prezzo, String colore) {
		super();
		this.cilindrata = cilindrata;
		this.consumo = consumo;
		this.serbatorio = serbatorio;
		this.prezzo = prezzo;
		this.colore = colore;
	}

	public void setCilindrata(double cilindrata) {
		this.cilindrata = cilindrata;
	}

	public double getConsumo() {
		return consumo;
	}

	public void setConsumo(double consumo) {
		this.consumo = consumo;
	}

	public double getSerbatorio() {
		return serbatorio;
	}

	public void setSerbatorio(double serbatorio) {
		this.serbatorio = serbatorio;
	}

	public double getPrezzo() {
		return prezzo;
	}

	public void setPrezzo(double prezzo) {
		this.prezzo = prezzo;
	}

	public String getColore() {
		return colore;
	}

	public void setColore(String colore) {
		this.colore = colore;
	}

	public double calcolaDistanza(double velocitaMedia, double ore) {
		return velocitaMedia * ore;
	}

	@Override
	public String toString() {
		return "Autoveicolo [cilindrata=" + cilindrata + ", consumo=" + consumo + ", serbatorio=" + serbatorio
				+ ", prezzo=" + prezzo + ", colore=" + colore + "]";
	}
}
