all: adminserver worker

adminserver: adminserver.c
	gcc -m32 -fno-stack-protector -o adminserver adminserver.c

worker: worker.c
	gcc -m32 -fno-stack-protector -o worker worker.c
