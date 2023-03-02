create table banking.customers(
	customer_id serial primary key,
	first_name varchar(36),
	last_name varchar(36),
	passwrd varchar(60),
	email varchar(60),
	phone_number varchar(13),
	address varchar(60)
);

create table banking.bank_accounts(
	account_id serial primary key,
	customer_id int,
	balance float check (0 <= balance),
	constraint customerfk foreign key (customer_id) references Banking.customers(customer_id)
);

create table banking.transactions(
	transaction_id serial primary key,
	time_and_date varchar(26),
	transaction_type varchar(16),
	account_id int,
	amount float,
	constraint accountfk foreign key (account_id) references Banking.bank_accounts(account_id)
);

create table banking.sessions(
	session_id serial primary key,
	customer_id int,
	issue_date_time varchar(26),
	expire_date_time varchar(26),
	constraint customerfk foreign key (customer_id) references Banking.customers(customer_id)
);


insert into banking.customers values (-1, 'test', 'customer', 'work', 'test@email.com', '123-456-7890',
    '123 This Street, City, State, ZIP');

insert into banking.bank_accounts values (-1, -1, 1.00);

insert into banking.transactions values (-1, 'that one time', 'deposit', -1, 1.00);

insert into banking.bank_accounts values (-2, -1, 5000.00);

insert into banking.customers values (-2, 'test', 'customer', 'money', 'no@money.com', '123-456-7890',
    '123 This Street, City, State, ZIP');

insert into banking.bank_accounts values (-3, -1, 50.00);