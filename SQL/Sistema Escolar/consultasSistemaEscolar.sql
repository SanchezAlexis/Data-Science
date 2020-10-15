--TP 2
use SistemaEscolar

--Ejercicio A
select IdProf,NomProf from Prof

--Ejercicio B
select * from Prof

--c
select *from Alum

--promedio de negocios
select NomAl, Prom from Alum where Prom>=8 and Carr='neg'

--d
select distinct Carr from Alum

--e
select distinct Carr from Alum order by Carr asc

select NomAl,Carr,Prom from Alum order by Carr asc, Prom desc

--g
select NomProf, NomMat from Prof, Grupo, Mater
	where Prof.IdProf=Grupo.IdProf 
		and Grupo.ClaveM=Mater.ClaveM
	order by NomProf asc

select NomAl, NomMat, Calif from Alum, Historial,Mater
	where Alum.CU=Historial.CU and Historial.ClaveM=Mater.ClaveM
	and Historial.Fecha between '2008-01-01' and '2007-12-31'

select NomMat, Grupo.ClaveG,NomAl from Alum,Inscrito,Grupo,Mater
	where Alum.CU=Inscrito.CU 
	and Inscrito.ClaveG=Grupo.ClaveG
	and Grupo.ClaveM=Mater.ClaveM

--j
(select CU from Inscrito)--claves unicas del alumnes inscritos

--consulta principal
select NomAl,Carr from Alum

--todo junto
select NomAl,Carr from Alum where CU in (select CU from Inscrito)

select NomAl,Prom from Alum where CU not in (select CU from Inscrito)

--l
select NomProf, Categoría from Prof where IdProf not in (select IdProf from Grupo)

--2a
select NomProf,Categoría from Prof 
	where (Prof.Categoría ='tc' or Prof.Categoría='mt')
	and (NomProf Like 'L%' or NomProf like 'R%')

--2b
select NomMat from Mater where Creds>=8 order by Creds desc, NomMat asc

--2c
select NomProf, NomMat, NomAl from Prof, Mater, Alum, Grupo, Inscrito 
	where Prof.IdProf=Grupo.IdProf
	and Grupo.ClaveM=Mater.ClaveM
	and Grupo.ClaveG=Inscrito.ClaveG
	and Inscrito.CU=Alum.CU
	order by NomProf asc, NomMat desc

--2d
select NomMat, NomAl, Fecha, Calif from Mater, Alum, Historial
	where NomMat like 'E%'
	and Mater.ClaveM=Historial.ClaveM
	and Historial.CU=Alum.CU
	and Historial.Fecha between '2008-01-01' and '2008-09-09'
	order by Fecha desc

--2e
select NomMat from Mater, Grupo
	where Creds>=9 
	and Mater.ClaveM=Grupo.ClaveM
	and Grupo.ClaveG=null

--2f
select count(*) from Alum

--2g
select count(NomProf) from Prof, Grupo
	where Prof.IdProf=Grupo.IdProf

select NomMat, Calif from Mater,Historial
	where Mater.ClaveM=Historial.ClaveM

--Revision del control--------------------------------------------------------------------------
--1
select NomProf,Categoría  from Prof, Grupo, Inscrito, Alum
	where Prof.IdProf=Grupo.IdProf
	and Grupo.ClaveG=Inscrito.ClaveG
	and Inscrito.CU=Alum.CU
	and Alum.Carr='neg'

--2
select Grupo.ClaveG, Prof.NomProf, NomMat from Grupo, Prof,Mater,Inscrito,Alum
	where Mater.ClaveM=Grupo.ClaveM 
	and Grupo.IdProf=Prof.IdProf
	and Grupo.ClaveG=Inscrito.ClaveG
	and Inscrito.CU=Alum.CU
	and Alum.Carr='neg'
--3
select NomAl, Prom from Alum,Historial,Mater
	where Alum.CU=Historial.CU
	and Historial.ClaveM=Mater.ClaveM
	and Mater.NomMat='Algoritmos'

--4 (usando subconsulta)
select NomMat, Calif, Alum.NomAl from Alum, Historial,Mater
	where Alum.CU=Historial.CU
	and Historial.ClaveM=Mater.ClaveM
	and Alum.CU in 
	(select Alum.CU from Alum,Prof, Grupo, Inscrito
		where Prof.IdProf=Grupo.IdProf
		and Grupo.ClaveG=Inscrito.ClaveG
		and Inscrito.CU=Alum.CU
		and NomProf='Roberto')
	order by NomMat asc


--Control 2
--1
select NomMat,Calif,NomAl from Mater,Historial,Alum
	where Mater.ClaveM=Historial.ClaveM
	and Historial.CU=Alum.CU
	and Alum.NomAl='Patricia'

--2
select NomAl, NomMat, Grupo.ClaveG from Alum,Inscrito, Grupo,Prof,Mater
	where Alum.CU=Inscrito.CU
	and Inscrito.ClaveG=Grupo.ClaveG
	and Grupo.IdProf=Prof.IdProf
	and Grupo.ClaveM=Mater.ClaveM
	and Prof.NomProf='Luis'
	
select NomAl,Prom,NomMat from Alum,Inscrito,Grupo,Mater
	where Alum.CU=Inscrito.CU
	and Inscrito.ClaveG=Grupo.ClaveG
	and Grupo.ClaveM=Mater.ClaveM
	and Mater.NomMat='Matemáticas I'

--Control 3
--3
select NomAl, Carr from Alum, Historial
	where Alum.CU=Historial.CU
	and Historial.Fecha between '2007-01-01' and '2007-12-31'
	and Historial.Calif>8

