-- DDL  para eliminaci�n de tablas
DROP TABLE asignacion;
DROP TABLE profesor;
DROP TABLE asignatura;

-- DDL  para creaci�n de tablas
CREATE TABLE profesor (
    rut_profesor VARCHAR2(10) CONSTRAINT pk_rut_pro PRIMARY KEY
    ,nombre_profesor    VARCHAR2(50) NOT NULL
);

CREATE TABLE asignatura (
    sigla           VARCHAR2(3)
    ,descripcion    VARCHAR2(50) CONSTRAINT desc_nonulo NOT NULL
    ,CONSTRAINT pk_sig_asi PRIMARY KEY (sigla)
);

-- CREACI�N DE LLAVES FORANEAS EN FORMA INTERNA
CREATE TABLE asignacion (
    rut_profesor        VARCHAR2(10)    CONSTRAINT fk_pro_asig REFERENCES profesor(rut_profesor)
    ,sigla              VARCHAR2(3)     NOT NULL
    ,fecha_asignacion   DATE            NOT NULL
    ,horas_asignadas    NUMBER(3)
    ,CONSTRAINT fk_asi_asig FOREIGN KEY(sigla) REFERENCES asignatura(sigla)
);

ALTER TABLE asignacion 
    ADD CONSTRAINT pk_rut_sig_asi PRIMARY KEY (rut_profesor, sigla);

-- CREACI�N DE LLAVES FORANEAS EN FORMA INTERNA
CREATE TABLE asignacion (
    rut_profesor        VARCHAR2(10)    
    ,sigla              VARCHAR2(3)     NOT NULL
    ,fecha_asignacion   DATE            NOT NULL
    ,horas_asignadas    NUMBER(3)
);

ALTER TABLE asignacion 
    ADD CONSTRAINT pk_rut_sig_asi PRIMARY KEY (rut_profesor, sigla);
    
ALTER TABLE asignacion 
    ADD CONSTRAINT fk_pro_asig FOREIGN KEY (rut_profesor) REFERENCES profesor(rut_profesor);

ALTER TABLE asignacion 
    ADD CONSTRAINT fk_asi_asig FOREIGN KEY (sigla) REFERENCES asignatura(sigla);

