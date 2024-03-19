BEGIN;

CREATE SCHEMA msdbom;

CREATE TABLE msdbom.client (
  client_id SERIAL PRIMARY KEY,
  company_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(255) NOT NULL,
  contact_no VARCHAR(50),
  email_address VARCHAR(100),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE msdbom.product (
  product_id SERIAL PRIMARY KEY,
  setup_type VARCHAR(255),
  name VARCHAR(255),
  description TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE msdbom.department (
  department_id SERIAL PRIMARY KEY,
  department_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE msdbom.employee_position (
  employee_position_id SERIAL PRIMARY KEY,   
  employee_position_title VARCHAR(255) NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE msdbom.employee (
  employee_id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL DEFAULT '',
  last_name VARCHAR(255) NOT NULL DEFAULT '',
  department_id INT,
  employee_position_id INT,
  contact_no VARCHAR(50),
  email_address VARCHAR(100),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT department_id_fk FOREIGN KEY (department_id)
    REFERENCES msdbom.department(department_id),
  CONSTRAINT employee_position_id_fk FOREIGN KEY (employee_position_id)
    REFERENCES msdbom.employee_position(employee_position_id)
);

CREATE TABLE msdbom.job (
  job_id SERIAL PRIMARY KEY,
  sales_executive INT,
  date_created TIMESTAMP NOT NULL DEFAULT now(),
  event_name VARCHAR(255) NOT NULL DEFAULT '',
  event_venue VARCHAR(255) NOT NULL DEFAULT '',
  event_start_date TIMESTAMP NOT NULL DEFAULT now(),
  event_end_date TIMESTAMP NOT NULL DEFAULT now(),
  client_id INT NOT NULL,
  ingress_date TIMESTAMPTZ NOT NULL DEFAULT now(),
  ingress_time TIME NOT NULL DEFAULT CURRENT_TIME,
  egress_date TIMESTAMPTZ NOT NULL DEFAULT now(),
  egress_time TIME NOT NULL DEFAULT CURRENT_TIME,
  prepared_by INT,
  reviewed_by INT,
  approved_by INT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT client_id_fk FOREIGN KEY (client_id)
    REFERENCES msdbom.client(client_id)
);

COMMIT;