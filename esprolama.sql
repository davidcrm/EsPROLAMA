--
-- PostgreSQL database dump
--

-- Dumped from database version 16.8 (Debian 16.8-1.pgdg120+1)
-- Dumped by pg_dump version 16.8 (Debian 16.8-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.auth_group (
    id bigint NOT NULL,
    name text
);


ALTER TABLE public.auth_group OWNER TO elama;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: elama
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_group_id_seq OWNER TO elama;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: elama
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id bigint,
    permission_id bigint
);


ALTER TABLE public.auth_group_permissions OWNER TO elama;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: elama
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_group_permissions_id_seq OWNER TO elama;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: elama
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.auth_permission (
    id bigint NOT NULL,
    content_type_id bigint,
    codename text,
    name text
);


ALTER TABLE public.auth_permission OWNER TO elama;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: elama
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_permission_id_seq OWNER TO elama;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: elama
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.auth_user (
    id bigint NOT NULL,
    password text,
    last_login timestamp with time zone,
    is_superuser boolean,
    username text,
    last_name text,
    email text,
    is_staff boolean,
    is_active boolean,
    date_joined timestamp with time zone,
    first_name text
);


ALTER TABLE public.auth_user OWNER TO elama;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id bigint,
    group_id bigint
);


ALTER TABLE public.auth_user_groups OWNER TO elama;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: elama
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_user_groups_id_seq OWNER TO elama;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: elama
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: elama
--

CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_user_id_seq OWNER TO elama;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: elama
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id bigint,
    permission_id bigint
);


ALTER TABLE public.auth_user_user_permissions OWNER TO elama;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: elama
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNER TO elama;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: elama
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.django_admin_log (
    id bigint NOT NULL,
    object_id text,
    object_repr text,
    action_flag smallint,
    change_message text,
    content_type_id bigint,
    user_id bigint,
    action_time timestamp with time zone
);


ALTER TABLE public.django_admin_log OWNER TO elama;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: elama
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.django_admin_log_id_seq OWNER TO elama;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: elama
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.django_content_type (
    id bigint NOT NULL,
    app_label text,
    model text
);


ALTER TABLE public.django_content_type OWNER TO elama;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: elama
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.django_content_type_id_seq OWNER TO elama;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: elama
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app text,
    name text,
    applied timestamp with time zone
);


ALTER TABLE public.django_migrations OWNER TO elama;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: elama
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.django_migrations_id_seq OWNER TO elama;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: elama
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.django_session (
    session_key text NOT NULL,
    session_data text,
    expire_date timestamp with time zone
);


ALTER TABLE public.django_session OWNER TO elama;

--
-- Name: elama_autoevaluacion; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.elama_autoevaluacion (
    id bigint NOT NULL,
    fecha_hora timestamp with time zone,
    finalizada boolean
);


ALTER TABLE public.elama_autoevaluacion OWNER TO elama;

--
-- Name: elama_autoevaluacion_id_seq; Type: SEQUENCE; Schema: public; Owner: elama
--

CREATE SEQUENCE public.elama_autoevaluacion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.elama_autoevaluacion_id_seq OWNER TO elama;

--
-- Name: elama_autoevaluacion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: elama
--

ALTER SEQUENCE public.elama_autoevaluacion_id_seq OWNED BY public.elama_autoevaluacion.id;


--
-- Name: elama_descriptor; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.elama_descriptor (
    id bigint NOT NULL,
    titulo text,
    contenido_html text,
    descriptor_padre_id bigint,
    principio_id bigint
);


ALTER TABLE public.elama_descriptor OWNER TO elama;

--
-- Name: elama_descriptor_id_seq; Type: SEQUENCE; Schema: public; Owner: elama
--

CREATE SEQUENCE public.elama_descriptor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.elama_descriptor_id_seq OWNER TO elama;

--
-- Name: elama_descriptor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: elama
--

ALTER SEQUENCE public.elama_descriptor_id_seq OWNED BY public.elama_descriptor.id;


--
-- Name: elama_estrategia; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.elama_estrategia (
    id bigint NOT NULL,
    titulo text
);


ALTER TABLE public.elama_estrategia OWNER TO elama;

--
-- Name: elama_estrategia_id_seq; Type: SEQUENCE; Schema: public; Owner: elama
--

CREATE SEQUENCE public.elama_estrategia_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.elama_estrategia_id_seq OWNER TO elama;

--
-- Name: elama_estrategia_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: elama
--

ALTER SEQUENCE public.elama_estrategia_id_seq OWNED BY public.elama_estrategia.id;


--
-- Name: elama_principio; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.elama_principio (
    id bigint NOT NULL,
    titulo text,
    estrategia_id bigint
);


ALTER TABLE public.elama_principio OWNER TO elama;

--
-- Name: elama_principio_id_seq; Type: SEQUENCE; Schema: public; Owner: elama
--

CREATE SEQUENCE public.elama_principio_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.elama_principio_id_seq OWNER TO elama;

--
-- Name: elama_principio_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: elama
--

ALTER SEQUENCE public.elama_principio_id_seq OWNED BY public.elama_principio.id;


--
-- Name: elama_volcado; Type: TABLE; Schema: public; Owner: elama
--

CREATE TABLE public.elama_volcado (
    id bigint NOT NULL,
    valoracion text,
    autoevaluacion_id bigint,
    descriptor_id bigint
);


ALTER TABLE public.elama_volcado OWNER TO elama;

--
-- Name: elama_volcado_id_seq; Type: SEQUENCE; Schema: public; Owner: elama
--

CREATE SEQUENCE public.elama_volcado_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.elama_volcado_id_seq OWNER TO elama;

--
-- Name: elama_volcado_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: elama
--

