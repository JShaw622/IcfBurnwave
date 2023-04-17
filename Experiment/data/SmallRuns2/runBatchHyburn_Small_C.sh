#!/bin/bash
#SBATCH --job-name=Hyburn_Small_C
#SBATCH -p devel
#SBATCH --output=Hyburn_Small_C.txt
#SBATCH --ntasks=52
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
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_5_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_5_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_5_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_5_3.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_5_4.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_6_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_6_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_6_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_6_3.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_6_4.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_7_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_7_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_7_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_7_3.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_7_4.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_8_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_8_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_8_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_8_3.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_8_4.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_9_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_9_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_9_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_9_3.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/C/test_T_10_9_4.inf &
wait