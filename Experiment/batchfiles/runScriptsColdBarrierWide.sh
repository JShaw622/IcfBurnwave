#!/bin/bash
#SBATCH --job-name=Hyburn
#SBATCH -p scarf
#SBATCH --output=hyades_output.txt
#SBATCH --ntasks=50
#SBATCH --cpus-per-task=1
#SBATCH --time=23:59:59
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_0_0.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_0_0.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_0_1.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_0_1.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_0_2.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_0_2.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_0_3.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_0_3.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_0_4.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_0_4.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_1_0.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_1_0.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_1_1.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_1_1.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_1_2.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_1_2.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_1_3.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_1_3.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_1_4.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_1_4.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_2_0.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_2_0.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_2_1.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_2_1.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_2_2.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_2_2.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_2_3.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_2_3.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_2_4.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_2_4.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_3_0.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_3_0.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_3_1.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_3_1.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_3_2.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_3_2.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_3_3.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_3_3.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_3_4.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_3_4.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_4_0.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_4_0.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_4_1.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_4_1.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_4_2.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_4_2.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_4_3.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_4_3.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_4_4.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_4_4.ppf
