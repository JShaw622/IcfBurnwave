#!/bin/bash
#SBATCH --job-name=Hyburn_Small_C
#SBATCH -p devel
#SBATCH --output=Hyburn_Small_C.txt
#SBATCH --ntasks=27
#SBATCH --cpus-per-task=1
#SBATCH --time=11:00:00
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_0_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_0_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_0_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_0_3.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_0_4.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_1_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_1_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_1_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_1_3.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_1_4.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_2_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_2_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_2_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_2_3.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_2_4.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_3_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_3_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_3_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_3_3.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_3_4.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_4_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_4_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_4_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_4_3.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_4_4.inf &
wait