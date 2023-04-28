#!/bin/bash
#SBATCH --job-name=HyburnConvergence
#SBATCH -p scarf
#SBATCH --output=hyades_output_Convergece.txt
#SBATCH --ntasks=70
#SBATCH --cpus-per-task=1
#SBATCH --time=23:59:59
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_0.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_1.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_2.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_3.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_4.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_5.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_6.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_7.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_8.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_9.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_10.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_11.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_12.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_13.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_14.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_15.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_16.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_17.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_18.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_19.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_20.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_21.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_22.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_23.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_24.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_25.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_26.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_27.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_28.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_29.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_30.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_31.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_32.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_33.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_34.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_35.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_36.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_37.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_38.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_39.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_40.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_41.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_42.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_43.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_44.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_45.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_46.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_47.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_48.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_49.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_50.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_51.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_52.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_53.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_54.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_55.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_56.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_57.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_58.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_59.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_60.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_61.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_62.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_63.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_64.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_65.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_66.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_67.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_68.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/test_69.inf &
wait