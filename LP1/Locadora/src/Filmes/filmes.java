package Filmes;

public class filmes {
	//atributos
	
			
			private String titulo;
			private String genero;
			private int duracao;
			private String diretor;
			private int codigo;
			private String midia;
			
			
			//métodos de acesso
			
			public String getTitulo() {
				return titulo;
			}

			public String getGenero() {
				return genero;
			}

			public int getDuracao() {
				return duracao;
			}

			public String getDiretor() {
				return diretor;
			}

			public int getCodigo() {
				return codigo;
			}						
			public String getMidia() {
				return midia;
			}

			
			
			//método construtor
			public filmes(String titulo, String genero, String diretor, String midia){
				this.titulo = titulo;
				this.genero = genero;
				this.diretor = diretor;
				this.midia = midia;
				
			}
			
			//métodos de classes
			public void assistir(){
				System.out.println("Sentar no sofá");
			}
			
			public void comer (){
			System.out.println("Fazer pipoca");
			}
			
			
				
			

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	   
		filmes o2=new filmes("Matrix","Ação","lana wachowski","DVD");
		o2.assistir();
		filmes o3=new filmes("Minions","Comedia","João Diretor","DVD");
		o3.comer();
		
		
				
			
	}

}
