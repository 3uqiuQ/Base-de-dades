#!/usr/bin/env python
# coding: utf-8

# **Exercici 1:**
# 
# **A partir dels documents adjunts (estructura i dades), crea una base de dades amb MySQL. Mostra les característiques principals de l'esquema creat i explica les diferents taules i variables que hi ha.**

# La base de datos está formada por cinco tablas:
# - tb_movie_person
# - tb_person
# - tb_movie
# - tb_role
# - tb_genre
# 
# La tabla principal es la tb_movie_person. La tabla contiene tres Primary Keys que coinciden con una Primary Key otra tabla. Así:
# - movie_id en tb_movie_person coincide con movie_id en tb_movie.
# - person_id en tb_movie_person coincide con person_id en tb_person.
# - role_id en tb_movie_person coincide con role_id en tb_role.
# - La relación con la quinta tabla aparece desde la tabla tb_movie, donde existe una Foreign Key (movie_genre_id) que coincide con la Primary Key de la tb_genre (genre_id). Esta última relación, al no ser entre Primary Key, aparece como una linea discontinua en el EER Diagram.
# - Aparece otra relación en la tb_person con respecto a sí misma entre la su Primary Key (person_id) y una Foreign Key de la misma tabla (person_parent_id).

# **Exercici 2:**
# 
# **Has d'obtenir el nom, el país i la data de naixement d'aquelles persones per les quals no consti una data de mort
# i ordenar les dades de la persona més vella a la persona més jove.**

# In[ ]:


USE movies;
SELECT person_name, person_country, person_dob, person_dod FROM tb_person 
WHERE person_dod is NULL ORDER BY person_dob DESC;


# ![Exercici2_M1_T01.png](attachment:Exercici2_M1_T01.png)

# **Exercici 3:**
# 
# **Has d'obtenir el nom del gènere i el nombre total de pel·lícules d'aquest gènere i ordenar-ho per ordre descendent de nombre total de pel·lícules.**

# In[ ]:


USE movies;
SELECT genre_name, genre_id FROM tb_genre ORDER BY genre_id DESC;


# ![Exercici3_M1_T01.png](attachment:Exercici3_M1_T01.png)

# __Exercici 4 (A):__
# 
# __Has d'obtenir, per a cada persona, el seu nom i el nombre màxim de rols diferents que ha tingut en una mateixa pel·lícula.__

# In[ ]:


USE movies;

SELECT tb_person.person_name, count(tb_movie_person.role_id) AS num_rol 
FROM tb_person INNER JOIN tb_movie_person 
ON tb_person.person_id = tb_movie_person.person_id group by person_name;


# ![Exercici4_A_M1_T01.png](attachment:Exercici4_A_M1_T01.png)

# __Exercici 4 (B):__
# 
# __Posteriorment, mostra únicament aquelles persones que hagin assumit més d'un rol en una mateixa pel·lícula.__

# In[ ]:


USE movies;

SELECT tb_person.person_name, count(tb_movie_person.role_id) AS num_rol 
FROM tb_person INNER JOIN tb_movie_person ON tb_person.person_id = tb_movie_person.person_id 
GROUP BY tb_person.person_name HAVING count(tb_movie_person.role_id) > 1;


# ![Exercici4_B_M1_T01.png](attachment:Exercici4_B_M1_T01.png)

# __Exercici 5:__
# 
# __Has de crear un nou gènere anomenat "Documental" el qual tingui com a identificador el nombre 69.__

# In[ ]:


INSERT INTO movies.tb_genre (genre_id, genre_name, created_date) VALUES (69, 'Documental', '2023-04-24');


# ![Exercici5_M1_T01.png](attachment:Exercici5_M1_T01.png)

# __Exercici 6:__
# 
# __Elimina la pel·lícula "La Gran Familia Española" de la base de dades.__

# In[ ]:


USE movies;
DELETE FROM tb_movie_person WHERE movie_id = 11;


# La pelicula está guardada en la tb_movies, donde existe una Foreign Key que se relaciona con la tb_genre y también con la tb_movie_person mediante las Primary Keys, por lo que el sistema no permite eliminarla. Después de cambiar 'On Delete'a CASCADE, para que automaticamente actualice los registros coincidentes, se ha de eliminar desde la tabla principal.

# ![Exercici6_M1_T01.png](attachment:Exercici6_M1_T01.png)

# **Exercici 7:**
# 
# **Canvia el gènere de la pel·lícula "Ocho apellidos catalanes" perquè consti com a comèdia i no com a romàntica.**

# In[ ]:


UPDATE tb_movie SET movie_genre_id = 3 WHERE movie_genre_id = 8;


# ![Exercici7_M1_T01.png](attachment:Exercici7_M1_T01.png)

# In[ ]:




