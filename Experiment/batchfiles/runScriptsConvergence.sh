#!/bin/bash
#SBATCH --job-name=HyburnConvergence
#SBATCH -p scarf
#SBATCH --output=hyades_output_Convergece.txt
#SBATCH --ntasks=50
#SBATCH --cpus-per-task=1
#SBATCH --time=23:59:59
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_0.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_1.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_2.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_3.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_4.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_5.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_6.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_7.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_8.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_9.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_10.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_11.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_12.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_13.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_14.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_15.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_16.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_17.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_18.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_19.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_20.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_21.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_22.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_23.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_24.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_25.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_26.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_27.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_28.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_29.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_30.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_31.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_32.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_33.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_34.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_35.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_36.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_37.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_38.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_39.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_40.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_41.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_42.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_43.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_44.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_45.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_46.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_47.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_48.inf &
srun -n1 --exclusive hyades -c /home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/test_49.inf &
wait