ALTER SEQUENCE public.elama_volcado_id_seq OWNED BY public.elama_volcado.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: elama_autoevaluacion id; Type: DEFAULT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_autoevaluacion ALTER COLUMN id SET DEFAULT nextval('public.elama_autoevaluacion_id_seq'::regclass);


--
-- Name: elama_descriptor id; Type: DEFAULT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_descriptor ALTER COLUMN id SET DEFAULT nextval('public.elama_descriptor_id_seq'::regclass);


--
-- Name: elama_estrategia id; Type: DEFAULT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_estrategia ALTER COLUMN id SET DEFAULT nextval('public.elama_estrategia_id_seq'::regclass);


--
-- Name: elama_principio id; Type: DEFAULT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_principio ALTER COLUMN id SET DEFAULT nextval('public.elama_principio_id_seq'::regclass);


--
-- Name: elama_volcado id; Type: DEFAULT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_volcado ALTER COLUMN id SET DEFAULT nextval('public.elama_volcado_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.auth_permission (id, content_type_id, codename, name) FROM stdin;
1       1       add_logentry    Can add log entry
2       1       change_logentry Can change log entry
3       1       delete_logentry Can delete log entry
4       1       view_logentry   Can view log entry
5       2       add_permission  Can add permission
6       2       change_permission       Can change permission
7       2       delete_permission       Can delete permission
8       2       view_permission Can view permission
9       3       add_group       Can add group
10      3       change_group    Can change group
11      3       delete_group    Can delete group
12      3       view_group      Can view group
13      4       add_user        Can add user
14      4       change_user     Can change user
15      4       delete_user     Can delete user
16      4       view_user       Can view user
17      5       add_contenttype Can add content type
18      5       change_contenttype      Can change content type
19      5       delete_contenttype      Can delete content type
20      5       view_contenttype        Can view content type
21      6       add_session     Can add session
22      6       change_session  Can change session
23      6       delete_session  Can delete session
24      6       view_session    Can view session
25      7       add_principio   Can add principio
26      7       change_principio        Can change principio
27      7       delete_principio        Can delete principio
28      7       view_principio  Can view principio
29      8       add_estrategia  Can add estrategia
30      8       change_estrategia       Can change estrategia
31      8       delete_estrategia       Can delete estrategia
32      8       view_estrategia Can view estrategia
33      9       add_descriptor  Can add descriptor
34      9       change_descriptor       Can change descriptor
35      9       delete_descriptor       Can delete descriptor
36      9       view_descriptor Can view descriptor
37      10      add_autoevaluacion      Can add autoevaluacion
38      10      change_autoevaluacion   Can change autoevaluacion
39      10      delete_autoevaluacion   Can delete autoevaluacion
40      10      view_autoevaluacion     Can view autoevaluacion
41      11      add_volcado     Can add volcado
42      11      change_volcado  Can change volcado
43      11      delete_volcado  Can delete volcado
44      11      view_volcado    Can view volcado
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.auth_user (id, password, last_login, is_superuser, username, last_name, email, is_staff, is_active, date_joined, first_name) FROM stdin;
1       pbkdf2_sha256$870000$bDP11XkpChte4CmGKtegWL$B7yAK0TE47yIGrdLwSaIWQbI99UTMgrncU16fTTFKy0=        2025-03-14 15:43:17.68975+00    t       elama                   t       t       2024-06-05 18:07:47.35072+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.django_admin_log (id, object_id, object_repr, action_flag, change_message, content_type_id, user_id, action_time) FROM stdin;
1       1       Estrategias institucionales     1       [{"added": {}}] 8       1       2024-06-05 18:19:48.774586+00
2       2       Estrategias pedagógicas y de integración        1       [{"added": {}}] 8       1       2024-06-05 18:20:09.228185+00
3       1       1. Establecer las bases del programa    1       [{"added": {}}] 7       1       2024-06-05 18:20:37.166092+00
4       2       2. Dotarse de equipos para hacer posible el programa    1       [{"added": {}}] 7       1       2024-06-05 18:22:01.780818+00
5       3       3. Dotarse de espacios para el desarrollo del programa  1       [{"added": {}}] 7       1       2024-06-05 18:22:21.669837+00
6       4       4. Dotarse de recursos para la enseñanza de ELA en el programa. 1       [{"added": {}}] 7       1      2024-06-05 18:22:48.45473+00
7       5       5. Asegurar el funcionamiento adecuado del programa.    1       [{"added": {}}] 7       1       2024-06-05 18:23:12.781947+00
8       6       6. Promocionar el aprendizaje de ELA y difundir el programa.    1       [{"added": {}}] 7       1      2024-06-05 18:23:39.028142+00
9       7       7. Recoger datos, evaluar y mejorar el programa.        1       [{"added": {}}] 7       1       2024-06-05 18:23:59.830407+00
10      1       1. Establecer las bases del programa.   2       [{"changed": {"fields": ["Titulo"]}}]   7       1      2024-06-05 18:24:09.068937+00
11      2       2. Dotarse de equipos para hacer posible el programa.   2       [{"changed": {"fields": ["Titulo"]}}]  71       2024-06-05 18:24:14.569988+00
12      3       3. Dotarse de espacios para el desarrollo del programa. 2       [{"changed": {"fields": ["Titulo"]}}]  71       2024-06-05 18:24:19.22232+00
13      8       8. Reclamar el desarrollo de políticas públicas de ELAMA.       1       [{"added": {}}] 7       1      2024-06-05 18:24:51.517251+00
14      9       A. Diseñar la oferta formativa del Programa de ELAMA.   1       [{"added": {}}] 7       1       2024-06-05 18:25:17.853393+00
15      10      B. Desarrollar el programa formativo de ELAMA.  1       [{"added": {}}] 7       1       2024-06-05 18:25:36.551081+00
16      11      C. Prestar servicios de apoyo para la integración.      1       [{"added": {}}] 7       1       2024-06-05 18:25:58.981366+00
17      1       1.1. Comprender de manera profunda el reto migratorio.  1       [{"added": {}}] 9       1       2024-06-05 18:49:27.661925+00
18      2       1.2. Concebir el aprendizaje de la lengua desde el derecho a la educación.      1       [{"added": {}}]91       2024-06-05 22:51:49.054973+00
19      3       1.3. Conocer iniciativas y experiencias de referencia.  1       [{"added": {}}] 9       1       2024-06-05 22:53:06.150987+00
20      4       1.4. Definir las bases del programa.    1       [{"added": {}}] 9       1       2024-06-05 22:53:31.842094+00
21      5       1.4.1. Enfatizar la orientación al alumno y la perspectiva de la educación de adultos.  1       [{"added": {}}] 9       1       2024-06-05 22:55:03.484104+00
22      6       1.4.2. Ir más allá del aprendizaje de la lengua.        1       [{"added": {}}] 9       1       2024-06-05 22:56:24.898718+00
23      7       1.4.3. Asumir presupuestos de educación inclusiva y emancipatoria.      1       [{"added": {}}] 9      12024-06-05 22:57:57.104575+00
24      8       1.4.4. Adoptar un enfoque de educación integral.        1       [{"added": {}}] 9       1       2024-06-05 22:59:25.829651+00
25      9       1.4.5. Adoptar un enfoque intercultural.        1       [{"added": {}}] 9       1       2024-06-05 23:00:32.93277+00
26      10      1.4.6. Asumir expectativas positivas de logro de los participantes.     1       [{"added": {}}] 9      12024-06-05 23:01:49.544596+00
27      11      1.5. Diseñar un plan para el desarrollo del programa.   1       [{"added": {}}] 9       1       2024-06-05 23:03:05.013165+00
28      12      1.6. Conseguir financiación y recursos para el programa.        1       [{"added": {}}] 9       1      2024-06-05 23:04:16.98608+00
29      13      2.1. Configurar el equipo docente.      1       [{"added": {}}] 9       1       2024-06-05 23:05:43.549033+00
30      14      2.1.1. Promover un perfil especializado.        1       [{"added": {}}] 9       1       2024-06-05 23:07:01.100853+00
31      1       1.1. Comprender de manera profunda el reto migratorio.  2       [{"changed": {"fields": ["Contenido html"]}}]   9       1       2024-06-15 21:03:38.329159+00
32      5       2024-06-16T09:30:45.134221+00:00        2       [{"changed": {"fields": ["Finalizada"]}}]       10     12024-06-16 10:05:30.390055+00
33      5       2024-06-16T09:30:45.134221+00:00        2       [{"changed": {"fields": ["Finalizada"]}}]       10     12024-06-16 10:17:04.678239+00
34      5       2024-06-16T09:30:45.134221+00:00        2       [{"changed": {"fields": ["Finalizada"]}}]       10     12024-06-16 13:10:52.312235+00
35      5       2024-06-16T09:30:45.134221+00:00        2       [{"changed": {"fields": ["Finalizada"]}}]       10     12024-06-16 13:44:20.87726+00
36      5       2024-06-16T09:30:45.134221+00:00        2       [{"changed": {"fields": ["Finalizada"]}}]       10     12024-06-16 13:54:10.132297+00
37      4       4. Dotarse de recursos para la enseñanza de español en el programa.     2       [{"changed": {"fields": ["Titulo"]}}]   7       1       2025-01-07 20:10:05.609798+00
38      2       1.2. Concebir la enseñanza del español como un derecho educativo.       2       [{"changed": {"fields": ["Titulo"]}}]   9       1       2025-01-07 20:12:46.916064+00
39      10      1.4.6. Asumir expectativas positivas de logro de los alumnos.   2       [{"changed": {"fields": ["Titulo"]}}]   9       1       2025-01-07 20:14:00.015957+00
40      11      1.5. Diseñar un plan de desarrollo del programa.        2       [{"changed": {"fields": ["Titulo"]}}]  91       2025-01-07 20:14:19.319213+00
41      1       1.1. Comprender de manera profunda el reto migratorio.  2       [{"changed": {"fields": ["Contenido html"]}}]   9       1       2025-01-07 20:46:49.262695+00
42      1       1.1. Comprender de manera profunda el reto migratorio.  2       [{"changed": {"fields": ["Contenido html"]}}]   9       1       2025-01-07 20:47:18.07957+00
43      1       1.1. Comprender de manera profunda el reto migratorio.  2       [{"changed": {"fields": ["Contenido html"]}}]   9       1       2025-01-07 20:54:19.650098+00
44      1       1.1. Comprender de manera profunda el reto migratorio.  2       [{"changed": {"fields": ["Contenido html"]}}]   9       1       2025-01-07 20:55:42.468306+00
45      2       1.2. Concebir la enseñanza del español como un derecho educativo.       2       [{"changed": {"fields": ["Contenido html"]}}]   9       1       2025-01-07 20:58:27.9679+00
46      3       1.3. Conocer iniciativas y experiencias de referencia.  2       [{"changed": {"fields": ["Contenido html"]}}]   9       1       2025-01-07 21:00:09.188016+00
47      2       1.2. Concebir la enseñanza del español como un derecho educativo.       2       []      9       1      2025-01-07 21:00:19.190315+00
48      4       1.4. Definir las bases del programa.    2       []      9       1       2025-01-07 21:00:31.822481+00
49      5       1.4.1. Enfatizar la orientación al alumno y la perspectiva de la educación de adultos.  2       []     91       2025-01-07 21:01:21.586565+00
50      6       1.4.2. Ir más allá del aprendizaje de la lengua.        2       [{"changed": {"fields": ["Contenido html"]}}]   9       1       2025-01-07 21:06:33.481576+00
51      7       1.4.3. Asumir presupuestos de educación inclusiva y emancipatoria.      2       []      9       1      2025-01-07 21:07:38.610266+00
52      8       1.4.4. Adoptar un enfoque de educación integral.        2       [{"changed": {"fields": ["Contenido html"]}}]   9       1       2025-01-07 21:09:00.442011+00
53      9       1.4.5. Adoptar un enfoque intercultural.        2       []      9       1       2025-01-07 21:09:57.54333+00
54      10      1.4.6. Asumir expectativas positivas de logro de los alumnos.   2       []      9       1       2025-01-07 21:11:17.004257+00
55      11      1.5. Diseñar un plan de desarrollo del programa.        2       []      9       1       2025-01-07 21:12:34.576392+00
56      12      1.6. Conseguir financiación y recursos para el programa.        2       [{"changed": {"fields": ["Contenido html"]}}]   9       1       2025-01-07 21:13:58.129793+00
57      13      2.1. Crear el equipo docente.   2       [{"changed": {"fields": ["Titulo"]}}]   9       1       2025-01-07 21:16:02.623002+00
58      13      2.1. Crear el equipo docente.   2       []      9       1       2025-01-07 21:16:32.376446+00
59      14      2.1.1. Promover un perfil especializado.        2       [{"changed": {"fields": ["Contenido html"]}}]  91       2025-01-07 21:18:14.467754+00
60      1       Estrategias institucionales     2       []      8       1       2025-01-07 21:18:42.912257+00
61      2       Estrategias pedagógicas y de integración        2       []      8       1       2025-01-07 21:18:45.304834+00
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1       admin   logentry
2       auth    permission
3       auth    group
4       auth    user
5       contenttypes    contenttype
6       sessions        session
7       elama   principio
8       elama   estrategia
9       elama   descriptor
10      elama   autoevaluacion
11      elama   volcado
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1       contenttypes    0001_initial    2024-06-05 18:06:17.748993+00
2       auth    0001_initial    2024-06-05 18:06:17.766115+00
3       admin   0001_initial    2024-06-05 18:06:17.780204+00
4       admin   0002_logentry_remove_auto_add   2024-06-05 18:06:17.795481+00
5       admin   0003_logentry_add_action_flag_choices   2024-06-05 18:06:17.801615+00
6       contenttypes    0002_remove_content_type_name   2024-06-05 18:06:17.816907+00
7       auth    0002_alter_permission_name_max_length   2024-06-05 18:06:17.828346+00
8       auth    0003_alter_user_email_max_length        2024-06-05 18:06:17.837093+00
9       auth    0004_alter_user_username_opts   2024-06-05 18:06:17.84221+00
10      auth    0005_alter_user_last_login_null 2024-06-05 18:06:17.851903+00
11      auth    0006_require_contenttypes_0002  2024-06-05 18:06:17.851903+00
12      auth    0007_alter_validators_add_error_messages        2024-06-05 18:06:17.851903+00
13      auth    0008_alter_user_username_max_length     2024-06-05 18:06:17.869718+00
14      auth    0009_alter_user_last_name_max_length    2024-06-05 18:06:17.869718+00
15      auth    0010_alter_group_name_max_length        2024-06-05 18:06:17.880866+00
16      auth    0011_update_proxy_permissions   2024-06-05 18:06:17.880866+00
17      auth    0012_alter_user_first_name_max_length   2024-06-05 18:06:17.899329+00
18      sessions        0001_initial    2024-06-05 18:06:17.899329+00
19      elama   0001_initial    2024-06-05 18:06:46.05504+00
20      elama   0002_autoevaluacion_volcado     2024-06-15 20:48:47.529242+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
cngs4mx2n3e8zx5a0lz2brao4r5bd10q        .eJxVjDsOwjAQBe_iGln-rT-U9JzBWtsbHEC2FCcV4u4QKQW0b2bei0Xc1hq3QUucCzszyU6_W8L8oLaDcsd26zz3ti5z4rvCDzr4tRd6Xg7376DiqN86kwgafPHWBoHWSaNAwSSFsGSCBdQUsJgkVJI5ZSe1A2_AJ7A0GUPs_QG2Azbp:1sEvLY:ExOPgD29Rhnh56UoR58pEJS_JaecXQI1jhD9SVCERh4    2024-06-19 18:26:52.521631+00
i7fl6ncnib738mk0y66fai7gh8d6mrdk        .eJxVjDsOwjAQBe_iGln-rT-U9JzBWtsbHEC2FCcV4u4QKQW0b2bei0Xc1hq3QUucCzszyU6_W8L8oLaDcsd26zz3ti5z4rvCDzr4tRd6Xg7376DiqN86kwgafPHWBoHWSaNAwSSFsGSCBdQUsJgkVJI5ZSe1A2_AJ7A0GUPs_QG2Azbp:1sEzOR:nI1PRc9kJWvZ7t-UAV3_OoYdI7K7yw3D2Kx3Updulbs    2024-06-19 22:46:07.275167+00
1vdgxoedrbt981oa3vpvhldpbkn1tz2k        .eJxVjDsOwjAQBe_iGln-rT-U9JzBWtsbHEC2FCcV4u4QKQW0b2bei0Xc1hq3QUucCzszyU6_W8L8oLaDcsd26zz3ti5z4rvCDzr4tRd6Xg7376DiqN86kwgafPHWBoHWSaNAwSSFsGSCBdQUsJgkVJI5ZSe1A2_AJ7A0GUPs_QG2Azbp:1sImiX:ya19HCX36dXUqv8g-nwfQLGwG9GHqujAyLZ7qW8GECs    2024-06-30 10:02:33.538575+00
bis0y084nlz1ovadcuwdfu3j1zmilhtn        .eJxVjDsOwjAQBe_iGln-xR9K-pzBste7OIAcKU4qxN1JpBTQzsx7bxbTtta4dVziVNiVSXb5ZTnBE9shyiO1-8xhbusyZX4k_LSdj3PB1-1s_w5q6nVfC_CBlHPaBJu1yI4SqYEoOIU6gzMIMhuvwOzAeCiFpB1UQStJO4Hs8wXjGTgT:1tqZxS:x-kV0_bc8aBeqJN7JB9LOeLnAns0J9Z5IM_6ycq5YQM    2025-03-21 15:49:54.69+00
y9o6tf3ftltxqwjw2b97ykj2rfnw2s1e        .eJxVjDsOwjAQBe_iGln-xR9K-pzBste7OIAcKU4qxN1JpBTQzsx7bxbTtta4dVziVNiVSXb5ZTnBE9shyiO1-8xhbusyZX4k_LSdj3PB1-1s_w5q6nVfC_CBlHPaBJu1yI4SqYEoOIU6gzMIMhuvwOzAeCiFpB1UQStJO4Hs8wXjGTgT:1tt7Bt:uPxVzzY5aIoy1bD205t274901IrSP3ntm1j9S4tQL20    2025-03-28 15:43:17.706141+00
\.


--
-- Data for Name: elama_autoevaluacion; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.elama_autoevaluacion (id, fecha_hora, finalizada) FROM stdin;
1       2024-06-15 20:50:45.933622+00   f
2       2024-06-15 20:51:25.488052+00   f
3       2024-06-15 20:53:46.252862+00   f
4       2024-06-15 20:55:45.721798+00   f
5       2024-06-16 09:30:45.134221+00   t
6       2024-06-16 15:35:42.727897+00   t
7       2025-01-07 20:04:47.502534+00   f
8       2025-03-07 15:07:30.726398+00   f
9       2025-03-07 15:15:26.823401+00   f
10      2025-03-07 15:47:32.565413+00   f
11      2025-03-07 15:49:38.748783+00   f
12      2025-03-07 15:49:58.932085+00   f
13      2025-03-07 16:44:23.977436+00   f
14      2025-03-07 17:00:27.575822+00   f
15      2025-03-07 23:44:19.984262+00   f
16      2025-03-14 15:43:25.434516+00   f
\.


--
-- Data for Name: elama_descriptor; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.elama_descriptor (id, titulo, contenido_html, descriptor_padre_id, principio_id) FROM stdin;
1       1.1. Comprender de manera profunda el reto migratorio.  <p>El desarrollo del programa de ELAMA se hace a partir de una comprensión profunda del fenómeno migratorio. Se conoce el marco jurídico nacional respecto a las migraciones y las políticas específicas que se refieren a la educación (en general) y a la formación lingüística (en particular) de las personas migrantes adultas.</p>\r\n<p>El equipo responsable del programa de ELAMA se interesa por conocer y difundir internamente informes y datos actualizados de la migración en la comunidad, en el país y en el contexto internacional.</p>\N      1
2       1.2. Concebir la enseñanza del español como un derecho educativo.       <p>El programa de ELAMA se fundamenta en que tanto el aprendizaje del español como la alfabetización en español son un derecho de todas las personas migrantes asentadas en la comunidad, y que al igual que el resto de derechos humanos, han de tener alcance universal, independientemente de la edad, el género, el estatus migratorio, etc.</p>\r\n<p>En ningún caso, se entiende la acción del programa de ELAMA desde una mera perspectiva asistencial o de ayuda, sino desde la convención de que es imprescindible asegurar prácticas educativas igualitarias y de calidad para toda la ciudadanía.</p>\r\n<p>En la documentación del programa de ELAMA se ha incluido referencia a los numerosos tratados y acuerdos internacionales en los que está recogido el derecho a la educación de las personas migrantes y se promueve su conocimiento interno (entre los usuarios y los participantes en el programa).</p>  \N      1
3       1.3. Conocer iniciativas y experiencias de referencia.  <p>Se conocen las principales iniciativas y experiencias nacionales e internacionales en la atención socioeducativa y lingüística a personas adultas migrantes y los actores implicados en ellas (instituciones y entidades internacionales, nacionales y locales).</p>\r\n<p>El equipo responsable del programa de ELAMA está familiarizado con los trabajos y recursos que ya están elaborados y publicados para la formación lingüística de personas migrantes y los utilizan en el programa, bien directamente, bien como referencia para la elaboración de recursos y materiales propios.</p>\r\n<p>La entidad cuenta con herramientas formativas (jornadas, talleres, cursos, etc.) e informativas (comunicaciones, repositorios, manuales, etc.) para trasladar este conocimiento a los equipos que desarrollan los servicios de enseñanza y los servicios de apoyo a los participantes en el programa.</p>      \N     1
4       1.4. Definir las bases del programa.            \N      1
5       1.4.1. Enfatizar la orientación al alumno y la perspectiva de la educación de adultos.  <p>La orientación del programa de ELAMA se basa en los principios de la educación de adultos. </p>\r\n<p>Se parte del reconocimiento del participante en el programa como fuente y capital de conocimiento. Las experiencias vividas por los alumnos y las narrativas propias son un recurso habitual en la formación y en el desarrollo de actividades y tareas de aprendizaje. Se reconoce su contribución  en la creación de un espacio en el aula seguro y respetuoso para todos.</p>\r\n<p>Se fomenta un aprendizaje participativo y experiencial para favorecer la implicación en el aprendizaje de los participantes en el programa.</p>41
6       1.4.2. Ir más allá del aprendizaje de la lengua.        <p>El programa de ELAMA tiene una finalidad formativa que va más allá del aprendizaje del español. Su enfoque instrumental y la consideración de la formación en el marco del aprendizaje a lo largo de toda la vida, permite integrar otros objetivos relacionados con la alfabetización, el acceso al empleo, la educación, los servicios públicos y la participación comunitaria y ciudadana.</p>\r\n<p>Para alcanzar estos objetivos que van más allá del aprendizaje del español, se cuenta con una amplia oferta formativa de cursos de español en la que se tratan estos temas (empleo, educación, vivienda, servicios públicos, participación comunitaria, etc.).  El programa cuenta además con servicios complementarios a las clases de español donde se prestan servicios de apoyo para la integración a los destinatarios del programa.</p>\r\n<p>El equipo del programa de ELAMA lo integran tanto profesores de español, como educadores, trabajadores sociales y otros profesionales. Estos pueden formar parte del equipo de la entidad o estar vinculados a otras entidades colaboradoras en el programa.</p> 4       1
7       1.4.3. Asumir presupuestos de educación inclusiva y emancipatoria.      <p>El equipo de la entidad es consciente de que los participantes en el programa de ELAMA pueden ser personas vulnerables en riesgo de exclusión social que necesitan apoyo significativo para superar las barreras que limitan su formación (costes, disponibilidad, formación previa, etc.). Por ello, las actividades formativas del programa incluyen objetivos relacionados con la inclusión social y la interacción con la comunidad, desarrollan prácticas igualitarias y se fundamentan en valores y principios sociales, cívicos y democráticos.</p>\r\n<p>El programa de ELAMA tiene una finalidad emancipatoria: capacitar a los participantes en los cursos para ser conscientes de sus propios propósitos y del uso que pueden hacer del español a fin de participar e influir positivamente en su contexto social más inmediato.</p>      4       1
8       1.4.4. Adoptar un enfoque de educación integral.        <p>El programa de ELAMA contempla la atención del alumno de manera integral. Se atienden sus necesidades de aprendizaje y de uso de la lengua, pero también sus necesidades afectivas y sociales. En concreto, se pone especial atención en el desarrollo de habilidades que facilitan el desarrollo personal y el bienestar (por ejemplo, resiliencia y espíritu crítico, actitudes positivas, compromiso, relaciones, significado y logro).</p>\r\n<p>La entidad desarrolla alianzas con otros organismos y entidades (instituciones de salud, ONG, centros comunitarios, colegios profesionales, etc.) o con educadores y psicólogos para la prestación de servicios de apoyo a los participantes en el programa.</p>        4       1
9       1.4.5. Adoptar un enfoque intercultural.        <p>Los fines formativos generales del programa se enmarcan dentro de los de la educación intercultural y ciudadana y están orientados a reconocer la contribución de los distintos grupos sociales al patrimonio cultural de la humanidad.</p>\r\n<p>Para ello, la entidad ha articulado medidas para la promoción y el reconocimiento de la diversidad y cuenta con mecanismos concretos de prevención del racismo y la xenofobia. El equipo trabaja para que los participantes  sean conscientes de la riqueza que aporta formar parte de un entorno y contexto social heterogéneo en el que se reconocen las diferencias y estas se explican a partir de las historias, las experiencias y las circunstancias personales de cada persona.</p>        4       1
10      1.4.6. Asumir expectativas positivas de logro de los alumnos.   <p>Se adopta una perspectiva positiva sobre el potencial de aprendizaje de los adultos migrantes con vistas a generar un entorno seguro y constructivo en el aula y evitar  y prácticas inadecuadas. Se trabaja en detectar y modificar creencias limitantes, tanto de profesores como de alumnos,  que puedan impedir el progreso de su aprendizaje.</p>\r\n<p>Algunas creencias que se cuestionan se refieren, por ejemplo, a asociar a todas las personas adultas migrantes con carencias económicas, procedencia de zonas de renta económica baja o bajo nivel formativo. Se conoce que la investigación ha demostrado que la situación económica de estos aprendientes tiene menor relevancia en su aprendizaje que otras diferencias individuales relacionadas con la edad de llegada a la nueva comunidad, la escolarización y formación previa, el contacto con nativos o el tiempo que llevan ya instalados en el país de acogida.</p> 4       1
11      1.5. Diseñar un plan de desarrollo del programa.        <p>Las bases del programa de ELAMA están recogidas en alguna documentación interna, por ejemplo, en el plan de enseñanza. La entidad cuenta con mecanismos de formación interna para asegurarse de que todas las personas involucradas en el proyecto están familiarizadas con las bases del programa y participan en su revisión y actualización.</p>\r\n<p>Además, la entidad cuenta con un plan para el desarrollo del programa de ELAMA. En él se han incluido objetivos realistas y alcanzables. Asimismo, se han establecido las acciones que se van a realizar anualmente, qué equipos van a estar implicados en ellas y los tiempos y plazos con que se cuenta para ponerlas en marcha.</p>\r\n<p>Se han estimado también los recursos humanos, materiales y financieros que se requieren y que harán viable el plan anual del programa de ELAMA. También se ha determinado cómo se van a evaluar los resultados que se alcancen y la forma de comunicarlos tanto interna como externamente.</p>        \N      1
12      1.6. Conseguir financiación y recursos para el programa.        <p>Los recursos que reúne el programa de ELAMA son suficientes para asegurar una formación de calidad y evitar listas de espera a los migrantes adultos que quieren participar en sus actividades.</p>\r\n<p>Se conocen las opciones de financiación disponibles para el programa: patrocinios, licitaciones, subvenciones, etc. La entidad concursa para la obtención de estas ayudas y, en el caso de poder disponer de ellas, conoce en detalle las características de la formación lingüística que establece el organismo responsable de la financiación. Se asegura que las prácticas del programa de ELAMA sean acordes con ellos y que las personas implicadas en su aplicación estén plenamente informadas.</p> \N      1
13      2.1. Crear el equipo docente.           \N      2
14      2.1.1. Promover un perfil especializado.        <p>El equipo docente de la entidad tiene experiencia y formación profesional especializada en la enseñanza de español para adultos migrantes y en la enseñanza de adultos.</p>\r\n<p>Los miembros del equipo docente conocen las teorías de adquisición de segundas lenguas y lenguas extranjeras y son capaces de relacionar teoría y práctica para adaptar su enfoque metodológico a las expectativas y necesidades de aprendizaje de los migrantes adultos y a las particularidades de la enseñanza en este contexto.</p>\r\n<p>Han desarrollado sensibilidad cultural, étnica y religiosa y son conscientes de la necesidad de adoptar un enfoque inclusivo e intercultural en la enseñanza de español en este contexto. También de la necesidad de ofrecer una respuesta educativa integral a estos aprendientes que, además del desarrollo de sus competencias generales y de la lengua, contemple su formación a lo largo de la vida, su desarrollo personal y su participación en la comunidad de acogida.</p>  13      2
\.


--
-- Data for Name: elama_estrategia; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.elama_estrategia (id, titulo) FROM stdin;
1       Estrategias institucionales
2       Estrategias pedagógicas y de integración
\.


--
-- Data for Name: elama_principio; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.elama_principio (id, titulo, estrategia_id) FROM stdin;
1       1. Establecer las bases del programa.   1
2       2. Dotarse de equipos para hacer posible el programa.   1
3       3. Dotarse de espacios para el desarrollo del programa. 1
4       4. Dotarse de recursos para la enseñanza de español en el programa.     1
5       5. Asegurar el funcionamiento adecuado del programa.    1
6       6. Promocionar el aprendizaje de ELA y difundir el programa.    1
7       7. Recoger datos, evaluar y mejorar el programa.        1
8       8. Reclamar el desarrollo de políticas públicas de ELAMA.       1
9       A. Diseñar la oferta formativa del Programa de ELAMA.   2
10      B. Desarrollar el programa formativo de ELAMA.  2
11      C. Prestar servicios de apoyo para la integración.      2
\.


--
-- Data for Name: elama_volcado; Type: TABLE DATA; Schema: public; Owner: elama
--

COPY public.elama_volcado (id, valoracion, autoevaluacion_id, descriptor_id) FROM stdin;
1       1       4       1
2       1       4       3
3       4       4       2
4       2       5       1
5       3       5       5
6       2       5       2
7       1       5       6
8       1       6       1
9       2       6       2
10      3       6       3
11      4       6       5
12      2       7       1
13      3       7       2
14      4       12      7
15      3       13      8
16      3       13      7
17      2       13      1
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: elama
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: elama
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: elama
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 44, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: elama
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: elama
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: elama
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: elama
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 61, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: elama
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 11, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: elama
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 20, true);


