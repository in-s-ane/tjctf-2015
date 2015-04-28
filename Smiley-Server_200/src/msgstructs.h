
#ifndef DATA_H
#define DATA_H

#define CAPVAL 1

typedef enum action_e {
	INVALID_ACTION, READ_ACTION, EXEC_ACTION, LOGIN_ACTION, STATUS_ACTION, SMILEY_ACTION, HELP_ACTION, EXIT_ACTION
} action_t;

typedef enum status_e {
	SUCCESS, FAILURE
} status_t;

typedef struct query_s {
	action_t action;
	double credentials;
	long userid;
	char data[256];
} query_t;

typedef struct response_s {
	status_t status;
	char data[256];
} response_t;

#endif