--Control 4
select Grupo.ClaveG, NomProf from Alum,Inscrito, Grupo,Prof
	where Alum.NomAl='Ana'
	and Prof.IdProf=Grupo.IdProf
	and Grupo.ClaveG=Inscrito.ClaveG
	and Inscrito.CU=Alum.CU

--termina control---------------------------------------------------------------------------

--FUNCIONES DE AGREGACION
--TP2 m
select avg(Prom) as 'Promedio General', count (CU) as 'Num Alumnos' from Alum 
	where carr='ind'

--n
select count(ClaveM) as 'Numero de Materias' from Mater

--o
select avg(Prom) as 'Promedio de todos los alumnos' from Alum

--GROUP BY
--¿Cual es el promedio de cada carrera? 
select avg(prom)as 'promedio de cada carrera',carr from Alum group by carr

--p ¿Cuantas clases toma cada alumno?
select count(ClaveG)as 'Clave Grupo',NomAl from Alum, Inscrito 
	where Alum.CU=Inscrito.CU
	group by NomAl

--q
select NomMat,avg(Calif) as 'Promedio de Calis aprobadas por materia' from Historial,Mater
	where Historial.Fecha between '2007-01-01' and '2007-12-31'
	and Historial.ClaveM=Mater.ClaveM
	and Historial.Calif>=6
	group by NomMat

--FUNCION SUM (pregunta r)
select NomAl, sum(Creds) as 'Num Creditos' from Alum,Grupo,Mater,Inscrito
	where Alum.CU=Inscrito.CU
	and Inscrito.ClaveG=Grupo.ClaveG
	group by NomAl

--FUNCION HAVING para condicionar que solo aparezan las sumas mayores o iguales a 15
--Having: solo funciona con group by y sirve para evaluar condiciones de los resultados
--de las funciones de agregacion 
select NomAl, sum(Creds) as 'Num Materias' from Alum,Grupo,Mater,Inscrito
	where Alum.CU=Inscrito.CU
	and Inscrito.ClaveG=Grupo.ClaveG
	group by NomAl having sum(Creds)>=15

--Numero de materias con mas de alumno de la carrera de computacion
select NomMat, count(Carr) as 'Num de mat con las de un alumno de com'  from Alum, Inscrito, Grupo,Mater
	where Alum.CU=Inscrito.CU
	and Inscrito.ClaveG=Grupo.ClaveG
	and Grupo.ClaveM=Mater.ClaveM
	and Carr='com'
	group by NomMat having count(Carr)>1

--Misma de arriba pero con el nombre del alumno
select NomAl,NomMat, count(Carr) as 'Num de mat con las de un alumno de com'  from Alum, Inscrito, Grupo,Mater
	where Alum.CU=Inscrito.CU
	and Inscrito.ClaveG=Grupo.ClaveG
	and Grupo.ClaveM=Mater.ClaveM
	and Carr='com'
	group by NomMat,NomAl having count(Carr)>1

select Carr,avg(Prom) as 'Promedio Carrera' from Alum
	group by Carr having avg(Prom)<=8.5

--OR siempre entre parentesis
--las cu de los alumnos que estudian computacion y toman la materia de matematicas I
--Uso de UNION, INTERSECT,EXCEPT. Las consultas deben tener las mismas columnas 

--Empieza UNION-------------------------------
select CU from Alum where carr='com'
union
select Alum.CU from Alum,Inscrito,Grupo,Mater
	where Alum.CU=Inscrito.CU
	and Inscrito.ClaveG=Grupo.ClaveG
	and Grupo.ClaveM=Mater.ClaveM
	and Mater.NomMat='Matemáticas I'
--Termina UNION--------------------------------

--los dos juntos 
select distinct Alum.CU from Alum, Inscrito,Grupo,Mater
	where Alum.CU=Inscrito.CU
	and Inscrito.ClaveG=Grupo.ClaveG
	and Grupo.ClaveM=Mater.ClaveM
	and (Alum.Carr='com' or Mater.NomMat='Matemáticas I')

--x: Alumnos que toman Eco y Mate al mismo tiempo
--Empieza Intersect
select Alum.CU from Alum,Inscrito,Grupo,Mater
	where Alum.CU=Inscrito.CU
	and Inscrito.ClaveG=Grupo.ClaveG
	and Grupo.ClaveM=Mater.ClaveM
	and Mater.NomMat='Economía I'
intersect
select Alum.CU from Alum,Inscrito,Grupo,Mater
	where Alum.CU=Inscrito.CU
	and Inscrito.ClaveG=Grupo.ClaveG
	and Grupo.ClaveM=Mater.ClaveM
	and Mater.NomMat='Matemáticas I'
--Termina Intersect

--y: Listar los alumnos que mas (desc) o menos materias (asc) tienen
--Se usa top(x) para mostrar los de hasta arriba
select NomAl,count(NomMat) 'Maximo numero de materias' from Alum, Grupo,Inscrito,Mater
	where Alum.CU=Inscrito.CU
	and Inscrito.ClaveG=Grupo.ClaveG
	and Grupo.ClaveM=Mater.ClaveM
	group by NomAl having count(NomMat)in
	(select top (1)count(NomMat) 'Maximo numero de materias' from Alum, Grupo,Inscrito,Mater
		where Alum.CU=Inscrito.CU
		and Inscrito.ClaveG=Grupo.ClaveG
		and Grupo.ClaveM=Mater.ClaveM
		group by NomAl
		order by count(NomMat)desc)
--la subconsulta solo regresa una columna

--Funcion LIKE: se usa para la comparacion de Strings
-- ej: NomAl like 'A%'
--% muchos caracteres
-- _ para un caracter