--
-- Name: elama_autoevaluacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: elama
--

SELECT pg_catalog.setval('public.elama_autoevaluacion_id_seq', 16, true);


--
-- Name: elama_descriptor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: elama
--

SELECT pg_catalog.setval('public.elama_descriptor_id_seq', 14, true);


--
-- Name: elama_estrategia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: elama
--

SELECT pg_catalog.setval('public.elama_estrategia_id_seq', 2, true);


--
-- Name: elama_principio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: elama
--

SELECT pg_catalog.setval('public.elama_principio_id_seq', 11, true);


--
-- Name: elama_volcado_id_seq; Type: SEQUENCE SET; Schema: public; Owner: elama
--

SELECT pg_catalog.setval('public.elama_volcado_id_seq', 17, true);


--
-- Name: django_migrations idx_16600_django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT idx_16600_django_migrations_pkey PRIMARY KEY (id);


--
-- Name: auth_group_permissions idx_16607_auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT idx_16607_auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups idx_16612_auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT idx_16612_auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions idx_16617_auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT idx_16617_auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log idx_16622_django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT idx_16622_django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type idx_16629_django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT idx_16629_django_content_type_pkey PRIMARY KEY (id);


--
-- Name: auth_permission idx_16636_auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT idx_16636_auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_group idx_16643_auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT idx_16643_auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_user idx_16650_auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT idx_16650_auth_user_pkey PRIMARY KEY (id);


