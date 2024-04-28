CREATE TABLE nacionalidad(
    id_nacionalidad NUMBER(3) CONSTRAINT NACIONALIDAD_PK PRIMARY KEY ,
    desc_nacionalidad VARCHAR2(20) NOT NULL
);

INSERT INTO nacionalidad(id_nacionalidad, desc_nacionalidad) VALUES (100, 'CHILENA');
INSERT INTO nacionalidad(id_nacionalidad, desc_nacionalidad) VALUES (110, 'BRITANICA');
INSERT INTO nacionalidad(id_nacionalidad, desc_nacionalidad) VALUES (120, 'ESPAÑOLA');
INSERT INTO nacionalidad(id_nacionalidad, desc_nacionalidad) VALUES (130, 'FRANCESA');
INSERT INTO nacionalidad(id_nacionalidad, desc_nacionalidad) VALUES (140, 'MEXICANO');


SELECT * FROM nacionalidad;

CREATE TABLE editorial(
    id_editorial NUMBER CONSTRAINT EDITORIAL_PK PRIMARY KEY NOT NULL,
    nombre_editorial VARCHAR2(20)
);

INSERT INTO editorial(id_editorial, nombre_editorial) VALUES (1, 'ALFAGUARA');
INSERT INTO editorial(id_editorial, nombre_editorial) VALUES (2, 'GEORGE ALLEN & UNWIN');
INSERT INTO editorial(id_editorial, nombre_editorial) VALUES (3, 'SALAMANDRA');
INSERT INTO editorial(id_editorial, nombre_editorial) VALUES (4, 'CONTINENTAL');

SELECT * FROM editorial;

CREATE TABLE autor(
    id_autor NUMBER(5) NOT NULL CONSTRAINT PK_LIBRO_AUTOR PRIMARY KEY,
    nombre_autor VARCHAR2(20) NOT NULL ,
    ap_pat_autor VARCHAR2(20) NOT NULL ,
    ap_mat_autor VARCHAR2(20),
    id_nacionalidad NUMBER(3) NOT NULL
);
INSERT INTO autor(id_autor, nombre_autor, ap_pat_autor, ap_mat_autor, id_nacionalidad) VALUES
(1, 'MIGUEL', 'CERVANTES', NULL, 120);
INSERT INTO autor(id_autor, nombre_autor, ap_pat_autor, ap_mat_autor, id_nacionalidad) VALUES
(2, 'J. R. R.', 'TOLKIEN', NULL, 110);
INSERT INTO autor(id_autor, nombre_autor, ap_pat_autor, ap_mat_autor, id_nacionalidad) VALUES
(3, 'J.K.', 'ROWLING', NULL, 110);
INSERT INTO autor(id_autor, nombre_autor, ap_pat_autor, ap_mat_autor, id_nacionalidad) VALUES
(4, 'ANTOINE', 'DE SAINT-EXUPÉRY', NULL, 130);


ALTER TABLE autor ADD CONSTRAINT AUTOR_LIBROA_FK FOREIGN KEY (id_nacionalidad)
REFERENCES  nacionalidad (id_nacionalidad);

SELECT * FROM AUTOR;

CREATE TABLE tipo_usuario(
    id_tipo_us NUMBER(8) NOT NULL CONSTRAINT TIPO_USUARIO_PK PRIMARY KEY,
    desc_tipo_us VARCHAR2(20) NOT NULL
);

INSERT INTO tipo_usuario(id_tipo_us, desc_tipo_us) VALUES (1, 'PROFESOR');
INSERT INTO tipo_usuario(id_tipo_us, desc_tipo_us) VALUES (2, 'ESTUDIANTE');

ALTER TABLE tipo_usuario ADD CONSTRAINT TIPO_USUARIO_USUARIO_FK FOREIGN KEY (id_tipo_us)
REFERENCES usuario (id_tipo_us)


CREATE TABLE libro(
    isbn_libro CHAR(13) NOT NULL CONSTRAINT PK_LIBRO PRIMARY KEY,
    titulo_libro VARCHAR2(50) NOT NULL,
    num_pag_libro NUMBER(5) NOT NULL,
    anno_pub_libro NUMBER(4) NOT NULL,
    id_autor NUMBER(5) NOT NULL,
    id_editorial NUMBER(5) NOT NULL,
    CONSTRAINT FK_LIBRO_AUTOR FOREIGN KEY (id_autor)
    REFERENCES autor (id_autor),
    CONSTRAINT FK_LIBRO_EDITORIAL FOREIGN KEY (id_editorial)
    REFERENCES editorial (id_editorial)
);

INSERT INTO libro (isbn_libro, titulo_libro, num_pag_libro, anno_pub_libro, id_autor, id_editorial) VALUES
('9788420403021', 'EL QUIJOTE', 1424, 2013, 1, 1);
INSERT INTO libro (isbn_libro, titulo_libro, num_pag_libro, anno_pub_libro, id_autor, id_editorial) VALUES
('9788498380170', 'HARRY POTTER Y LA PIEDRA FILOSOFAL', 288, 2021, 3, 3);
INSERT INTO libro (isbn_libro, titulo_libro, num_pag_libro, anno_pub_libro, id_autor, id_editorial) VALUES
('9781937482978', 'EL PRINCIPITO', 117, 2014, 4, 4);
INSERT INTO libro (isbn_libro, titulo_libro, num_pag_libro, anno_pub_libro, id_autor, id_editorial) VALUES
('8445071793', 'EL SEÑOR DE LOS ANILLOS', 1272, 1995, 2, 2);


