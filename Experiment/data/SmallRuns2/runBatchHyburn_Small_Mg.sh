#!/bin/bash
#SBATCH --job-name=Hyburn_Small_Mg
#SBATCH -p scarf
#SBATCH --output=Hyburn_Small_Mg.txt
#SBATCH --ntasks=17
#SBATCH --cpus-per-task=1
#SBATCH --time=23:59:59
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_0_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_0_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_0_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_1_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_1_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_1_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_2_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_2_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_2_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_3_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_3_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_3_2.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_4_0.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_4_1.inf &
srun -n1 --exclusive hyades /home/vol05/scarf1185/icfBurnwave/SmallSample/Scripts/Mg/test_T_10_4_2.inf &
wait