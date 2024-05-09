-- borrado de objetos
DROP TABLE cliente CASCADE CONSTRAINTS;
DROP TABLE comuna CASCADE CONSTRAINTS;
DROP TABLE categoria CASCADE CONSTRAINTS;



CREATE TABLE categoria
(   id_categoria NUMERIC(1) NOT NULL,
    desc_categoria VARCHAR2(30) NOT NULL,
    CONSTRAINT pk_categoria_empleado PRIMARY KEY (id_categoria));

CREATE TABLE cliente
(   numrut_cli NUMERIC(10) NOT NULL,
    dvrut_cli  VARCHAR2(1) NOT NULL,
    appaterno_cli VARCHAR2(15) NOT NULL,
    apmaterno_cli VARCHAR2(15) NOT NULL,
    nombre_cli VARCHAR2(25) NOT NULL,
    direccion_cli VARCHAR2(60) NOT NULL,
    estcivil   VARCHAR(10) NOT NULL, 
    CONSTRAINT pk_cliente PRIMARY KEY (numrut_cli)
);

-- creacion de llaves foraneas 
ALTER TABLE propiedad
  ADD CONSTRAINT fk_propiedad_comuna FOREIGN KEY (id_comuna)
  REFERENCES comuna (id_comuna);

-- insercion de datos
INSERT INTO comuna VALUES (1, 'Santiago');
INSERT INTO comuna VALUES (2, 'Vi�a del Mar');

INSERT INTO categoria VALUES (1, 'Categoria 1');
INSERT INTO categoria VALUES (2, 'Categoria 2');

INSERT INTO CLIENTE (NUMRUT_CLI, DVRUT_CLI, APPATERNO_CLI, APMATERNO_CLI, NOMBRE_CLI, DIRECCION_CLI, 
                     estcivil)
VALUES (5, '5', 'VALENZUELA', 'C', 'BRYAN', 'Ahumada 254', 'Soltero');

INSERT INTO CLIENTE (NUMRUT_CLI, DVRUT_CLI, APPATERNO_CLI, APMATERNO_CLI, NOMBRE_CLI, DIRECCION_CLI, 
                     estcivil)
VALUES (6, '6', 'GONZALEZ', 'M', 'MURIEL', 'Ahumada 254', 'Viudo');
COMMIT;


