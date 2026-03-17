from django.db import models
class livro(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    genero = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nome)

class aluno(models.Model):
    nome_aluno = models.CharField(max_length=100)
    matricula = models.IntegerField(unique=True)
    curso = models.CharField(max_length=100)
    idade = models.IntegerField()
    def __str__(self):
       return str(self.nome_aluno)


class avisos(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_publicacao = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.titulo)
