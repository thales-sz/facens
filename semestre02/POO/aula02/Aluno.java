public class Aluno {
  String nome;
  Double media;

  public void verificarAprovacao() {
    if (this.media >= 7) {
      System.out.println("O aluno " + this.nome + " foi aprovado!");
    } else {
      System.out.println("O aluno " + this.nome + " foi reprovado!");
    }
  }

  public void setNome(String nome) {
    this.nome = nome;
  }

  public void setMedia(Double media) {
    this.media = media;
  }

  public String getNome() {
    return this.nome;
  }

  public Double getmedia() {
    return this.media;
  }

  public String toString() {
    return "Aluno {\n Nome: " + this.nome + "\n Média: " + this.media + "\n}";
  }
}