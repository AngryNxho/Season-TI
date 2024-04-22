-- 1.	Lee atentamente la contextualización del caso.
-- 2.	Crea las sentencias SQL DDL para construir el modelo físico de la base de datos. 
-- 3.	Crea las sentencias DML para poblar los datos solicitados, usando la herramienta Oracle SQL Developer Data Modeler.
-- 4.	Ordena las ventas ascendentemente por fecha de boleta y descendentemente por monto de la venta.
-- 5.	Construye el script para crear y poblar las tablas del modelo relacional con los datos planteados. 

-- DROP TABLE tipo_empleado;
-- DROP TABLE tabla_empleado;
-- DROP TABLE tabla_ventas;
-- DROP TABLE comision_ventas;


CREATE TABLE tipo_empleado (
    TIPO_EMPLEADO NUMBER(2) NOT NULL PRIMARY KEY,
    DESC_TIPO_EMPLEADO VARCHAR2(25) NOT NULL
);

INSERT INTO tipo_empleado (TIPO_EMPLEADO, DESC_TIPO_EMPLEADO) VALUES (1, 'Administrativo');
INSERT INTO tipo_empleado (TIPO_EMPLEADO, DESC_TIPO_EMPLEADO) VALUES (2, 'Cocinero');
INSERT INTO tipo_empleado (TIPO_EMPLEADO, DESC_TIPO_EMPLEADO) VALUES (3, 'Vendedor');
INSERT INTO tipo_empleado (TIPO_EMPLEADO, DESC_TIPO_EMPLEADO) VALUES (4, 'Repartidor');




CREATE TABLE tabla_empleado (
    ID_EMPLEADO NUMBER(5) NOT NULL PRIMARY KEY,
    NUMRUT NUMBER(10) NOT NULL,
    DVRUT VARCHAR2(1) NOT NULL,
    PNOMBRE VARCHAR2(20) NOT NULL,
    SNOMBRE VARCHAR2(20),
    APPATERNO VARCHAR2(20) NOT NULL,
    APMATERNO VARCHAR2(20) NOT NULL,
    FECHA_CONTRATO DATE NOT NULL ,
    TIPO_EMPLEADO NUMBER(2) NOT NULL
);



INSERT INTO tabla_empleado (ID_EMPLEADO, NUMRUT, DVRUT, PNOMBRE, SNOMBRE, APPATERNO, APMATERNO, FECHA_CONTRATO, TIPO_EMPLEADO) VALUES (4, 5555555, 5, 'MARIA', NULL, 'ROMERO', 'ROJAS', TO_DATE('01-08-12','DD-MM-YYYY' ), 1);
INSERT INTO tabla_empleado (ID_EMPLEADO, NUMRUT, DVRUT, PNOMBRE, SNOMBRE, APPATERNO, APMATERNO, FECHA_CONTRATO, TIPO_EMPLEADO) VALUES (5, 6666666, 6, 'SONIA', 'EUGENIA', 'TAPIA', 'VEGA', TO_DATE('01-08-12','DD-MM-YYYY' ), 2);
INSERT INTO tabla_empleado (ID_EMPLEADO, NUMRUT, DVRUT, PNOMBRE, SNOMBRE, APPATERNO, APMATERNO, FECHA_CONTRATO, TIPO_EMPLEADO) VALUES (1, 2222222, 2, 'PABLO', NULL, 'PEREZ', 'SOTO', TO_DATE('01-03-10','DD-MM-YYYY' ), 3);
INSERT INTO tabla_empleado (ID_EMPLEADO, NUMRUT, DVRUT, PNOMBRE, SNOMBRE, APPATERNO, APMATERNO, FECHA_CONTRATO, TIPO_EMPLEADO) VALUES (2, 3333333, 3, 'PEDRO', 'JOSE', 'TORRES', 'TRONCOSO', TO_DATE('14-03-11','DD-MM-YYYY' ), 3);
INSERT INTO tabla_empleado (ID_EMPLEADO, NUMRUT, DVRUT, PNOMBRE, SNOMBRE, APPATERNO, APMATERNO, FECHA_CONTRATO, TIPO_EMPLEADO) VALUES (3, 4444444, 4, 'FRANCISCO', 'ALEJANDRO', 'AGUILAR', 'TAPIA', TO_DATE('01-06-11','DD-MM-YYYY' ), 3);



CREATE TABLE tabla_ventas (
    NRO_BOLETA NUMBER(8) NOT NULL PRIMARY KEY,
    ID_EMPLEADO NUMBER(5) NOT NULL,
    FECHA_BOLETA DATE NOT NULL,
    MONTO_TOTAL NUMBER(8) NOT NULL
);

INSERT INTO tabla_ventas (NRO_BOLETA, ID_EMPLEADO, FECHA_BOLETA, MONTO_TOTAL) VALUES (
    100, 1, TO_DATE('01-03-2014', 'DD-MM-YYYY'), 200000);

INSERT INTO tabla_ventas (NRO_BOLETA, ID_EMPLEADO, FECHA_BOLETA, MONTO_TOTAL) VALUES (
    101, 1, TO_DATE('02-03-2014', 'DD-MM-YYYY'), 100000);

INSERT INTO tabla_ventas (NRO_BOLETA, ID_EMPLEADO, FECHA_BOLETA, MONTO_TOTAL) VALUES (
    102, 1, TO_DATE('02-03-2014', 'DD-MM-YYYY'), 75000);

INSERT INTO tabla_ventas (NRO_BOLETA, ID_EMPLEADO, FECHA_BOLETA, MONTO_TOTAL) VALUES (
    103, 3, TO_DATE('02-03-2014', 'DD-MM-YYYY'), 45200);

INSERT INTO tabla_ventas (NRO_BOLETA, ID_EMPLEADO, FECHA_BOLETA, MONTO_TOTAL) VALUES (
    90, 3, TO_DATE('02-02-2014', 'DD-MM-YYYY'), 75000);

SELECT * FROM tabla_ventas
ORDER BY FECHA_BOLETA ASC, MONTO_TOTAL DESC;


CREATE TABLE comision_ventas (
    NRO_BOLETA NUMBER(8) NOT NULL PRIMARY KEY,
    MONTO_COMISION NUMBER(8) NOT NULL
);

INSERT INTO comision_ventas (NRO_BOLETA, MONTO_COMISION) VALUES (100, 26000);
INSERT INTO comision_ventas (NRO_BOLETA, MONTO_COMISION) VALUES (101, 13000);
INSERT INTO comision_ventas (NRO_BOLETA, MONTO_COMISION) VALUES (102, 9750);
INSERT INTO comision_ventas (NRO_BOLETA, MONTO_COMISION) VALUES (103, 5876);
INSERT INTO comision_ventas (NRO_BOLETA, MONTO_COMISION) VALUES (90, 9750);

ALTER TABLE tabla_ventas ADD CONSTRAINT fk_empleado_ventas FOREIGN KEY (ID_EMPLEADO) 
REFERENCES tabla_empleado (ID_EMPLEADO);


ALTER TABLE tabla_empleado ADD CONSTRAINT fk_empleado_tipo_empleado FOREIGN KEY (TIPO_EMPLEADO) 
REFERENCES tipo_empleado (TIPO_EMPLEADO);