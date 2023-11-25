CREATE TABLE alimentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50)
);

CREATE TABLE dietas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_cliente VARCHAR(100),
    data_inicio DATE,
    data_fim DATE
);

CREATE TABLE dieta_alimento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dieta_id INT,
    alimento_id INT,
    quantidade VARCHAR(20),
    FOREIGN KEY (dieta_id) REFERENCES dietas(id),
    FOREIGN KEY (alimento_id) REFERENCES alimentos(id)
);

-- Inserções de exemplo
INSERT INTO alimentos (nome) VALUES ('Maçã'), ('Frango'), ('Brócolis'), ('Quinoa'), ('Abacate'), ('Salmão');
INSERT INTO dietas (nome_cliente, data_inicio, data_fim) VALUES ('Cliente 1', '2023-11-01', '2023-12-01');
INSERT INTO dieta_alimento (dieta_id, alimento_id, quantidade) VALUES (1, 1, '2 unidades'), (1, 2, '150g'), (1, 3, '100g');
