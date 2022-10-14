# Lista de dicionários contendo o id e o nome dos usuários
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

# Lista de amizades. Uma lista de tuplas contendo pares de ids.
friendships_par = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

#Criando um dict comprehention e adicionando uma lista de amizades vazia para cada usuário.
friendships = {user['id']: [] for user in users}

# Percorrendo o laço para popular a lista de amigos de cada usuário
for i, j in friendships_par:
    friendships[i].append(j) # adiciona j como amigo do usuário i
    friendships[j].append(i) # adiciona i como amigo do usuário j

# Exibindo o usuário e sua lista de amizades  
print(friendships)
# Função que retorna o tamanho da lista de amigos.
def number_of_friends(user):
    user_id = user['id']
    friends_id = friendships[user_id]
    return len(friends_id)

# Somatório das conexões
total_connections = sum(number_of_friends(user) for user in users)

# Obtendo o tamanho de usuários
num_users = len(users)
# Calculando o número médio de conexões
avg_users = total_connections/num_users

# Cria uma lista de tuplas com id do usuario e o número de amizades
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]

# Ordena a lista do maior para o menor. Do usuário que tem o maior número de amigos para o que tem
# o menor número de amigos
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)

# Exibindo a lista reversa
print(num_friends_by_id)

# Função que itera os amigos e os amigos dos amigos
# O problema é que ela retorna também o próprio usuário repetidas vezes
def foaf_ids_bad(user):
    # foat significa friend of a friend
    user_id = user['id']
    return [foaf_id for friend_id in friendships[user_id]
                    for foaf_id in friendships[friend_id]]

#what_friends = [foaf_ids_bad(user) for user in users]
print(foaf_ids_bad(users[0]))
# Utilizando a função Counter podermos resolver o problema da repetição de amigos,
# gerando a contagem de amigos em comum mas excluindo que o usuário já conhece.
from collections import Counter
from xml.etree.ElementInclude import default_loader
def friends_of_friends(user):
    user_id = user['id']
    return Counter(foaf_id for friend_id in friendships[user_id]
                           for foaf_id in friendships[friend_id]
                           if foaf_id != user_id and foaf_id not in friendships[user_id])

# Exibindo o amigo dos amigos do usuário de id 0, ou seja, o usuário de id 0 tem os amigos 2 e 1,
# os amigos de ids 2 e 1 também são amigos do usuário de id 3, então a saida será o usuário de id 3
# que tem um tatal de 2 amigos, esses são em comum com o ususário de id 0.
print(friends_of_friends(users[0]))
# output Count({3: 2})

# iterando sobre a lista de usuários para imprimir todos os amigos em comum
all_friends_of_friends = [friends_of_friends(user) for user in users]
#print(all_friends_of_friends)

all_friends_of_friends.sort(key=lambda most_friends: most_friends[1], reverse=True)
#print(all_friends_of_friends)

# Talvez você queira encontrar usurários com interesses similiares
# Lista de interesses
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]
# Observando a lista de interesses podemos ver que o usário de id 0 não possui amigos em comum
# com o usuário de id 9, no entanto os 2 se interessm por java e big data.
def data_scientest_who_like(target_interest):
    # Encontre os ids dos usuários com o mesmo interesse
    return [
        user_id for user_id, user_interest in interests
                if user_interest == target_interest
    ]

#print(data_scientest_who_like('Java'))
