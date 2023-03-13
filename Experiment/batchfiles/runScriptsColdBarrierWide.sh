#!/bin/bash
#SBATCH --job-name=Hyburn
#SBATCH -p scarf
#SBATCH --output=hyades_output.txt
#SBATCH --ntasks=20
#SBATCH --cpus-per-task=1
#SBATCH --time=23:59:59
hyades -b -cHbatch
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_0_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_0_1.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_1_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_1_1.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_2_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_2_1.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_3_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_3_1.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_4_0.ppf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_T_10_4_1.ppf
