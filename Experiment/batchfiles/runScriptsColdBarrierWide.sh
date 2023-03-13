#!/bin/bash
#SBATCH --job-name=Hyburn
#SBATCH -p scarf
#SBATCH --output=hyades_output.txt
#SBATCH --ntasks=10
#SBATCH --cpus-per-task=1
#SBATCH --time=23:59:59
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_0_0.inf
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_0_1.inf
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_1_0.inf
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_1_1.inf
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_2_0.inf
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_2_1.inf
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_3_0.inf
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_3_1.inf
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_4_0.inf
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_4_1.inf
