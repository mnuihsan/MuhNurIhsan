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
    chromosome = {
        'a': random.randint(a_min, a_max),
        'b': random.randint(b_min, b_max),
        'c': random.randint(c_min, c_max),
        'd': random.randint(d_min, d_max)
    }
    return chromosome

def evaluate(chromosome):
    equation_result = chromosome['a'] + 4 * chromosome['b'] + 2 * chromosome['c'] + 3 * chromosome['d']
    fitness = abs(equation_result - 30)
    return fitness

def calculate_fitness(population):
    total_fitness = sum(1 / (1 + evaluate(chromosome)) for chromosome in population)
    return [1 / (1 + evaluate(chromosome)) / total_fitness for chromosome in population]

def select_parent(population, fitness_values):
    cumulative_probabilities = [sum(fitness_values[:i+1]) for i in range(len(fitness_values))]
    random_value = random.random()
    for i, probability in enumerate(cumulative_probabilities):
        if random_value <= probability:
            return population[i]

def crossover(parent1, parent2):
    cut_point = random.randint(1, 3)  # Memilih posisi pemotongan acak
    child1 = {key: parent1[key] if index < cut_point else parent2[key] for index, key in enumerate(parent1)}
    child2 = {key: parent2[key] if index < cut_point else parent1[key] for index, key in enumerate(parent2)}
    return child1, child2

def mutate(chromosome):
    mutated_gene = random.choice(['a', 'b', 'c', 'd'])
    if mutated_gene == 'a':
        chromosome['a'] = random.randint(a_min, a_max)
    elif mutated_gene == 'b':
        chromosome['b'] = random.randint(b_min, b_max)
    elif mutated_gene == 'c':
        chromosome['c'] = random.randint(c_min, c_max)
    elif mutated_gene == 'd':
        chromosome['d'] = random.randint(d_min, d_max)
    return chromosome

def genetic_algorithm():
    # Inisialisasi populasi awal
    population = [generate_chromosome() for _ in range(jumlah_populasi)]

    for iteration in range(max_iterasi):
        fitness_values = calculate_fitness(population)

        # Seleksi orang tua
        parents = [select_parent(population, fitness_values) for _ in range(jumlah_populasi)]

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
        population += offspring

        # Memilih populasi baru berdasarkan fitness
        population = sorted(population, key=lambda x: evaluate(x))
        population = population[:jumlah_populasi]

        best_chromosome = population[0]
        best_fitness = evaluate(best_chromosome)

        print(f"Iterasi {iteration+1}: Kromosom Terbaik: {best_chromosome}, Fitness: {best_fitness}")

        if best_fitness == 0:
            break

    return best_chromosome

# Menjalankan algoritma genetika
nilai_mutasi = 0.1
solusi_terbaik = genetic_algorithm()
print("Solusi Terbaik:", solusi_terbaik)