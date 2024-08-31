import java.util.Scanner;

public class Aula02 {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    String nome;
    Double media;
    Aluno aluno = new Aluno();

    System.out.println(aluno.toString());

    System.out.println("Digite o nome do aluno: ");
    nome = sc.nextLine();
    aluno.setNome(nome);
  
    System.out.println("Digite a média do aluno: ");
    media = sc.nextDouble();
    aluno.setMedia(media);

    System.out.println(aluno.toString());
    
    aluno.verificarAprovacao();

    sc.close();
  }
}