--
-- Name: django_session idx_16656_sqlite_autoindex_django_session_1; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT idx_16656_sqlite_autoindex_django_session_1 PRIMARY KEY (session_key);


--
-- Name: elama_estrategia idx_16662_elama_estrategia_pkey; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_estrategia
    ADD CONSTRAINT idx_16662_elama_estrategia_pkey PRIMARY KEY (id);


--
-- Name: elama_principio idx_16669_elama_principio_pkey; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_principio
    ADD CONSTRAINT idx_16669_elama_principio_pkey PRIMARY KEY (id);


--
-- Name: elama_descriptor idx_16676_elama_descriptor_pkey; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_descriptor
    ADD CONSTRAINT idx_16676_elama_descriptor_pkey PRIMARY KEY (id);


--
-- Name: elama_autoevaluacion idx_16683_elama_autoevaluacion_pkey; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_autoevaluacion
    ADD CONSTRAINT idx_16683_elama_autoevaluacion_pkey PRIMARY KEY (id);


--
-- Name: elama_volcado idx_16688_elama_volcado_pkey; Type: CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_volcado
    ADD CONSTRAINT idx_16688_elama_volcado_pkey PRIMARY KEY (id);


--
-- Name: idx_16607_auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16607_auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: idx_16607_auth_group_permissions_group_id_permission_id_0cd325b; Type: INDEX; Schema: public; Owner: elama
--

