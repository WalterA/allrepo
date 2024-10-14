
public class Persona {
	private String nome;
	/*
	 * Costruire una classe Persona e verificare il funzionamento dei setter e getter
	 * - aggiungere un attributo temperatura alla persona e modificare setter e getter per mostrare temperatura celsius o fahrenheit 
	 */
	private float temperatura;
	
	public float getTemperaturaCelsuis() {
		return temperatura;
	}
	public float getTemperaFarhenheit() {
		return (float)(temperatura * 9.0 /5.0+32.0);
	}
	public void setTemperaturaCelsuis(float temperatura) {
		this.temperatura = temperatura;
	}
	public void setTemperaturaFarhenheit(float temperatura) {
		this.temperatura = (float)(temperatura-32.0 /9.0*5.0);
	}
	

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

}
