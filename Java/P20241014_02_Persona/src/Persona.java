
public class Persona {
	private String nome, cognome, codiceFiscale, indirizzo, comune, sesso, data, telefono;

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getCognome() {
		return cognome;
	}

	public void setCognome(String cognome) {
		this.cognome = cognome;
	}

	public String getCodiceFiscale() {
		return codiceFiscale;
	}

	public void setCodiceFiscale(String codiceFiscale) {
		this.codiceFiscale = codiceFiscale;
	}

	public String getIndirizzo() {
		return indirizzo;
	}

	public void setIndirizzo(String indirizzo) {
		this.indirizzo = indirizzo;
	}

	public String getComune() {
		return comune;
	}

	public void setComune(String comune) {
		this.comune = comune;
	}

	public String getSesso() {
		return sesso;
	}

	public void setSesso(String sesso) {
		this.sesso = sesso;
	}

	public String getData() {
		return data;
	}

	public void setData(String data) {
		this.data = data;
	}

	public String getTelefono() {
		return telefono;
	}

	public void setTelefono(String telefono) {
		this.telefono = telefono;
	}

	public Persona(String nome, String cognome, String codiceFiscale, String indirizzo, String comune, String sesso,
			String data, String telefono) {
		super();
		this.nome = nome;
		this.cognome = cognome;
		this.codiceFiscale = codiceFiscale;
		this.indirizzo = indirizzo;
		this.comune = comune;
		this.sesso = sesso;
		this.data = data;
		this.telefono = telefono;
	}

	@Override
	public String toString() {
		return "Persona [nome=" + nome + ", cognome=" + cognome + ", codiceFiscale=" + codiceFiscale + ", indirizzo="
				+ indirizzo + ", comune=" + comune + ", sesso=" + sesso + ", data=" + data + ", telefono=" + telefono
				+ "]";
	}

}
