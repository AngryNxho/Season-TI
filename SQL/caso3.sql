-- Creación de la tabla cliente
CREATE TABLE cliente (
    numrut_cli NUMBER(10) NOT NULL,
    dvrut_cli VARCHAR2(1) NOT NULL,
    appaterno_cli VARCHAR2(15) NOT NULL,
    apmaterno_cli VARCHAR2(15),
    nombre_cli VARCHAR2(25) NOT NULL,
    direccion_cli VARCHAR2(40),
    estcivil VARCHAR2(10) CHECK (estcivil IN ('Soltero', 'Casado', 'Divorciado', 'Viudo', 'Conviviente Civil')),
    CONSTRAINT pk_cliente PRIMARY KEY (numrut_cli)
);

-- Creación de la tabla categoria
CREATE TABLE categoria (
    id_categoria NUMBER(1) NOT NULL,
    nom_categoria VARCHAR2(30) NOT NULL,
    CONSTRAINT pk_categoria PRIMARY KEY (id_categoria)
);

-- Creación de la tabla empleado
CREATE TABLE empleado (
    numrut_emp NUMBER(10) NOT NULL,
    dvrut_emp VARCHAR2(1) NOT NULL,
    nombre_emp VARCHAR2(60) NOT NULL,
    direccion_emp VARCHAR2(60),
    fecing_emp DATE DEFAULT SYSDATE NOT NULL,
    sueldo_emp NUMBER(7) NOT NULL,
    id_categoria NUMBER(1),
    numrut_superv NUMBER(10),
    CONSTRAINT pk_empleado PRIMARY KEY (numrut_emp),
    CONSTRAINT fk_empleado_categoria FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);

-- Creación de la tabla tipo_propiedad
CREATE TABLE tipo_propiedad (
    id_tipo_propiedad NUMBER(5) NOT NULL,
    desc_tipo_propiedad VARCHAR2(100) NOT NULL,
    CONSTRAINT pk_tipo_propiedad PRIMARY KEY (id_tipo_propiedad)
);

-- Inserción en tipo_propiedad
INSERT INTO tipo_propiedad (id_tipo_propiedad, desc_tipo_propiedad) VALUES (1005, 'CASA');
INSERT INTO tipo_propiedad (id_tipo_propiedad, desc_tipo_propiedad) VALUES (1010, 'DEPARTAMENTO');
INSERT INTO tipo_propiedad (id_tipo_propiedad, desc_tipo_propiedad) VALUES (1015, 'LOFT');
INSERT INTO tipo_propiedad (id_tipo_propiedad, desc_tipo_propiedad) VALUES (1020, 'LOCAL');
INSERT INTO tipo_propiedad (id_tipo_propiedad, desc_tipo_propiedad) VALUES (1025, 'SITIO');
INSERT INTO tipo_propiedad (id_tipo_propiedad, desc_tipo_propiedad) VALUES (1030, 'PARCELA CON CASA');

-- Creación de la tabla comuna
CREATE TABLE comuna (
    id_comuna NUMBER(3) NOT NULL,
    nom_comuna VARCHAR2(20) NOT NULL,
    CONSTRAINT pk_comuna PRIMARY KEY (id_comuna)
);

-- Creación de la tabla propiedad
CREATE TABLE propiedad (
    nro_propiedad NUMBER(4) NOT NULL,
    direccion_propiedad VARCHAR2(60) NOT NULL,
    nro_dormitorios NUMBER(1) NOT NULL,
    nro_banos NUMBER(1) NOT NULL,
    valor_arriendo NUMBER(8) CHECK (valor_arriendo <= 600000) NOT NULL,
    valor_gastoscomun NUMBER(6),
    id_tipo_propiedad NUMBER(2),
    id_comuna NUMBER(3),
    CONSTRAINT pk_propiedad PRIMARY KEY (nro_propiedad),
    CONSTRAINT fk_propiedad_tipopropiedad FOREIGN KEY (id_tipo_propiedad) REFERENCES tipo_propiedad(id_tipo_propiedad),
    CONSTRAINT fk_propiedad_comuna FOREIGN KEY (id_comuna) REFERENCES comuna(id_comuna)
);

-- Creación de la tabla telefono
CREATE TABLE telefono (
    nro_telefono NUMBER(15) NOT NULL,
    numrut_emp NUMBER(10) NOT NULL,
    tipo_telefono VARCHAR2(12),
    CONSTRAINT pk_telefono PRIMARY KEY (nro_telefono),
    CONSTRAINT fk_telefono_empleado FOREIGN KEY (numrut_emp) REFERENCES empleado(numrut_emp)
);

-- Creación de la tabla visita_propiedad
CREATE TABLE visita_propiedad (
    numrut_cli NUMBER(10) NOT NULL,
    nro_propiedad NUMBER(4) NOT NULL,
    fecha_visita DATE NOT NULL,
    comentarios VARCHAR2(200),
    CONSTRAINT pk_visita_propiedad PRIMARY KEY (numrut_cli),
    CONSTRAINT fk_visita_cliente FOREIGN KEY (numrut_cli) REFERENCES cliente(numrut_cli),
    CONSTRAINT fk_visita_propiedad FOREIGN KEY (nro_propiedad) REFERENCES propiedad(nro_propiedad)
);