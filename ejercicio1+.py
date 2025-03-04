

a = "Jorge Vela"
b = 25

print("Mi nombre es es", a, "y tengo", b, "años")

c = "Hola"
print(c,c,c,c,c)

f = "que la fuerza te acompañe"
f_updated = f.replace(" ","_")
print(f_updated)

greeting = "Hola"
name = "Lucas"
print(greeting,name)

message = 'Buenos días'
print(message)
message = "Buenas noches"
print(message)

word = "Adios, doctor"
name = "Who"
sentence = word + " " + name
print(sentence)
word = "Adios, doctor"
print(sentence)


hero = 'SpiderMan'

for letras in hero:
    print("---",letras)

name = 'Pikachu'
line = ''
for rampa in name:
    line += rampa
    print(line)
   
    
for i in range(5):
    print(i)
    
for i in range(1,6):  
    print(i)
    
    
superhero_active = True

if (superhero_active):
    print("¡Spider-Man está en acción!")
else:
    print("")

sentence = 'messi es el mejor'
excited = False

if(excited):
    print(sentence.upper())
else:
    print(sentence)

password = 'openSesame'
access_level = 6
if password == "openSesame" and access_level> 5:
    print("Acceso concedido a la base secreta.")
else:
    print("Acceso denegado.")
 
characters = ['Luke Skywalker', 'Darth Vader', 'Leia Organa', 'Han Solo']
for character in characters:
    print(character)
    
durations = [121, 154, 178, 132]
total_duration = 0
for duration in durations:
    total_duration += duration
print(total_duration)

movies = ['The Godfather', 'Pulp Fiction', 'Inception', 'The Dark Knight']

titulos = " ".join(movies)
print(titulos)
titulos = " / ".join(movies)
print(titulos)