CREATE TABLE usuario(
    id_usuario NUMBER(7) NOT NULL CONSTRAINT PK_USUARIO PRIMARY KEY,
    run_usuario CHAR(8) NOT NULL,
    dv_usuario CHAR(1) NOT NULL,
    nombre_usuario VARCHAR2(20) NOT NULL,
    ap_pat_usuario VARCHAR2(20) NOT NULL,
    ap_mat_usuario VARCHAR2(20),
    direcc_usuario VARCHAR2(50) NOT NULL,
    tel_usuario NUMBER(15),
    email_usuario VARCHAR2(50),
    id_tipo NUMBER(8) NOT NULL,
    CONSTRAINT FK_USUARIO_TIPO FOREIGN KEY (id_tipo)
    REFERENCES tipo_usuario (id_tipo_us)
);

INSERT INTO usuario (id_usuario, run_usuario, dv_usuario, nombre_usuario, ap_pat_usuario, ap_mat_usuario, direcc_usuario, tel_usuario, email_usuario, id_tipo) VALUES
(1, '10214564', 'K', 'VIVIANA JACQUELINE', 'ALARCON', 'CACERES', 'SOTOMAYOR N° 728', 92293759, 'VALARCON@GMAIL.COM', 2);
INSERT INTO usuario (id_usuario, run_usuario, dv_usuario, nombre_usuario, ap_pat_usuario, ap_mat_usuario, direcc_usuario, tel_usuario, email_usuario, id_tipo) VALUES
(2, '3781561', '6', 'MARIA LUCILA', 'ALARCON', 'SEPULVEDA', 'AVENIDA GRECIA N° 2030', 92293760, 'MLARCON@GMAIL.COM', 1);
INSERT INTO usuario (id_usuario, run_usuario, dv_usuario, nombre_usuario, ap_pat_usuario, ap_mat_usuario, direcc_usuario, tel_usuario, email_usuario, id_tipo) VALUES
(3, '4884829', 'K', 'FLOR MARIA', 'ALVAREZ', 'CACERES', 'CALLE RANCAGUA N° 499', 92293761, 'FALVAREZ@GMAIL.COM', 1);
INSERT INTO usuario (id_usuario, run_usuario, dv_usuario, nombre_usuario, ap_pat_usuario, ap_mat_usuario, direcc_usuario, tel_usuario, email_usuario, id_tipo) VALUES
(4, '3758049', 'K', 'HECTOR RENE', 'ANDRADE', 'FAUNDEZ', 'CALLE BRASIL N° 366', 92293762, 'HANDRADE@GMAIL.COM', 1);


SELECT * FROM usuario;












CREATE TABLE bibliotecario(
    run_biblio CHAR(8) NOT NULL CONSTRAINT PK_BIBLIO PRIMARY KEY,
    dv_biblio VARCHAR2(2) NOT NULL,
    nombre_biblio VARCHAR2(20) NOT NULL,
    ap_pat_biblio VARCHAR2(20) NOT NULL,
    ap_mat_biblio VARCHAR2(20),
    direcc_biblio VARCHAR2(50) NOT NULL,
    tel_biblio NUMBER(15),
    email_biblio VARCHAR2(60)
);

INSERT INTO bibliotecario (run_biblio, dv_biblio, nombre_biblio, ap_pat_biblio, ap_mat_biblio, direcc_biblio, tel_biblio, email_biblio) VALUES
('9274151', '9', 'ELIZABETH', 'GRACIANA', 'BARRERA', 'AV. ALMIRANTE SIPSON N° 367', 92293769, 'EBARRERA@GMAIL.COM');
INSERT INTO bibliotecario (run_biblio, dv_biblio, nombre_biblio, ap_pat_biblio, ap_mat_biblio, direcc_biblio, tel_biblio, email_biblio) VALUES
('3062656', '3', 'OLGA', 'BELMAR', 'LAMILA', 'JORGE MONT 710', 92293770, 'OBELMAR@GMAIL.COM');
INSERT INTO bibliotecario (run_biblio, dv_biblio, nombre_biblio, ap_pat_biblio, ap_mat_biblio, direcc_biblio, tel_biblio, email_biblio) VALUES
('5643549', '2', 'RAMON ANTONIO', 'CONTRERAS', 'TOLEDO', 'AVDA. LITORAL N° 335, ROCAS SANTO DOMINGO', 92293796, 'RCONTRERAS@GMAIL.COM');
INSERT INTO bibliotecario (run_biblio, dv_biblio, nombre_biblio, ap_pat_biblio, ap_mat_biblio, direcc_biblio, tel_biblio, email_biblio) VALUES
('4378812', '4', 'JULIA IRIS', 'CHAVARRIA', 'GUTIERREZ', 'MATAVERI ESQUINA MANUTARA S/N', 92293797, 'JCHAVARRIA@GMAIL.COM');

SELECT * FROM bibliotecario;