CREATE UNIQUE INDEX idx_16607_auth_group_permissions_group_id_permission_id_0cd325b ON public.auth_group_permissions USING btree (group_id, permission_id);


--
-- Name: idx_16607_auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16607_auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: idx_16612_auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16612_auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: idx_16612_auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16612_auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: idx_16612_auth_user_groups_user_id_group_id_94350c0c_uniq; Type: INDEX; Schema: public; Owner: elama
--

CREATE UNIQUE INDEX idx_16612_auth_user_groups_user_id_group_id_94350c0c_uniq ON public.auth_user_groups USING btree (user_id, group_id);


--
-- Name: idx_16617_auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16617_auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: idx_16617_auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16617_auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: idx_16617_auth_user_user_permissions_user_id_permission_id_14a6; Type: INDEX; Schema: public; Owner: elama
--

CREATE UNIQUE INDEX idx_16617_auth_user_user_permissions_user_id_permission_id_14a6 ON public.auth_user_user_permissions USING btree (user_id, permission_id);


--
-- Name: idx_16622_django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16622_django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: idx_16622_django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16622_django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: idx_16629_django_content_type_app_label_model_76bd3d3b_uniq; Type: INDEX; Schema: public; Owner: elama
--

CREATE UNIQUE INDEX idx_16629_django_content_type_app_label_model_76bd3d3b_uniq ON public.django_content_type USING btree (app_label, model);


