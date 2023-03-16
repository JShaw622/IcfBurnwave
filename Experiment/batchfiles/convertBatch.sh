#!/bin/bash
#SBATCH --job-name=HyburnConvert
#SBATCH -p scarf
#SBATCH --output=convert-output.txt
#SBATCH --ntasks=10
#SBATCH --cpus-per-task=1
#SBATCH --time=23:59:59
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_0_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_0_1.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_1_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_1_1.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_2_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_2_1.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_3_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_3_1.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_4_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/scripts/Cold/test_T_10_4_1.ppf
