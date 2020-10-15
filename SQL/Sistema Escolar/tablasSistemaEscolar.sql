use SistemaEscolar

create table Prof
	(IdProf	   int	primary key,
	NomProf	   char(30),
	Categoría  char(2)	check (Categoría in ('tc','mt','tp')));

create table Alum
	(CU	   		int	primary key,
	NomAl	   char(30),
	Carr	   char(3)	check (Carr in ('act','com','ind','neg')),
	Prom	   real		check (Prom is null
				  	or Prom between 6 and 10));

create table Mater
	(ClaveM    int	primary key,
	NomMat	   char(30)	unique,
	Creds	   smallint	check (Creds between 2 and 12));

create table Grupo
	(ClaveG	   char(6)	primary key,
	Salón	   char(8),
	IdProf	   int	references Prof,
	ClaveM 	   int	references Mater not null);
	
create table Inscrito
	(CU			int	references Alum,
	ClaveG	   char(6)	references Grupo,  
				primary key (CU,ClaveG));

create table Historial
	(Folio	   int		primary key,	
	Calif	   int	check (Calif between 5 and 10),
	Fecha	   datetime	check (Fecha > '1990-01-01'),
	CU	   		int	references Alum not null,
	ClaveM	   int	references Mater not null);
