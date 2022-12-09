create table banking.customers(
	customer_id serial primary key,
	first_name varchar(36),
	last_name varchar(36),
	username varchar(36),
	passwrd varchar(36),
	email varchar(36),
	phone_number varchar(13),
	address varchar(50)
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
	transaction_type varchar(8),
	account_id int,
	amount float,
	constraint accountfk foreign key (account_id) references Banking.bank_accounts(account_id)
);

insert into banking.customers values (-1, 'test', 'customer', 'please', 'work', 'test@email.com', '123-456-7890',
'123 This Street, City, State, ZIP');

insert into banking.bank_accounts values(-1, -1, 0.00);