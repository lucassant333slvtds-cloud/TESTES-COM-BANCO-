from faker import Faker
from db import conectar
import random
from datetime import datetime

fake = Faker("pt_BR")  # GERANDO DADOS DO BRASIL

def gerar_cliente():
    nome = fake.name()
    email = fake.email()
    idade = random.randint(18, 70)
    cpf = fake.cpf()
    telefone = fake.phone_number()
    endereco = fake.address().replace("\n", ", ")  # tirar quebra de linha
    cidade = fake.city()
    estado = fake.estado_sigla()
    genero = random.choice(["Masculino", "Feminino", "Outro"])
    data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return (
        nome, email, idade, cpf, telefone,
        endereco, cidade, estado, genero, data_cadastro
    )

def inserir_cliente():
    conn = conectar()
    cursor = conn.cursor()

    sql = """
        INSERT INTO clientes 
        (nome, email, idade, cpf, telefone, endereco, cidade, estado, genero, data_cadastro)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cliente = gerar_cliente()
    cursor.execute(sql, cliente)
    conn.commit()

    print("✔ Cliente cadastrado com sucesso!")

for _ in range(100):
    inserir_cliente()