--
-- Name: idx_16636_auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16636_auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: idx_16636_auth_permission_content_type_id_codename_01ab375a_uni; Type: INDEX; Schema: public; Owner: elama
--

CREATE UNIQUE INDEX idx_16636_auth_permission_content_type_id_codename_01ab375a_uni ON public.auth_permission USING btree (content_type_id, codename);


--
-- Name: idx_16643_sqlite_autoindex_auth_group_1; Type: INDEX; Schema: public; Owner: elama
--

CREATE UNIQUE INDEX idx_16643_sqlite_autoindex_auth_group_1 ON public.auth_group USING btree (name);


--
-- Name: idx_16650_sqlite_autoindex_auth_user_1; Type: INDEX; Schema: public; Owner: elama
--

CREATE UNIQUE INDEX idx_16650_sqlite_autoindex_auth_user_1 ON public.auth_user USING btree (username);


--
-- Name: idx_16656_django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16656_django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: idx_16669_elama_principio_estrategia_id_97c479af; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16669_elama_principio_estrategia_id_97c479af ON public.elama_principio USING btree (estrategia_id);


--
-- Name: idx_16676_elama_descriptor_descriptor_padre_id_4046c26b; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16676_elama_descriptor_descriptor_padre_id_4046c26b ON public.elama_descriptor USING btree (descriptor_padre_id);


