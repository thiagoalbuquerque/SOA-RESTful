
create table Publicacao (Id Bigserial PRIMARY key , Titulo varchar(50));
create table Autor (Cpf varchar(13) primary key, Nome varchar(50));
create table Publicacao_Autor(Id int REFERENCES Publicacao (Id), Cpf varchar(13) REFERENCES Autor (Cpf), PRIMARY KEY (Id, Cpf) );
create table Edicao (IdEdicao Bigserial PRIMARY key , data TIMESTAMP  , Qualis varchar(2));
create table Local(Cidade varchar (30) , Paiasds varchar (30));
create table Forum (Nome varchar (30) , Tipo varchar(20), Sigla varchar(10), IdEdicao int REFERENCES Edicao(IdEdicao));
