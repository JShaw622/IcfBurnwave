#!/bin/bash
#SBATCH --job-name=Hyburn
#SBATCH -p scarf
#SBATCH --output=hyades_output.txt
#SBATCH --ntasks=10
#SBATCH --cpus-per-task=1
#SBATCH --time=23:59:59
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_0.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_0.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_1.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_1.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_2.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_2.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_3.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_3.ppf
hyades -c /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_4.inf
ppf2ncdf /home/vol05/scarf1185/icfBurnwave/test/coldWide/test_4.ppf