--
-- Name: idx_16676_elama_descriptor_principio_id_6f0c0679; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16676_elama_descriptor_principio_id_6f0c0679 ON public.elama_descriptor USING btree (principio_id);


--
-- Name: idx_16688_elama_volcado_autoevaluacion_id_f401555c; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16688_elama_volcado_autoevaluacion_id_f401555c ON public.elama_volcado USING btree (autoevaluacion_id);


--
-- Name: idx_16688_elama_volcado_descriptor_id_80e2fbb9; Type: INDEX; Schema: public; Owner: elama
--

CREATE INDEX idx_16688_elama_volcado_descriptor_id_80e2fbb9 ON public.elama_volcado USING btree (descriptor_id);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.auth_group(id);


--
-- Name: auth_group_permissions auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id);


--
-- Name: auth_permission auth_permission_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id);


--
-- Name: auth_user_groups auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.auth_group(id);


--
-- Name: auth_user_groups auth_user_groups_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- Name: django_admin_log django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id);


--
-- Name: django_admin_log django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- Name: elama_descriptor elama_descriptor_descriptor_padre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_descriptor
    ADD CONSTRAINT elama_descriptor_descriptor_padre_id_fkey FOREIGN KEY (descriptor_padre_id) REFERENCES public.elama_descriptor(id);


--
-- Name: elama_descriptor elama_descriptor_principio_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_descriptor
    ADD CONSTRAINT elama_descriptor_principio_id_fkey FOREIGN KEY (principio_id) REFERENCES public.elama_principio(id);


--
-- Name: elama_principio elama_principio_estrategia_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_principio
    ADD CONSTRAINT elama_principio_estrategia_id_fkey FOREIGN KEY (estrategia_id) REFERENCES public.elama_estrategia(id);


--
-- Name: elama_volcado elama_volcado_autoevaluacion_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_volcado
    ADD CONSTRAINT elama_volcado_autoevaluacion_id_fkey FOREIGN KEY (autoevaluacion_id) REFERENCES public.elama_autoevaluacion(id);


--
-- Name: elama_volcado elama_volcado_descriptor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: elama
--

ALTER TABLE ONLY public.elama_volcado
    ADD CONSTRAINT elama_volcado_descriptor_id_fkey FOREIGN KEY (descriptor_id) REFERENCES public.elama_descriptor(id);


--
-- PostgreSQL database dump complete
--