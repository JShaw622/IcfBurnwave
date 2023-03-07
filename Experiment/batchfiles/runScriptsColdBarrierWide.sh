#!/bin/bash
#SBATCH --job-name=Hyburn2
#SBATCH -p scarf
#SBATCH --output=hyades_output.txt
#SBATCH --ntasks=20
#SBATCH --cpus-per-task=1
#SBATCH --time=23:59:59
hyades -c /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_0_0.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_0_0.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_0_1.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_0_1.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_1_0.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_1_0.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_1_1.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_1_1.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_2_0.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_2_0.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_2_1.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_2_1.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_3_0.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_3_0.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_3_1.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_3_1.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_4_0.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_4_0.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_4_1.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/cold/test_T_10_4_1.ppf
