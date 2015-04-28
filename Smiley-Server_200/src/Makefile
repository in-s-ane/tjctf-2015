GCC='gcc -Wall'

all: adminserver worker

adminserver: adminserver.c
	$(GCC) -m32 -fno-stack-protector -o adminserver adminserver.c

worker: worker.c
	$(GCC) -m32 -fno-stack-protector -o worker worker.c
