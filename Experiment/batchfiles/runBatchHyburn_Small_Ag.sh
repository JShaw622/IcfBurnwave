#!/bin/bash
#SBATCH --job-name=Hyburn_Small_Ag
#SBATCH -p scarf
#SBATCH --output=Hyburn_Small_Ag.txt
#SBATCH --ntasks=11
#SBATCH --cpus-per-task=1
#SBATCH --time=23:59:59
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/test/scripts/Small/Ag/test_T_10_0_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/test/scripts/Small/Ag/test_T_10_0_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/test/scripts/Small/Ag/test_T_10_0_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/test/scripts/Small/Ag/test_T_10_1_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/test/scripts/Small/Ag/test_T_10_1_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/test/scripts/Small/Ag/test_T_10_1_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/test/scripts/Small/Ag/test_T_10_2_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/test/scripts/Small/Ag/test_T_10_2_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/test/scripts/Small/Ag/test_T_10_2_2.inf &
wait