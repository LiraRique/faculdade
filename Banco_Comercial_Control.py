import sqlite3

conexao= sqlite3.connect("Bd_ComercialControl.db")

cursor= conexao.cursor()

cursor.execute("""
    Create Table Usuario(
        cod_usuario varchar(30) ,
        nome_usuario varchar(40) ,
        dt_cadastro date ,
        dt_bloqueio date ,
        dt_ultimo_acesso date ,
        motivo_bloqueio varchar(100),
        qtde_senha_errada number(2),
        dt_ultima_troca date,
        ind_bloqueado varchar(1),
        senha_aplicacao varchar(500),

        constraint pkcod_usuario primary key (cod_usuario)
    )
""")

cursor.execute("""
    Create Table Pessoa(
        id_pessoa number(12),
        id_tipo_pessoa varchar(1),
        nome varchar(130),
        incricao  number(14),
        data_cadastro date,
        ind_cliente varchar (1),
        ind_funcionario varchar(1),
        ind_fornecedor varchar(1),

        constraint pkid_pessoa primary key (id_pessoa)
        constraint fkid_tipo foreign key (id_tipo_pessoa) references Pessoa(id_tipo_pessoa)

    )
""")

#constraint fkVendasAnuais_idVeiculo foreign key (idVeiculo) references Veiculo(idVeiculo)






conexao.commit()
cursor.close()
conexao.close()

