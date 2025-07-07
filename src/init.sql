CREATE TABLE IF NOT EXISTS planets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS landmarks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    planet_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50),
    coordinates VARCHAR(50),
    FOREIGN KEY (planet_id) REFERENCES planets(id)
);

-- Sample data
INSERT INTO planets (name, description) VALUES
('Mars', 'The Red Planet'),
('Moon', 'Earth’s only natural satellite');

INSERT INTO landmarks (planet_id, name, type, coordinates) VALUES
(1, 'Olympus Mons', 'Mountain', '18.65N, 226.2E'),
(1, 'Valles Marineris', 'Canyon', '14.0S, 75.0W'),
(2, 'Tranquility Base', 'Landing Site', '0.674N, 23.473E');
