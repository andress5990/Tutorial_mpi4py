# University of Pittsburgh
# Center for Simulation and Modeling (SaM)
# Introduction to MPI with MPI4Py
# Esteban Meneses, PhD
# Description: exchange of messages between two ranks.

from mpi4py import MPI

if not MPI.Is_initialized():
    MPI.Init()

# getting basic info
comm = MPI.COMM_WORLD
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

if size != 2:
    print("Number of ranks should be exactly 2")
    exit()

# ping-pong between two ranks
counter = 0
for x in range(10):
    if rank == 0:
        comm.send(counter, dest=1)
        print 'Root node got counter {counter}'.format(counter=counter)
        counter = comm.recv(source=1)
    else:
        counter = comm.recv(source=0)
        counter += 1
        comm.send(counter, dest=0)
if rank == 0:
    print 'Total number of message exchanges: {counter}'.format(counter=counter)

MPI.Finalize()
