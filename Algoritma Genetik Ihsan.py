import random

# Batasan nilai variabel
a_min = 0
a_max = 30
b_min = 0
b_max = 10
c_min = 0
c_max = 10
d_min = 0
d_max = 10

# Jumlah populasi dan iterasi
jumlah_populasi = 6
max_iterasi = 100

def generate_chromosome():
    kromosom = {
        'a': random.randint(a_min, a_max),
        'b': random.randint(b_min, b_max),
        'c': random.randint(c_min, c_max),
        'd': random.randint(d_min, d_max)
    }
    return kromosom

def evaluate(kromosom):
    hasil_perhitungan = kromosom['a'] + 4 * kromosom['b'] + 2 * kromosom['c'] + 3 * kromosom['d']
    fitness = abs(hasil_perhitungan - 30)
    return fitness

def calculate_fitness(populasi):
    total_fitness = sum(1 / (1 + evaluate(kromosom)) for kromosom in populasi)
    return [1 / (1 + evaluate(kromosom)) / total_fitness for kromosom in populasi]

def select_parent(populasi, fitness_values):
    probabilitas_kumulatif = [sum(fitness_values[:i+1]) for i in range(len(fitness_values))]
    nilai_acak = random.random()
    for i, probability in enumerate(probabilitas_kumulatif):
        if nilai_acak <= probability:
            return populasi[i]

def crossover(parent1, parent2):
    cut_point = random.randint(1, 3)  # Memilih posisi pemotongan acak
    child1 = {key: parent1[key] if index < cut_point else parent2[key] for index, key in enumerate(parent1)}
    child2 = {key: parent2[key] if index < cut_point else parent1[key] for index, key in enumerate(parent2)}
    return child1, child2

def mutate(kromosom):
    mutated_gene = random.choice(['a', 'b', 'c', 'd'])
    if mutated_gene == 'a':
        kromosom['a'] = random.randint(a_min, a_max)
    elif mutated_gene == 'b':
        kromosom['b'] = random.randint(b_min, b_max)
    elif mutated_gene == 'c':
        kromosom['c'] = random.randint(c_min, c_max)
    elif mutated_gene == 'd':
        kromosom['d'] = random.randint(d_min, d_max)
    return kromosom

def genetic_algorithm():
    # Inisialisasi populasi awal
    populasi = [generate_chromosome() for _ in range(jumlah_populasi)]

    for iterasi in range(max_iterasi):
        fitness_values = calculate_fitness(populasi)

        # Seleksi orang tua
        parents = [select_parent(populasi, fitness_values) for _ in range(jumlah_populasi)]

        # Crossover
        offspring = []
        for i in range(0, jumlah_populasi, 2):
            parent1 = parents[i]
            parent2 = parents[i+1]
            child1, child2 = crossover(parent1, parent2)
            offspring.append(child1)
            offspring.append(child2)

        # Mutasi
        for i in range(jumlah_populasi):
            if random.random() < nilai_mutasi:
                offspring[i] = mutate(offspring[i])

        # Menggabungkan populasi sebelumnya dengan offspring
        populasi += offspring

        # Memilih populasi baru berdasarkan fitness
        populasi = sorted(populasi, key=lambda x: evaluate(x))
        populasi = populasi[:jumlah_populasi]

        kromosom_terbaik = populasi[0]
        best_fitness = evaluate(kromosom_terbaik)

        print(f"Iterasi {iterasi+1}: Kromosom Terbaik: {kromosom_terbaik}, Fitness: {best_fitness}")

        if best_fitness == 0:
            break

    return kromosom_terbaik

# Menjalankan algoritma genetika
nilai_mutasi = 0.1
solusi_terbaik = genetic_algorithm()
print("Solusi Terbaik:", solusi_terbaik)
